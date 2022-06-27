import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

temp_df = pd.read_csv("./data/data-04-zoo.csv")
# print(temp_df.head(20))
df = temp_df.iloc[18:, :]
# print(temp_df.head(20))

df.columns = ["hair", "feathers", "eggs", "milk", "airborne",
                   "aquatic", "predator", "toothed", "backbone", "breathes",
                   "venomous", "fins", "legs", "tail", "domestic", "catsize",
                   "type"]

# print(temp_df.head(20))
df.index = [i for i in range(len(df))]
# print(len(df)) # 101
# print(df.head(20))
# print(df.tail(20))


# hair, feathers, aquatic 이 object 타입이라 float로 타입변환
# df["hair"] = df["hair"].astype("float")
# df["feathers"] = df["feathers"].astype("float")
# df["aquatic"] = df["aquatic"].astype("float")

# 위 방법보다 아래방법 추천
df = df.astype({"hair" : "float", "feathers" : "float", "aquatic" : "float"})

print(df.info())

# print(df["hair"].value_counts())
# print(df["feathers"].value_counts())
# print(df["aquatic"].value_counts())

# train set
x_train = df.iloc[:-30, :-1]
x_array = np.array(x_train)
# print(x_train.info()) # hair, feathers, aquatic이 object네.. df 에서 미리 바꿔놓을 걸..
x_train_new = torch.FloatTensor(x_array)

y_train = df.iloc[:-30, -1:]
y_train = pd.get_dummies(y_train["type"]) # 클래스는 0부터 6까지 총 7개 # one-hot encoding
new_array = np.array(y_train)
y_train_new = torch.FloatTensor(new_array)


# test set
x_test = df.iloc[-30:,:-1]
y_test = df.iloc[-30:, -1:]

x_testArr = np.array(x_test)
x_test_new = torch.FloatTensor(x_testArr)

y_test = pd.get_dummies(y_test["type"])
y_testArr = np.array(y_test)
y_test_new = torch.FloatTensor(y_testArr)

print(x_train_new)
print(x_train_new.shape) # 71 x 16
print(y_train_new)
print(y_train_new.shape) # 71 X 7

# 그러면 w는 16 x 7 이 되어야 y_train_new의 shape이 101 x 7이 되겠네

w = torch.zeros((16, 7), requires_grad=True)
b = torch.zeros(7, requires_grad=True)

optimizer = optim.SGD([w, b], lr=1)

nb_epochs = 1000

for epoch in range(nb_epochs + 1):
    # 1. 가설함수 ==> softmax
    hx = F.softmax(x_train_new.matmul(w) + b, dim=1)

    # 2. cost function
    cost = (y_train_new * -torch.log(hx)).sum(dim=1).mean()

    # 3. 최적화
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f'Epoch {epoch:4d} / {nb_epochs}\t, cost {cost.item():.6f}')

