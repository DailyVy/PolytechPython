import pandas as pd
import matplotlib.pyplot as plt

######### 판다스 내장 그래프 ##########
# 1교시 - 남북한발전전력량.xlsx
# df1 = pd.read_excel("Data/남북한발전전력량.xlsx")
# print(df1.info())
# print(df1.head(10))

# df1 = df1.iloc[[0, 5], 2:] # 0번째가 남한, 5번째가 북한
# df1.index=["south", "North"] # 행인덱스를 숫자형에서 설정해준 값으로 바꾼다.
# print(df1.head())

# df1.plot() # df1.plot.line(), df1.plot(kind='line')과 같음, 아무것도 지정안하면 default가 line이다.
# plt.show() # 바라던 결과가 아니므로 transpose를 할 예정 ==> row가 x축이고 column이 범례인데 현재 column이 연도라 범례가 너무 많다!!!

# df2 = df1.T # Transpose, 열과 행을 바꿈
# print(df2.head())
# df2.plot.line() # line
# df2.plot.bar()  # bar그래프, df2.plot(kind='bar')
# df2.plot.barh() # 수평 bar 그래프
# plt.show()

# 2교시 - auto-mpg.csv
# df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X
#
# # 열 이름 지정
# df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
#               "acceleration", "model_year", "origin", "name"]
# print(df.head())
#
# # 하나의 열을 가지고 오고 싶다. df1에 'mpg'컬럼만 가져오자
# df1 = df['mpg']
#
# ### 히스토그램을 그려봅시다.
# df1.plot.hist(bins=8) # bin은 몇개의 구간으로 나눌지를 결정한다.
# plt.show()
# # bin의 최대 갯수를 어떻개 생각하면 좋을까? - value_counts() 이용
# print(df1.value_counts()) # Name: mpg, Length: 129, dtype: int64
# # Length 가 129 이므로 이를 몇등분으로 할 것인지는 알아서 결정~
#
# ### 산점도를 그려봅시다.
# df.plot.scatter(x="weight", y="mpg") # df.plot(kind="scatter", x="weight", y="mpg")
# plt.show()
#
# ### box plot 을 그려봅시다. - 'mpg', 'cylinder'
# df2 = df[['mpg', 'cylinders']] # column 두 개를 가져 오자, column을 두 개 이상 가져오고 싶을 때는 [[ , ]] 형태로
# df2.plot.box()
# plt.show()

######### MATPLOTLIB 이용 하자 ##########
# 어떤 스타일이 있을까?
print(plt.style.available)
# 나는 ggplot을 사용할래
plt.style.use('ggplot') # plt.style.use('Solarize_Light2')

df = pd.read_excel('시도별 전출입 인구수.xlsx')
# print(df.info())
print(df.head(30))

# todo : 1. 서울에서 다른지역(경기도)으로 이동한 데이터만 주출하여 정리해 보자
# todo : 2. 누락값(NaN)을 앞 데이터로 채워보자 ==> NaN을 서울특별시로 채워넣기 : fillna(method='ffill')
# method='bfill', 'ffill' (f: Forwarding, b:Backwarding)
# forward : NaN이 나오기 바로 이전의 데이터를 사용해서 NaN 값을 대체.
# 언제까지? 빈 데이터가 다 채워질 때 까지!

df1 = df.fillna(method='ffill')
print(df1.head(30))

# Mask 형태로 데이터를 가져와보자
# mask가 True 인 것만 가져와봅시다.
# 서울 ==> 서울로 이동한 인구는 필요 없고, 다른 지역은 관심 없음! 서울에서 타지역으로의 이동에만 관심!
# 전출지가 서울특별시이고, 전입지가 서울특별시인 것
mask = (df1["전출지별"] == "서울특별시") & (df1["전입지별"] != "서울특별시")
# print(mask[19:19+18])
df_seoul = df1[mask]
print(df_seoul.head(3))
# 이제 전출지가 서울인 데이터만 추출했으니까, 전출지별 컬럼을 drop시켜주자
df_seoul.drop(["전출지별"], axis=1, inplace=True)
print(df_seoul.head())
# 이제 전입지별 => 전입지로 column 이름 변경
df_seoul.rename({"전입지별":"전입지"}, axis=1, inplace=True)
print(df_seoul.head())
# 인덱스를 바꿔주자 : 전입지를 index로 사용합시다!
df_seoul.set_index('전입지', inplace=True) # 특정 행을 index로 바꿔준다.
print(df_seoul.head())
# 경기도 행만 가져오자
sr = df_seoul.loc["경기도"] # 이렇게 가져오면 series 로 가져오게되겠지?
print(sr.head())
print(type(sr)) # <class 'pandas.core.series.Series'>
# plt.plot(sr)
# plt.show()

plt.plot(sr)
# 그래프 제목부터 달아봅시다
plt.title("Seoul -> Gyeonggi")
# x축, y축 이름
plt.xlabel("Year")
plt.ylabel("Number of migration")
plt.show()


### 실습 : 서울 -> 대구
# 1. mask 형태로 한번 실습해조고, df.iloc 이용해서도 한 번 해보세요.
# 2. df.replace('-', 0, inplace=True) : 대쉬(-)를 0으로 바꾸기

# 1. mask
# 전출지가 서울특별시이고, 전입지가 서울특별시인 것
mask = (df1["전출지별"] == "서울특별시") & (df1["전입지별"] != "서울특별시")
# print(mask[19:19+18])

df_seoul = df1[mask]
print(df_seoul.head(3))

# 이제 전출지가 서울인 데이터만 추출했으니까, 전출지별 컬럼을 drop시켜주자
df_seoul.drop(["전출지별"], axis=1, inplace=True)
print(df_seoul.head())
# 이제 전입지별 => 전입지로 column 이름 변경
df_seoul.rename({"전입지별":"전입지"}, axis=1, inplace=True)
print(df_seoul.head())
# 인덱스를 바꿔주자 : 전입지를 index로 사용합시다!
df_seoul.set_index('전입지', inplace=True) # 특정 행을 index로 바꿔준다.
print(df_seoul.head())
# 대구 행만 가져오자
seo_dae = df_seoul.loc["대구광역시"] # 이렇게 가져오면 series 로 가져오게되겠지?
print(seo_dae.head())
# - 를 0으로 바꿔주자
seo_dae.replace('-', 0, inplace=True)
print(seo_dae.head())
# 그래프
plt.figure(figsize=(15,7))
plt.plot(seo_dae)
plt.title("Seoul → Daegu")
plt.xlabel("Year")
plt.xticks(rotation=45)
plt.ylabel("Number of migration")
plt.show()

# 2. iloc 이용
print(df1.head())
# print(df1.iloc[22, 2:]) # 전출지별, 전입지별에서 서울, 대구에 해당하는 행 index가 22, 그리고 1970년이 column index가 2
seo_dae2 = df1.iloc[22, 2:]
print(seo_dae2, type(seo_dae2))
# -를 0으로 채워주자
seo_dae2 = seo_dae2.replace('-', 0)
print(seo_dae2)
plt.figure(figsize=(15,10))
plt.plot(seo_dae2)
plt.title("Seoul → Daegu, iloc")
plt.xlabel("Year")
plt.xticks(rotation = 90)
plt.ylabel("Number of migration")
plt.show()