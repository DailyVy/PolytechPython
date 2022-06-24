import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
# matplotlib.rcParams['axes.unicode_minus'] = False # y축 음수표현(-) 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel("Data/남북한발전전력량.xlsx", header=0)
print(df.head(10))

# 북한의 전력 발전량만 가지고 옴
df = df.loc[5:9] # iloc, loc
print(df.head())

df.drop("전력량 (억㎾h)", axis=1, inplace=True)
# df.drop("전력량 (억㎾h)", axis='columns', inplace=True) # 윗 코드와 같다.
df.set_index("발전 전력별", inplace=True)
print(df.head())

df = df.T # 열과 행을 바꾸고 싶어요
print(df.head())

# 증감율 계산 (전년대비 증감율 컬럼을 만들고, 이 컬럼을 그래프로 그려주기 위해)
df["총발전량-1년"] = df["합계"].shift(1) # 합계를 밑으로 한칸씩 떨어뜨림, (-1)하면 위로 올라감
print(df.head())
df['증감율'] = ((df["합계"]/df["총발전량-1년"])-1)*100
# df['증감율'] = (((df["합계"]-df["총발전량-1년"])/df["총발전량-1년"]))*100 # 위와 코드 같음
print(df.head())

print(df.iloc[1, 0])
print("shift말고....")

# shift를 사용하지 말고 증감율 컬럼을 만들어 보자!
print(len(df))
df["총발전량-1년_ver2"] = np.nan
print(df.head())
for i in range(len(df)-1):
    df.iloc[i+1, 6] = df.iloc[i, 0] # iloc말고 loc으로 하고싶다....................

print(df.head())
df['증감율_ver2'] = ((df["합계"]/df["총발전량-1년_ver2"])-1)*100
print(df.head())

# 이제 그래프 그리자
plt.style.use("ggplot")
# 막대그래프 stack, 선 그래프를 겹쳐서 그리기
# 수력하고 화력만 가져오자
ax1 = df[["수력", "화력"]].plot(kind='bar', figsize=(20, 10), stacked=True) # stacked=True 옵션으로 막대그래프 쌓기
ax1.set_ylim(0, 500)
ax1.set_xlabel("연도", fontsize=15)
ax1.set_ylabel("발전량 (억㎾h)")

plt.title("북한 전력 발전량 (1990 ~ 2016)", size=30)
ax1.legend(loc='upper left')
# ax2: 선 그래프
ax2 = ax1.twinx() # twinx는 x-axis는 공유하고 y-axis는 따로 표현하고자 할 때 => y축 지정 필요
ax2.plot(df.index, df.증감율_ver2, ls='-', marker='o', markersize=20, color='green' ) # default는 line그래프, x축은 df.index로 연도값, y축은 증감율
plt.ylabel("전년 대비 증감율(%)")
ax2.set_ylim(-50, 50)
# ls: line style '--'는 점선
plt.show()



## 교수님 풀이는??
# list_shift = []
# list_shift.append(np.nan)
# for i in range(len(df["합계"])-1):
#     list_shift.append(df.iloc[i, ]) # ????
# print(list_shift)


# plt.style.use("ggplot")
# # 막대그래프 stack, 선 그래프를 겹쳐서 그리기
# # 수력하고 화력만 가져오자
# ax1 = df[["수력", "화력"]].plot(kind='bar', figsize=(20, 10), stacked=True) # stacked=True 옵션으로 막대그래프 쌓기
# ax1.set_ylim(0, 500)
# ax1.set_xlabel("연도", fontsize=15)
# ax1.set_ylabel("발전량 (억㎾h)")
#
# plt.title("북한 전력 발전량 (1990 ~ 2016)", size=30)
# ax1.legend(loc='upper left')
# # ax2: 선 그래프
# ax2 = ax1.twinx() # twinx는 x-axis는 공유하고 y-axis는 따로 표현하고자 할 때 => y축 지정 필요
# ax2.plot(df.index, df.증감율, ls='-', marker='o', markersize=20, color='green' ) # default는 line그래프, x축은 df.index로 연도값, y축은 증감율
# plt.ylabel("전년 대비 증감율(%)")
# ax2.set_ylim(-50, 50)
# # ls: line style '--'는 점선
# plt.show()
