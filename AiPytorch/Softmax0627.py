# 2022.06.27
# softmax regression

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
import numpy as np # pandas ==> get_dummies() ==> DataFrame으로 반환 ==> array Type 으로 변경위해 numpy

# 8 x 4 (4개 특성(특징)을 가진 데이터, row:8)
x_train = [[1, 2, 1, 1],
           [2, 1, 3, 2],
           [3, 1, 3, 4],
           [4, 1, 5, 5],
           [1, 7, 5, 5],
           [1, 2, 5, 6],
           [1, 6, 6, 6],
           [1, 7, 7, 7]]

# GT(or Label Data) 각 샘플([1, 2, 1, 1] ==> 2)에 대한 GT값
# 0, 1, 2 총 3개의 클래스가 존재
y_train = [2, 2, 2, 1, 1, 1, 0, 0]

# one-hot encoding으로 y_train을 변경
# 1) pandas의 get_dummies() 메서드 샤용
# 2) torch: one_hot() 메서드 존재하지 않음
# 파이토치 시작할 떄 사용한, scatter, unsqueeze 메서드 등을 이용해서 구현
# 3) check : nn.Linear(), F.CrossEntropy 사용시
#  y_train 자체를 one-hot encoding으로 하지 않아도 자동으로 변환하는 걸로 알고 있음


# 1) get_dummies() 사용
df = pd.DataFrame({"y_train" : y_train})
# print(df.head())
df = pd.get_dummies(df["y_train"]) # get_dummies(DataFrame["Column Name"])
# print(df.head())

# DataFrame ==> array (8x3) ==> 변환해주어야 학습가능
new_array = np.array(df)
# print(new_array)
# Pytorch에서 사용하기 위해서는 Tensor로 변경
y_train_new = torch.FloatTensor(new_array)
print(y_train_new.shape, y_train_new.dim())

# 2) scatter, unsqueeze를 이용한 one-hot encoding
# y_one_hot의 사이즈를 정의
#  ==> row가 8개 있고, classes가 3개 있으므로 8x3 one-hot encoding
y_one_hot = torch.zeros(8, 3) # 주어진 모양의 텐서를 만들어주는데 0으로 채움 c.f. torch.ones(8, 3)
# print(y_one_hot)
# y_one_hot.scatter_(1, y_train.unsqueeze(1), 1)
# todo. y_train은 list니까 에러 ==> Tensor 형태로 바꿔줘야해
x_train = torch.FloatTensor(x_train)
# y_train = torch.FloatTensor(y_train)

# y_one_hot.scatter_(1, y_train.unsqueeze(1), 1) # RuntimeError: scatter(): Expected dtype int64 for index
# todo. y_train을 scatter_ 메서드 사용을 위해 LongTensor로 변경
y_train = torch.LongTensor(y_train)
y_one_hot.scatter_(1, y_train.unsqueeze(1), 1)
# y_train.sahpe ==> (8, ) ==> (8x1)
# squeeze(제거하다) ==> 8x1 ==> 8
# row(0), col(1) ==> unsqueeze(0) ==> 1x8, unsqeeze(1) ==> 8x1

# scatter(흩어지다): 열 방향 또는 행방향으로 흩어짐
"""
scatter(dim, index, src)
1st param : 어느 dim으로 확장할 건지 결정, 0은 행방향, 1은 열방향
2nd param : LoneTensor type을 받음
3rd param : y_train 값에 해당하는 인덱스에 1을 삽입
y_one_hot.scatter_(1, y_train.unsqueeze(1), 2) 하면 2를 삽입하겠지
_ : inplace=True와 같은 개념(scatter, scatter_)
"""
# print(y_one_hot.shape, y_one_hot)

## 학습을 위한 준비
# 1) weight, bias shape 정의
# 2) optimizer를 뭘 쓸지 정의
# 3) for문에서 정의된 epoch 수만큼 돌면서 w, b값 학습
#  3-1) 가설함수(hypothesis: softmax)
#  3-2) cost function : cross-entropy


"""
x_train shape : 8x4
y_train shape : 8x3

x_train * w ==> y_train
8x4 matrix multiplication 4x3 ==> 8x3
"""

w = torch.zeros((4, 3), requires_grad=True)
b = torch.zeros(3, requires_grad=True)

optimizer = optim.SGD([w, b], lr=1)

# 시간이 되는 분들은.. 수식을 그대로 구현해보세요..
# z = torch.FloatTensor([1, 2, 3])
# torch.exp(z[0])/(torch.exp(z[0]) + torch.exp(z[1]) + torch.exp(z[2]))



# model = nn.Linear(4, 3) # 4개의 출력이 들어가서 3개의 output을 보고싶다. 원래 이거 있으면 weight, bias가 자동으록 계산된다.
# optimizer = optim.SGD(model.parameters(), lr=0.1)

nb_epochs = 1000

for epoch in range(nb_epochs + 1):
    # 1. Hypothesis 함수(Forward)
    # softmax = exp(wx+b)/sum(exp(wx+b))
    # ==> F.softmax
    hx = F.softmax(x_train.matmul(w) + b, dim=1)
    # qna. dim=1이 되어야 하는 이유?
    #  실제 데이터는 가로방향으로 나열되어 있겠지.(컬럼방향)
    #  컬럼방향으로 세 개를 더해주어야 하기 때문에 dim = 1로 보면 된다.
    #  row 방향이라면 dim = 0

    # 2. Cost Function 사용
    # cross-entropy : 1/n Σ(y*(-log(h(x)))) # *: elements-wise곱
    cost = (y_one_hot * -torch.log(hx)).sum(dim=1).mean() # sum하고 전체를 평균...

    # 아니면 아래와 같이 사용하면 된다.
    # pred = model(x_train)
    # cost = F.cross_entropy(pred, y_train) # qna. y_train 여기서 자체적으로 one-hot encoding 하는 듯

    # 3. 최적화 (loss, cost function을 미분하고 경사타고 내려오면서 w, b업데이트)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch:4d}/{nb_epochs}\t, cost:{cost.item():.6f}')
