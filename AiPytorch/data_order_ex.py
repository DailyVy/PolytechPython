import torch
import torch.nn as nn # 여기에 있는 linear regression 을 사용할거야
import torch.nn.functional as F # 여기있는 cost function을 사용할거야

# pytorch에 Dataset, DataLoader 라이브러리를 이용해서
# 데이터를 보다 쉽게 load할 수 있음
# Data shuffle 가능, Batch 등과 같은 옵션을 지정할 수 있음
# augementation : Transform 별도의 라이브러리가 존재
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

x_train = torch.FloatTensor([
    [73, 80, 75],
    [90, 82, 77],
    [78, 98, 100],
    [64, 88, 75]
])

y_train = torch.FloatTensor([
    [152],
    [170],
    [182],
    [148]
])

# TensorDataset : 텐서들을 입력받아
# DataLoader의 입력인자인 Dataset 형태로 변환
dataset = TensorDataset(x_train, y_train)
"""
batch_size는 통상적으로 2의 배수를 자주 사용
shuffle=True : Epoch마다 데이터셋을 섞어서 데이터가 학습되는 순서를 변경
==> 모델이 데이터셋의 순서에 익숙해지는 것을 방지.
마치 우리가 문제은행을 많이 풀면 그다음 문제 풀 때 문제를 안 읽어도 답을 알 듯이
"""
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
model = nn.Linear(3, 1) # Linear regression
# Dimension으로 보면 input은 3개(4x3) output은 1개(4x1)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs):
    # dataloader에서 batch index와 데이터를...
    for batch_idx, samples in enumerate(dataloader):
        x_train, y_train = samples # 데이터를 가지고 왔어, x_train은 (4x3)
        # H(x)계산 - prediction
        prediction = model(x_train) # 계산하면 출력값이 나오겠지
        # cost계산
        cost = F.mse_loss(prediction, y_train)
        # optimization
        optimizer.zero_grad()
        cost.backward() # 미분을 해주고
        optimizer.step() # step하면서 w, b업데이트

        print(f'Epoch {epoch:4d}/{nb_epochs}\t' # 4d: 숫자를 4자리로 포맷팅, cf. 04d는 빈자리에 0을 넣음
              f'Batch {batch_idx + 1}/{len(dataloader)}\t'
              f'Cost: {cost.item():.6f}')
        # cost: Tensor, Tensor의 값을 가지고 오기 위해서 item()사용

# 모델이 가지고 있는 값들은 무엇인가? => 학습 파라미터들
# weight는 3x1이겠고 4x3 * 3x1 하면 4x1이 나오고 bias는 하나 나오겠찌
