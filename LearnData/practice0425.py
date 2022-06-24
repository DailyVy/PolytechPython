import pandas as pd
import matplotlib.pyplot as plt

# 남북한 발전 전력량
# df1 = pd.read_excel("Data/남북한발전전력량.xlsx")
# # print(df1.info())
# # print(df1.head(10)) # 행인덱스 0이 남한, 행인덱스 5가 북한
#
# df1 = df1.iloc[[0,5], 2:] # 열인덱스 2부터 연도별~(1990 1991 1992 ... )
# df1.index = ["South", "North"] # 행인덱스를 새로 지정한다.
#
# print(df1.head())
#
# # df1.plot.line()
# # plt.show()
#
# # 열과 행을 바꾸자. column 이 label이 된다.
# df2 = df1.transpose() # 아니면 df2 = df1.T
# print(df2.head())
#
# df2.plot(kind="line")
# # df2.plot.bar()
# plt.show()


# auto-mpg.csv
# df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X
# print(df.head())
#
# # 컬럼명 지정
# df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin", "name"]
# print(df.head())
#
# df1 = df["mpg"]
#
# # 히스토그램을 그려봅시다.
# # df1.plot.hist(bins=8)
# # plt.show()
# print(df1.value_counts())
#
# # 산점도를 그려봅시다.
# # df.plot.scatter(x="weight", y="mpg")
# # plt.show()
#
# df2 = df[["mpg", "cylinders"]] # column두개를 가져온 df2
# print(df2.head())
# df2.plot(kind="box")
# plt.show()

# plt 스타일봅시다
print(plt.style.available)
# 나는 ggplot을 이용할래
plt.style.use('ggplot') # plt.style.use('Solarize_Light2')

df = pd.read_excel("시도별 전출입 인구수.xlsx")
print(df.head(30))
print(df.info())