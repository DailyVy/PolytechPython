import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 가설 함수 함수로 작성하기  ==> 시그모이드
def hypothesisFunction(x):
    return 1/(1+torch.exp(-(x.matmul(w) + b)))

# cost(loss)함수 함수로 작성하기
def costFunction(hx ,y):
    return -((y * torch.log(hx)) + ((1-y)*torch.log(1-hx))).mean()

# Data Prepare
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

# w, b의 데이터를 지정
# x_train : 6x2 * 2x1(weight) ==> 6x1 + b(bias: 1)
# w = torch.zeros((size), requires_grad=True)
# w = torch.zeros((2, 1), requires_grad=True) # qna. sigmoid에서 x=0일 때 값이 0.5라서 학습하는데 문제가 없습니다.....???
w = torch.randn((2, 1), requires_grad=True) #
b = torch.zeros(1, requires_grad=True)


optimizer = optim.SGD([w, b], lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs+1):
    # 1. Hypothesis 함수(Forward)
    # sigmoid function 작성한 것을 import
    # sigmoid = 1/1+e^(-wx+b)
    # hx = 1/1+torch.exp(-(x_train.matmul(w) + b)) # Wx + b를 sigmoid에 대입, torch.exp대신 numpy 이용가능
    hx = hypothesisFunction(x_train)

    # 2. Cost Function 사용
    # cost(hx) = 1 : -log(h(x))
    # cost(hx) = 0 : -log(1-h(x))
    # 이 두개를 합친게 슬라이드 28번에 있는 식
    # y는 y_train(GT, 결괏값)
    # cost = -((y_train * torch.log(hx)) + ((1-y_train)*torch.log(1-hx))).mean()
    cost = costFunction(hx, y_train)
    # cost = F.binary_cross_entropy(hx, y_train) # 이걸 우리가 구현한 것이다.

    # 3. 최적화(loss, cost function 을 미분하고
    # 경사타고 내려오면서 w, b 업데이트)
    optimizer.zero_grad()
    cost.backward() # Loss Function 미분 ==> todo. 누적을 막기위해 zero_grad() 작성할 것
    optimizer.step() # SGD, lr 만큼 내려가면서 w, b 업데이트

    # 4. loss값 출력
    if epoch % 100 == 0:
        print(f'Epoch {epoch:4d}/{nb_epochs}\t, cost:{cost.item():.6f}') # cost자체가 tensor기 때문에 tensor에서 값을 가져오려면 item을 붙여줘야함

print(w, b)

# model parameter를 이용한 inference
# training dataset에 대해서 inference
hypothesis = torch.sigmoid(x_train.matmul(w) + b)
# 일반적으로 0.5보다 크면 1로 보고 작으면 0 (기준을 0.5)
# 아니면 좀 더 가혹하게 0.8 기준으로 1 / 0 나누면 됨
print(hypothesis)

# sigmoid 출력값이 0.5 이상이면 1, 아니면 0으로 출력
pred = []
for i in list(hypothesis):
    if i >= 0.5: pred.append(1)
    else: pred.append(0)

print(pred)

# 조금 더 쉽게 알 수 있는 방법은?
prediction = hypothesis >= torch.FloatTensor([0.5]) # True(1) or False(0)
print(prediction)