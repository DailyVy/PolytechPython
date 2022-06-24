import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from Own_ML_Class import LogisticRegression


# Data Prepare
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)

model = LogisticRegression(2, 1)
optimizer = optim.SGD(model.parameters(), lr=1)

nb_epochs = 1000
for epoch in range(nb_epochs):
    hypothesis = model(x_train)
    cost = F.binary_cross_entropy(hypothesis, y_train)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 20 == 0:
        prediction = hypothesis >= torch.FloatTensor([0.5])
        # 실제 y_train 값(GT)하고 예측된 결과 비교한 결과를
        # correct_pred 에 저장

        correct_pred = prediction == y_train
        accuracy = correct_pred.sum().item() / len(correct_pred) # correct_pred.sum() 텐서로 나오니까.item() 해줘야됨

        print(f'Epoch {epoch : 4d}/{nb_epochs}, cost : {cost.item() : .6f} '
              f'Accuracy : {accuracy * 100 : 3.2f}%')