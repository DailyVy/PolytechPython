import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Own_ML_Class import LogisticRegression

torch.manual_seed(1)

data = np.loadtxt("./data/data-03-diabetes.csv", delimiter=",", dtype=np.float32)

print(data.shape) # 759, 9 : 맨 마지막게 클래스겠구만

# df = pd.read_csv("./data/data-03-diabetes.csv", header=None)
# print(df.shape)
#
# print(df.info())
# print(df.value_counts())

# train/test set 나누기
x_train = data[:-20, :-1]
y_train = data[:-20, -1]
x_test = data[-20:, :-1]
y_test = data[-20:, -1]


#
# print(y_train)


x_train = torch.FloatTensor(x_train)
y_train = torch.FloatTensor(y_train)
y_train = y_train.view([739, -1])

print(x_train.shape)
print(y_train.shape)

# nn.Module 층을 차례로 쌓을 수있도록
model = nn.Sequential(
    nn.Linear(8, 1), # input_dim, output_dim
    nn.Sigmoid()
)


print("===========model.parameters()==============")
print(list(model.parameters()))

optimizer = optim.SGD(model.parameters(), lr=1)

# 모델 초기화
# W = torch.zeros((8, 1), requires_grad=True)
# b = torch.zeros(1, requires_grad=True)


nb_epochs = 1000

for epoch in range(nb_epochs):
    hypothesis = model(x_train) # 이게 forward가 되는거라고...?
    # hypothesis = model(x_train)
    cost = F.binary_cross_entropy(hypothesis, y_train)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 20 == 0:
        prediction = hypothesis >= torch.FloatTensor([0.5])

        correct_pred = prediction == y_train
        accuracy = correct_pred.sum().item() / len(correct_pred)

        print(f'Epoch {epoch : 4d}/{nb_epochs}, cost : {cost.item() : .6f} '
              f'Accuracy : {accuracy * 100 : 3.2f}%')


x_test = torch.FloatTensor(x_test)
y_test = torch.FloatTensor(y_test)
y_test = y_test.view([20, -1])

pred_y = model(x_test)
# print(pred_y)
result = pred_y >= torch.FloatTensor([0.5]) # 0.5를 넘으면 True, 넘지않으면 False로 정함
GT = result == y_test # 실제 값과 일치하는 경우만 True로 간주
accuracy = GT.sum().item() / len(GT)
print(f'Test Accuracy : {accuracy * 100 : 3.2f}%')