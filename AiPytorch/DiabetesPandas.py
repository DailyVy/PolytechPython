import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Own_ML_Class import LogisticRegression

torch.manual_seed(1)
#
# data = np.loadtxt("./data/data-03-diabetes.csv", delimiter=",", dtype=np.float32)
#
# print(data.shape) # 759, 9 : 맨 마지막게 클래스겠구만

df = pd.read_csv("./data/data-03-diabetes.csv", header=None)
print(df.shape)

print(df.info())
print(df[8].value_counts()) # 1 : 496, 0 : 263

# train/test set 나누기

train_set = df.iloc[:-20, :]
test_set = df.iloc[-20:, :]

print(train_set.shape)
print(test_set.shape)

# pandas에서 numpy array로 바꿔주기
train_set = train_set.to_numpy()
test_set = test_set.to_numpy()

train_x = train_set[:, :-1]
train_y = train_set[:, -1].reshape(len(train_set), -1) # 이번엔 numpy에서 reshape
test_x = test_set[:, :-1]
test_y = test_set[:, -1].reshape(len(test_set), -1)
# print(train_y)

train_x = torch.FloatTensor(train_x)
train_y = torch.FloatTensor(train_y)
test_x = torch.FloatTensor(test_x)
test_y = torch.FloatTensor(test_y)

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
    hypothesis = model(train_x)
    # hypothesis = model(x_train)
    cost = F.binary_cross_entropy(hypothesis, train_y)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 20 == 0:
        prediction = hypothesis >= torch.FloatTensor([0.5])

        correct_pred = prediction == train_y
        accuracy = correct_pred.sum().item() / len(correct_pred)

        print(f'Epoch {epoch : 4d}/{nb_epochs}, cost : {cost.item() : .6f} '
              f'Accuracy : {accuracy * 100 : 3.2f}%')


pred_y = model(test_x)
# print(pred_y)
result = pred_y >= torch.FloatTensor([0.5]) # 0.5를 넘으면 True, 넘지않으면 False로 정함
GT = result == test_y # 실제 값과 일치하는 경우만 True로 간주
accuracy = GT.sum().item() / len(GT)
print(f'Test Accuracy : {accuracy * 100 : 3.2f}%')