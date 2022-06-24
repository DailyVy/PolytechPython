import torch
import numpy as np
import matplotlib.pyplot as plt


## 1교시


# Function name : get_data
# Param in : None (get_data())
#  <-> 만약 Param 있다면? get_data(param1, param2, ...)
"""
param1:
param2:
"""
#  이런 식으로 파라미터에 대해 작성해줘야 한다.
# Param out : Return [train data : x and y], (input x, GT y)
# Description
"""
학습 데이터를 가지고 오는 함수
np.array를 사용해서 tensor로 변경한 후  Return
"""
def get_data():
    train_X = np.array([3.3, 4.4, 5.5, 6.71, 6.93, 4.168, 9.779, 6.182, 7.59, 2.167,
                        7.042, 10.791, 5.313, 7.997, 5.654, 9.27, 3.1])
    train_Y = np.array([1.7, 2.76, 2.09, 3.19, 1.694, 1.573, 3.366, 2.596, 2.53, 1.221,
                        2.827, 3.465, 1.65, 2.904, 2.42, 2.94, 1.3])
    # x = torch.from_numpy(train_X)
    # print(x.shape)
    X = torch.from_numpy(train_X).float().view(17, 1)
    y = torch.from_numpy(train_Y)

    print(type(X), type(y))

    return X, y


# Function Name : get_weights
# Param in : None
# Param out : random weight and bias values
# Description
"""
학습 파라미터를 생성하는 함수
랜덤한 weight와 bias
- weight, bias는 random normal 한 값으로 셋팅
- randn(random normal 약어) : 정규분포를 기준으로 랜덤한 값 생성 (1)이면 -1~1(σ), 약 68% 값에 해당하는 값을 리턴
- vs.rand : 0 ~ 1사이의 랜덤한 값을 반환(균등하게 나누어서 반환)
- w, b는 항상 미분되어야 하므로(최적값을 찾기 위해 ==> Loss, Cost, Error 값을 최소화) 
   requires_grad = True로 셋팅
"""
def get_weights():
    w = torch.randn(1) # random normal : 평균이 0이고 표준편차가 1인 가우시안 정규분포를 이용해 생성
    w.requires_grad = True # 미분을 할 것이라는 걸 정의, w와 b는 gradient를 계산해주어야 한다는 뜻
    b = torch.randn(1)
    b.requires_grad = True
    return w, b

# Function Name : simple_network (or hypothesis_function)
# Param in : x (Train하기 위한 x(입력) 데이터)
# Param out : 가설함수의 출력 값 (y_pred)
# Description
"""
H(x) = Wx + b
- W: weights, b: bias
"""
def simple_network(x):
    y_pred = torch.matmul(x, w) + b
    return y_pred

# Function Name : loss_fn
# Param in : y, y_pred
"""
prediction 값과 실제 값과 얼마나 차이나는지 확인하려고
- y : 실제 결과 값
- y_pred : 가설함수의 출력 값

최적화하기 위해서 Gradient Descent 알고리즘을 사용한다. 
그러기 위해선 Loss Function 자체는 Convex한 형태를 지녀야 한다.
w := w - alpha(learning rate) * (Loss Function의 기울기)

- MSE(Mean Squared Error)을 loss function으로 선택
- param.grad.data.zero_() : 기울기 값이 있다면(if not param.grad is None) 초기화
- loss.backward() : backward를 호출하여 MSE의 기울기를 계산
"""
# Param out : loss(== error == cost) 값
# Description
def loss_fn(y, y_pred):
    loss = torch.mean((y_pred - y).pow(2).sum())
    for param in [w, b]:
        if not param.grad is None: param.grad.data.zero_() # 값이 있으면 초기화 해준다고
    loss.backward() # backward를 호출 : MSE의 기울기를 계산
    return loss.data

# Function Name : optimize
# Param in : learning_rate
# Param out : None
# description
"""
w, b를 업데이트 해주는 함수
"""
def optimize(lr):
    w.data = w.data - lr * w.grad.data
    b.data -= lr * b.grad.data

