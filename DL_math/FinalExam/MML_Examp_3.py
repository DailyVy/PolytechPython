# 3. 입력층에 있는 Weight들이 출력 층의 Error에 미치는 영향을 계산하기 위해서 Chain-rule을 이용한
#  Backpropagation을 수행하여야한다. 다음과 같은 신경망이 주어졌을 때, Backpropagation에 의해 업데이트 되는
#  Weight들을 구하는 코드를 작성하고 "MML_Exam_3.py"로 저장하여 제출하시오.

## 실제 코드 작성시에는
# w1 = 0.2, w2 = 0.23, w3 = 0.38, w4 = 0.35, w5 = 0.42, w6 = 0.32, w7 = 0.64, w8 = 0.6으로
# 셋팅 후 계산 결과를 도출하시오

## 조건 1: Weight 5, 6, 7, 8 이 Total Error에 미치는 영향을 구하는 코드만 작성하시오.
## 조건 2: Forward phase에서 계산되어지는 값은 미리 계산해놓고 z3, z4 를 w5, w6, w7, w8로 편미분한 값도 미리 계산해 놓는다.
## 조건 3: sigmoid 함수는 별도로 만들어서 사용하며, Learning Rate는 0.5 로 셋팅한다.

import numpy as np

def sigmoid(val):
    return 1 / (1 + np.exp(-val))

lr = 0.5

x1, x2 = 0.1, 0.2

w1 = 0.2
w2 = 0.23
w3 = 0.38
w4 = 0.35
w5 = 0.42
w6 = 0.32
w7 = 0.64
w8 = 0.5


# x1, x2 = 0.1, 0.2
#
# w1 = 0.3
# w2 = 0.25
# w3 = 0.4
# w4 = 0.35
# w5 = 0.45
# w6 = 0.4
# w7 = 0.7
# w8 = 0.6



z1 = x1 * w1 + x2 * w2
z2 = x1 * w3 + x2 * w4
h1 = sigmoid(z1)
h2 = sigmoid(z2)

z3 = w5 * h1 + w6 * h2
z4 = w7 * h1 + w8 * h2

# dz3/dw5, dz3/dw6, ...  편미분한 값,
dz3_w5 = h1
dz3_w6 = h2

dz4_w7 = h1
dz4_w8 = h2

# 예측값
o1 = sigmoid(z3)
o2 = sigmoid(z4)

# 실제값
target_o1 = 0.4
target_o2 = 0.6

Eo1 = 0.5*(target_o1 - o1)**2
Eo2 = 0.5*(target_o2 - o2)**2

Etotal = Eo1 + Eo2

print(z1, z2, h1, h2, z3, z4, o1, o2, Etotal)

def backpropagation_1(weight, d_weight, target, output):
    """
    :param weight: weight
    :param d_weight: dz / dw
    :param target: 실제값
    :param output: 예측값
    :return: 새로운 weight
    """

    """
    dEtotal/do1 = -(target_o1 - output_o1)
    """
    dEtotal_o = -(target - output)
    # print("dEtotal/do : ", dEtotal_o)


    """
    do1/dz3 = o1 * (1 - o1)
    """
    do_z = output * (1 - output)
    # print("do/dz : ", do_z)

    """
    dz3/dw5 = h1 
    ==> d_wegiht 로 미리 계산함
    """

    """
    dEtotal/dw5 = dEtotal/do1 * do1/dz3 * dz3 * dw5
    """
    dEtotal_w = dEtotal_o * do_z * d_weight

    newWeight = weight - (lr * dEtotal_w)

    return round(newWeight, 8)

if __name__ == "__main__":
    print(backpropagation_1(w5, dz3_w5, target_o1, o1))
    print(backpropagation_1(w6, dz3_w6, target_o1, o1))
    print(backpropagation_1(w7, dz4_w7, target_o2, o2))
    print(backpropagation_1(w8, dz4_w8, target_o2, o2))

