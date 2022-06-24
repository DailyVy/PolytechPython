import pandas as pd
from matplotlib import pyplot as plt

from matplotlib import font_manager, rc
font_path = "malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

plt.style.use("ggplot")
df = pd.read_excel("시도별 전출입 인구수.xlsx", engine="openpyxl", header=0) # engine="openpyxl"은 무엇인가

df = df.fillna(method="ffill")


mask = (df["전출지별"] == "서울특별시") & (df["전입지별"] != "서울특별시")
df_seoul = df[mask]
# print(df_seoul.head())
df_seoul = df_seoul.drop(["전출지별"], axis=1)
df_seoul.set_index("전입지별", inplace=True)
df_seoul = df_seoul.replace("-", 0)
print(df_seoul.head(30))

# 컬럼을 하나 만들자
col_year = list(map(str, range(1970, 2018))) # 1970년도부터 2017년까지를 컬럼 데이터로 만들 거임
df_3 = df_seoul.loc[["강원도", "충청북도", "충청남도"], col_year]



# 그려보자
fig3 = plt.figure(figsize=(20, 10))
plt.title("서울 → 충남, 경북, 강원 인구 이동")
ax = fig3.add_subplot(1, 1, 1)
ax.plot(col_year, df_3.loc["강원도", :], marker="o", markersize=8, color="green", label="서울 → 강원") # plot(x축, 데이터 자체)
ax.plot(col_year, df_3.loc["충청남도", :], marker="o", markersize=8, color="blue", label="서울 → 충남")
ax.plot(col_year, df_3.loc["충청북도", :], marker="o", markersize=8, color="orange", label="서울 → 충북")
# plt.ylim(0, 60000)
plt.xlabel("기간")
plt.ylabel("이동 인구수")
plt.xticks(rotation="vertical")
plt.legend(loc="best")
plt.show()