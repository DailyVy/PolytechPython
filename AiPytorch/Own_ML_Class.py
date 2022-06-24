# ML 모델들을 Class화
# Linear Regression
# Logistic Regression
# Softmax Regression

# class LogistRegression(nn.Module):


import torch.nn as nn
import torch

# 변수명(로컬변수, 글로벌변수), 클래스 명, 객체 생성시 사용명.
# 여러분들 스스로 정의해보세요.
# 일반적으로 클래스, 전역변수 등은 변수의 시작이 대문자로 시작을 함
# 단어가 두 개 이상 조합될 경우 "_"를 사용할 것인지, 또는 Camel기법(다른단어가 나올 때 대문자)으로 할 것인지..
# 변수라면 logic_regression(logicRegression)
# 전역변수를 만들 때 g를 붙인다던지.. gLogisticRegressionModel (global 표현)
class LogisticRegression(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim

        self.linear = nn.Linear(self.in_dim, self.out_dim)
        self.sigmoid = nn.Sigmoid()
    def forward(self, x):
        return self.sigmoid(self.linear(x))



class LinearRegression(nn.Module):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.in_dim = in_dim
        self.out_dim = out_dim

        self.linear = nn.Linear(self.in_dim, self.out_dim)
    def forward(self, x):
        return self.linear(x)

