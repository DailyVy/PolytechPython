import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auto-mpg.csv", header=None)  # 컬럼명 X

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# 산점도 : weight, mpg
print(df.head())
x = list(df["weight"])  # 반환되는 type : Series ==> Series를 list로 바꿀 것이다(numpy를 이용하기 위해서)
y = list(df["mpg"])

# 선형회귀(1차: 직선, numpy: polyfit 사용)
# 직선의 방정식에서 출력되는 것 y = ax + b (기울기와 절편)
# grad: 기울기, intercept: 절편
grad, intercept = np.polyfit(x, y, deg=1)  # deg=1 : 1차함수로 그려줄거야
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y, color="green")

# np.linspace(start, end, num)
# num : start, end 를 몇 등분 할 것인지
# start:1, end:10, num:10 ==> 10등분을 하는거니까 x축이 1씩 증가
# start:1, end:10, num:20 ==> 20등분을 하는거니까 x축이 0.5씩 증가
xseq = np.linspace(min(x), max(x), num=len(x))
# 직선을 그리기 위해 x축은 linspace를 통해서 지정
# y축은 grad, intercept를 구했다. y = grad * x + intercept
ax.plot(xseq, grad*xseq + intercept, color="red", lw=2.5) # x축은 xseq, y축은 방정식...
plt.show()