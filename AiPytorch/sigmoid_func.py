# 1. LinearReg0530.py 파일에
# plot_variable() 함수를 import
# 2. cost, sigmoid, paper의 수식들을 보고 코드화 할 수 있어야 함.
# from LinearReg0530 import plot_variable
# from Plot import plot_variable
import numpy as np # sigmoid 함수에서 exponentiol
import matplotlib.pyplot as plt

# sigmoid 함수 작성해봅시다.
# 슬라이드 참고하세요
# sigmoid = 1/(1+e^(-(Wx +b))
# Wx + b를 입력으로 주자
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def plot_variable(x, y, z='', **kwargs):
    print("1")
    l = []
    for d in [x, y]:
        l.append(d) # l.append(d.data) 하니까 나는 안돼
        print(l)
    plt.plot(l[0], l[1], z, **kwargs)

if __name__ == "__main__":
    # sigmoid (in_param): -5 ~ 5
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    print(len(x), len(y))
    print("================")
    print(x.data)
    print("================")

    print("why??")

    print(np.__version__)

    # plt.plot(x, y, 'g')
    plot_variable(x, y) # TypeError: memoryview: invalid slice key
    plt.plot([0,0], [1,0], ":")
    plt.title("Sigmoid Function")
    plt.show()