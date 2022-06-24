import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# df_scatter = df[['weight', 'mpg']] # 두 개의 컬럼을 가지고 온다.
# print(df_scatter.head())
# # 산점도에서 선형회귀 선을 같이 그리는 함수(라이브러리) regplot
# sns.regplot(x='weight', y='mpg', data=df_scatter, scatter_kws = {"color":"green"}, line_kws={'color':'red'})
# plt.show()

# 히트맵
# Dataset : seaborn에서 제공하는 flights 라는 데이터 셋 사용
# 연도/월별 탑승자수를 한 눈에 보기 위해 히트맵 작성
flights_data= sns.load_dataset('flights')
print(flights_data.head())
df = flights_data.pivot('month', 'year', 'passengers') # row, column, data
print(df.head())
# ax = sns.heatmap(df, annot=True, fmt="d") # annot : True -> 숫자 표시, fmt:"d" -> 정수형태
# plt.title('Heatmap if Flight by Seaborn')
# plt.show()

# matplot을 이용해서 heatmap 작성 가능
plt.pcolor(df)
plt.xticks(np.arange(0, len(df.columns)))
plt.yticks()
plt.colorbar()
plt.show()