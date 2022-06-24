import pandas as pd
from matplotlib import pyplot as plt

from matplotlib import font_manager, rc
font_path = "malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 스타일 적용
# print(plt.style.available)
plt.style.use("ggplot")

df = pd.read_excel("시도별 전출입 인구수.xlsx", engine="openpyxl", header=0) # engine="openpyxl"은 무엇인가
# print(df.head())

# iloc[] <-- index는 데이터를 보고 알아서 카운팅해야 함....
# NaN을 특정값으로 채워야함
df = df.fillna(method="ffill")
# iloc[행, 열]
# print(df.head(30))
tmp = df.iloc[19:37, 1:]
print(tmp.head())
# mask
mask = (df["전출지별"] == "서울특별시") & (df["전입지별"] == "대구광역시")
df_daegu = df[mask]
print(df_daegu) # 전출지별, 전입지별 제거 혹은 수정, 그리고 "-"값을 교체
df_daegu.replace("-", 0, inplace=True) # "-" 값을 0으로 교체
df_daegu = df_daegu.drop(["전출지별", "전입지별"], axis=1) # column방향으로 지움(axis=1)
print(df_daegu)
# 시리즈 형태로 가져와봅시다
sr_daegu = df_daegu.iloc[0, :] # 만약 df_daegu.loc으로 할거면 지금 행 이름이 정수형으로 22라서 df_daegu.loc[22, :] 해주면 된다.
print(sr_daegu.head())
# 그려봅시다
# plt.figure(figsize=(15,8))
# plt.plot(sr_daegu)
# plt.xticks(rotation=45)
# plt.title("Seoul → Daegu")
# plt.xlabel("Year")
# plt.ylabel("Number of migration")
# plt.show()


# 이제 경기도 버전으로 해보자
mask = (df["전출지별"] == "서울특별시") & (df["전입지별"] == "경기도")
df_gyeonggi = df[mask]
print(df_gyeonggi) # 전출지별, 전입지별 제거 혹은 수정, 그리고 "-"값을 교체
df_gyeonggi.replace("-", 0, inplace=True) # "-" 값을 0으로 교체
df_gyeonggi = df_gyeonggi.drop(["전출지별", "전입지별"], axis=1) # column방향으로 지움(axis=1)
print(df_gyeonggi)
# 시리즈 형태로 가져와봅시다
sr_gyeonggi = df_gyeonggi.iloc[0, :]
print(sr_gyeonggi.head())
# 그려봅시다, 선그리기 옵션도 이용해봅시다.
# plt.figure(figsize=(16,8))
# plt.plot(sr_gyeonggi, markersize=6, color="olive", marker="*") # 선그리기 옵션 적용
# plt.legend(labels=["Seoul → Gyeonggi"], loc="best") # 범례
# plt.xticks(rotation='vertical') # rotation=90 이랑 같아요
# plt.title("Seoul → Gyeonggi")
# plt.xlabel("Year")
# plt.ylabel("Number of migration")
# plt.show()


# 나 이거 여러개 하고 싶어
# mask = (df["전출지별"] == "서울특별시") & (df["전입지별"] != "서울특별시")
# df_local = df[mask]
# print(df_local) # 전출지별, 전입지별 제거 혹은 수정, 그리고 "-"값을 교체
# df_local.replace("-", 0, inplace=True) # "-" 값을 0으로 교체
# df_local = df_local.drop(["전출지별"], axis=1) # column방향으로 지움(axis=1)
# print(df_local)
# # 시리즈 형태로 가져와봅시다
# # sr_local = df_local.iloc[0, :]
# # print(sr_local.head())
# # 그려봅시다, 선그리기 옵션도 이용해봅시다.
# plt.figure(figsize=(16,8))
# plt.plot(sr_local, markersize=6, color="olive", marker="*") # 선그리기 옵션 적용
# plt.legend(labels=["Seoul → Gyeonggi"], loc="best") # 범례
# plt.xticks(rotation='vertical') # rotation=90 이랑 같아요
# plt.title("Seoul → Gyeonggi")
# plt.xlabel("Year")
# plt.ylabel("Number of migration")
# # plt.show()

# 차트에 comment, annotation 달기
# plt.plot(sr_gyeonggi.index, sr_gyeonggi.values) # row와 value 지정
# y축 범위 지정하기 : plt.ylim(min, max)
# plt.ylim(5000, 800000)
# # annotation 표시 : 화살표를 그림
# # 화살표를 그리자
# plt.annotate("" , # 표시할 문자
#              xy=(20, 620000), # 화살표의 머리부분(화살촉이 있는 부분)
#              xytext=(2, 290000), # 화살표의 꼬리부분(시작점)
#              xycoords="data", # 데이터 값에 따라 알아서 움직이게...? 데이터가 있으면 알아서 움직일 수 있게끔 할 수 있다고..
#              arrowprops=dict(arrowstyle="<->", color="skyblue", lw=3), # 화살표의 property => dictionary타입으로 표현, lw: lane width
#              )
# plt.annotate("" , # 표시할 문자
#              xy=(47, 450000), # 화살표의 머리부분(화살촉이 있는 부분)
#              xytext=(30, 580000), # 화살표의 꼬리부분(시작점)
#              xycoords="data", # 데이터 값에 따라 알아서 움직이게...? 데이터가 있으면 알아서 움직일 수 있게끔 할 수 있다고..
#              arrowprops=dict(arrowstyle="->", color="orange", lw=3), # 화살표의 property => dictionary타입으로 표현, lw: lane width
#              )
# # 화살표 위의 텍스트를 표시하자
# # 첫번째 화살표 위에
# plt.annotate("인구이동 증가(1970-1995)" , # 표시할 문자
#              xy=(10, 390000), # 화살표의 중간 쯤에 시작을 하고 싶다.
#              rotation=30,
#              va = 'baseline', # vertical align
#              ha = "center", # horizontal align
#              fontsize=15
#              )
# plt.annotate("인구이동 증가(1995-2017)" , # 표시할 문자
#              xy=(39, 500000), # 화살표의 중간 쯤에 시작을 하고 싶다.
#              rotation=-13,
#              va = 'baseline', # vertical align
#              ha = "center", # horizontal align
#              fontsize=15
#              )
# plt.show()


