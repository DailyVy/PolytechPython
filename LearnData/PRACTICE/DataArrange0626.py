import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../auto-mpg.csv", header=None) # header=None : 첫번째 행을 컬럼명으로 하지 않음
# print(df.head())

df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# print(df.head())
# print(df.tail())

# 모든 열 출력
pd.set_option("display.max_columns", None)

# print(df.shape) # (398, 9)
# print(df.info()) # 398 non-null, horsepower가 object네, name 은 당연한데..
# print("====================================================")
# print(df.describe())
# print("====================================================")
# print(df.describe(include="all"))
# print(df.describe(include=["object"]))

# print("====================================================")
# print(df.isnull().sum())
# print(df.count()) # 모든 열이 각각 얼마인지 확인

# print("====================================================")
# DataFrame에서 특정 열이 가지고 있는 고유값이 얼마인지 확인
# print(df["origin"].value_counts())
# print(df["origin"].value_counts(dropna=True))


# print(df[["mpg", "weight"]].mean())
# print("=========max값========")
# print(df.max())
# print("=========min값========")
# print(df.min())

# print("========================Corr============================")
# print(df.corr())
# print(df[["mpg","weight"]].corr())

# print("=========================데이터 전처리==========================")
# Data 전처리
# horespower의 경우 "?"가 포함되어 있음
# dfhorse = df["horsepower"][df["horsepower"] == "?"]
# print(dfhorse)
# print(len(dfhorse)) # 총 6개 있음

df["horsepower"].replace("?", np.nan, inplace=True) # "?"를 NaN값으로 변경
df.dropna(axis=0, inplace=True) # NaN 데이터 행단위로 삭제
df["horsepower"] = df["horsepower"].astype("float") # object ==> float형으로
# print(df["horsepower"].dtype)
# print(df.corr())

# horsepower통계
# print(df["horsepower"].min(), df["horsepower"].max(), df["horsepower"].median(), df["horsepower"].mean())

# print(df)

# origin을 counting 해서 파이차트로 표현
# count하기 위해 df["count"]추가
df["count"] = 1

df_origin = df.groupby(["origin"]).sum()
# print(df_origin.head())
# print(df_origin.sum())

# print(df["origin"].value_counts()) # 솔직히 이거랑 똑같은데... ^^ 굳이 count열을 추가해줄 필요가 있었나..?
print(df_origin)

# origin 1, 2, 3되어 있는걸 나라 이름으로 바꿔주자
df_origin.index = ["USA", "EU", "JAPAN"] # 1: usa, 2: eu, 3: japan
print(df_origin.head())

# 이제 그려봅시다.
df_origin["count"].plot(kind="pie", figsize=(7, 5),
                        autopct="%.2f%%", colors=["chocolate", "bisque", "cadetblue"])
plt.title("Model Origin")
plt.legend(labels=df_origin.index, loc="upper right")
# plt.show()


# value_counts()로도 해보기
df2 = df.replace({"origin" : 1}, "usa")
# print(df2)
df2 = df2.replace({"origin" : 2}, "eu")
df2 = df2.replace({"origin" : 3}, "japan")

print(df2["origin"].value_counts())
plt.figure(figsize=(7, 5))
df2["origin"].value_counts().plot(kind="pie", figsize=(7, 5), colors=["chocolate", "bisque", "cadetblue"],autopct="%.2f%%")
# plt.pie(df2["origin"].value_counts(), colors=["chocolate", "bisque", "cadetblue"],autopct="%.2f%%")
plt.title("Origin")
plt.legend(labels=df2.origin.value_counts().index, loc="upper right")
plt.show()