import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# auto-mpg 데이터셋에서 제조국(origin)을 counting하여 파이차트로 표현
# groupby 사용을 위해서 count 된 값을 넣기 위한 count 컬럼 생성 ==> DataFrame형식으로 나옴
# df['count'] =  1
# print(df.head())
# # 제조국가(origin)열을 기준으로 그룹화 및 합계 연산
# df_origin = df.groupby('origin').sum()
# print(df_origin.head())
#
# # 제조국가 값(1, 2, 3)을 usa, eu, japan으로 변경
# df_origin.index=["USA", "EU", "JAPAN"]
# print(df_origin.head())
# df_origin['count'].plot(kind='pie', figsize=(7, 5),
#                         autopct="%.2f%%", colors=['chocolate', 'bisque', 'cadetblue']) # autopct(auto percentage): 퍼센테이지 표현
# plt.title('Model Origin')
# plt.legend(labels=df_origin.index, loc='upper right')
# plt.show()

# 교수님 풀이 value_counts()
df_origin2 = df['origin'].value_counts() # ==> Series형식으로 나옴
print(df_origin2.head())
# df_origin2.plot(kind='pie')

# value_counts()를 이용해서 만들어봅시다.
df2 = df.replace({'origin':1}, 'usa')
df2 = df2.replace({'origin':2}, 'eu')
df2 = df2.replace({'origin':3}, 'japan')
# print(df2.head())
print(df2['origin'].value_counts())
plt.figure(figsize=(7,5))
plt.pie(df2['origin'].value_counts(), colors=['chocolate', 'bisque', 'cadetblue']
        ,autopct="%.2f%%")
plt.title("Model Origin")
plt.legend(labels=df2.origin.value_counts().index, loc='upper right')
plt.show()