# # # 화면을 분할하여 여러개 그려봅시당
# fig = plt.figure(figsize=(15, 10))
# # add_subplot(구성된 행, 구성된 열, 순서)
# ax1 = fig.add_subplot(2, 1, 1) # (행의 크기, 열의 크기, 서브플롯 순서) 2행 1열 중 첫번째 객체
# ax2 = fig.add_subplot(2, 1, 2) # (행의 크기, 열의 크기, 서브플롯 순서) 2행 1열 중 두번째 객체
# # plot 옵션(선 그래프에 속성을 정의)
# ax1.plot(sr_daegu, marker="o", color="red", linewidth=2)
# ax2.plot(sr_gyeonggi, marker="*", color="blue", linewidth=2)
# # y축의 범위를 지정(각 그래프마다)
# ax1.set_ylim(-1000, 20000)
# ax2.set_ylim(50000, 800000)
# # x축 label의 기울기 설정
# ax1.set_xticklabels(sr_daegu.index, rotation=75) # 시리즈 대구의 index는 연도!
# ax2.set_xticklabels(sr_gyeonggi.index, rotation=75) # 시리즈 대구의 index는 연도!
# # 범례를 설정해봅시다
# ax1.legend(labels=["서울 -> 대구"], loc="best")
# ax2.legend(labels=["서울 -> 경기"], loc="best")
# plt.show()

# 하나의 그래프를 여러개 그리는데 map이라는 것을 써봅시다.
# map(함수, 리스트) # 리스트대신 다른 타입도 들어갈 수 있어요
# map: 리스트의 요소를 지정된 함수로 처리해주는 함수
print(list(range(1970, 1980))) # [1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979]
print(range(1970, 1980)) # range(1970, 1980)
# 이걸 integer말고 str로 바꿔주는 방법은?
# num_list = [str(num) for num in range(1970, 1980)]
print([str(num) for num in range(1970, 1980)])
# 보통은 for문 써서 코드를 짤텐데 이럴 때 사용하는게 바로 map이다!
print(list(map(str,range(1970, 1980))))

mask = (df["전출지별"] == "서울특별시") & (df["전입지별"] != "서울특별시")
df_seoul = df[mask]
# print(df_seoul.head())
df_seoul = df_seoul.drop(["전출지별"], axis=1)
df_seoul.set_index("전입지별", inplace=True)
df_seoul = df_seoul.replace("-", 0)
# print(df_seoul.head(30))

# 컬럼을 하나 만들자
col_year = list(map(str, range(1970, 2018))) # 1970년도부터 2017년까지를 컬럼 데이터로 만들 거임
df_3 = df_seoul.loc[["강원도", "충청북도", "충청남도"], col_year]
# print(df_3.head())

# 그려보자
fig3 = plt.figure(figsize=(20, 10))
plt.title("서울 → 충남, 경북, 강원 인구 이동")
ax = fig3.add_subplot(1, 1, 1)
ax.plot(col_year, df_3.loc["강원도", :], marker="o", markersize=8, color="green", label="서울 → 강원") # plot(x축, 데이터 자체)
ax.plot(col_year, df_3.loc["충청남도", :], marker="o", markersize=8, color="blue", label="서울 → 충남")
ax.plot(col_year, df_3.loc["충청북도", :], marker="o", markersize=8, color="orange", label="서울 → 충북")
plt.ylim(0, 60000)
plt.xlabel("기간")
plt.ylabel("이동 인구수")
plt.xticks(rotation="vertical")
plt.legend(loc="best")
plt.show()


# 실습해보기
df_4 = df_seoul.loc[["강원도", "충청남도", "경상북도", "전라남도"], col_year]

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,2,2)
ax3 = fig.add_subplot(2,1,1)
ax4 = fig.add_subplot(2,2,1)

ax1.plot(df_4.loc["충청남도", :], marker="o", markersize=8, color="green")
ax2.plot(df_4.loc["경상북도", :], marker="o", markersize=8, color="blue")
ax3.plot(df_4.loc["강원도", :], marker="o", markersize=8, color="red")
ax4.plot(df_4.loc["전라남도", :], marker="o", markersize=8, color="yellow")

plt.show()