# plot_variable 함수는 스스로 작성해 보세요.
# 뒤에 logistic sigmoid 그래프 그릴 때 활용
# kwargs : keyword parameter 사용
# plt.plot(x, y, 'r', linestyle='--')
# plt.plot(x, y, 'ro', linestyle='--')이런식으로 쓰죠
# plot Document. default of z param: blue, o (이렇게 되어있을거라고 한다)
def plot_variable(x, y, z='', **kwargs):
    l = []
    for d in [x, y]:
        l.append(d.data)
    plt.plot(l[0], l[1], z, **kwargs)


# 다른 파일에서 이 모듈을 사용할 때 아래 코드는 실행되지 않는다.
if __name__ == "__main__":
    # print(get_data())

    print(torch.__version__)

    # 학습하기 위한 함수, linear regression 모델을 만들기 위한 함수 작성
    # 결과를 보기 위한 plot 함수도 작성
    # 다음주에 우리가 만든 함수로 학습 진행해보는 코드 간단히 작성
    # grad_zero 해주는 이유에 대해서 코드로 확인

    # train_x, train_y = get_data()
    # w, b = get_weights() # 이거 해줘야... 다음 함수에 w, b 가 들어갈 수 있어
    # simple_network(train_x)
    #
    # # ==> logistic regression -> ...
    #
    # # 한번 테스트 해봅시다.
    # X = [1, 2, 3]
    # Y = [1, 2, 3]
    # # Loss Function을 간결화 하기 위해서 b term은 제거
    # # 그래프를 그리기 위해서 W, cost 값을 넣을 빈 리스트 작성
    # w_val = []
    # cost_val = []
    # for i in range(-30, 50):
    #     weight = i * 0.1 # 0.1은 lr이 되나봐
    #     w_val.append(weight)
    #     curr_cost = ((Y[0] - X[0]*weight)**2 + (Y[1] - X[1]*weight)**2 + (Y[2] - X[2]*weight)**2)/len(X) # mse 수식이 들어감
    #     cost_val.append(curr_cost)
    # # show the cost_function
    # plt.plot(w_val, cost_val)
    # plt.show()



    ############################ 2022/06/13 ################################
    # grad.data.zero_, or optimizer.zero_grad()
    # pytorch에는 위의 초기화 과정이 필요
    # w = torch.tensor(2.0, requires_grad=True)
    # nb_epochs = 20
    # for epoch in range(nb_epochs):
    #     w.grad.data.zero_() # 이거 없으면 미분한 값이 증가한다.
    #     z = 2 * w
    #     z.backward() # dz/dw (z함수를 w로 미분): 2
    #     print(f'w의 함수 z를 w로 미분한 값: {w.grad}')


    # 작성한 함수를 통해서 linear regression 모델 학습
    # 데이터가 어떻게 구성되어 있는지 바라볼 필요가 있다.
    # 학습할 data 확인
    # plot을 통해서 data의 분포를 확인
    train_x, train_y = get_data()
    # plot_variable(train_x, train_y, 'ro')
    # plt.show()

    # get_weights 함수를 작성
    # 함수의 반환 값을 랜덤한 weight, bias 값을 셋팅
    w, b = get_weights()
    # lr 정의
    lr = 1e-4 # (10^(-4) 즉 0.0001)
    print(w)

    for i in range(500): # epoch 값을 정해줘야 하구요
        y_pred = simple_network(train_x) # wx + b 가설함수를 수행하는 파트
        loss = loss_fn(train_y, y_pred)# mse(y와 y_pred의 차의 제곱의 합) => loss값
        if i % 50 == 0: # epoch 50마다 함 찍어봅시다.
            print(f'Loss: {loss}, Weights: {w}, Bias: {b}')
        optimize(lr) # w, b를 업데이트하는 파트

    plot_variable(train_x, train_y, 'ro')
    plot_variable(train_x, y_pred, label='Fitted line')
    plt.show()