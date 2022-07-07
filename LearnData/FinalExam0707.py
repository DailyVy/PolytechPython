import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1, 2번 Pokemon.csv 파일 사용
# 1. Attack 컬럼의 값을 기준으로 내림차순 정렬했을 때,
# 상위 400위까지 포켓몬들과 401~800위까지 포켓몬들에서 전설포켓몬(Legendary컬럼)의 숫자 차이를 구하시오.

# 2. Type 1 컬럼의 속성이 Fire인 포켓몬들의 Attack의 평균이상인 Water속성의 포켓몬 수를 고르시오.

pokemon = pd.read_csv("./Data/Pokemon.csv")
# column 전체 봅시다.
pd.set_option("display.max_columns", None)
# print(pokemon.head())

poke_sort = pokemon.sort_values(by="Attack", ascending=False)
poke_sort = poke_sort.reset_index()

# print(poke_sort.head())

poke_sort_400 = poke_sort.iloc[:400, :]
poke_sort_800 = poke_sort.iloc[400:800, :]
# print(poke_sort_400.Legendary.value_counts()) # False 339, True 61
# print(poke_sort_800.Legendary.value_counts()) # False 396, True 4

# Legendary포켓몬의 숫자를 세기 위해 Name을 기준으로 셈
# print(poke_sort_400["Name"][poke_sort_400.Legendary == True].count()) # 61
# print(poke_sort_800["Name"][poke_sort_800.Legendary == True].count()) # 4

# 1번 답. 위 값의 차이
# print(poke_sort_400["Name"][poke_sort_400.Legendary == True].count()
#       - poke_sort_800["Name"][poke_sort_800.Legendary == True].count())

########################################################################################################

# 2번
pokegroup = pokemon.groupby("Type 1") # Type 1으로 그룹
pokeFire = pokegroup.get_group("Fire")
pokeWater = pokegroup.get_group("Water")
FAM = pokeFire.Attack.mean() # Fire 포켓몬들의 Attack 평균
# print(FAM)  # 84.769231...
# print(pokeWater)

# 2번 답
# print(len(pokeWater[pokeWater["Attack"] >= FAM])) # 37

########################################################################################################


# 3 ~ 9 번 bank.csv 파일 사용 : 데이터는 포르투갈 은행 기관의 직접 마케팅 캠페인(전화 통화)과 관련된 것
# 3. 마케팅 응답 고객들의 나이를 10살 단위로 변환했을 때, 가장 많은 인원을 가진 "나이대와 인원수"를 도출하시오.
#  (10살 단위 변환 예: (0~9:0, 10~19:10, 20~29:20))

bank = pd.read_csv("./Data/bank/bank.csv", sep=";")
# bankfull = pd.read_csv("./Data/bank/bank-full.csv", sep=";")
# print(bankfull.info())

# print(bank.head())
# print(bank.info())
# print(bank.isnull().sum()) # null 값 있는 컬럼 없음

# 10살 단위 변환 컬럼 추가
bank["age10"] = bank["age"] // 10
# print(bank.head())
# 3번 답. 가장 많은 인원을 가진 "나이대와 인원수"
# print(bank.age10.value_counts()) # 3, 1808

########################################################################################################

# 4. 나이가 25살 이상 29살 미만인 응답 고객들 중 housing 컬럼의 값이 yes인 고객의 수

# print(bank.head())
bank.drop(columns=["age10"], axis=1, inplace=True) # age10 컬럼 삭제

bank2529 = bank[(bank.age >= 25) & (bank.age < 29)]
# print(bank2529.head(30))

# 4번 답
bank2529yes = bank2529[bank2529["housing"] == "yes"]
# print(len(bank2529yes)) # 187

########################################################################################################

# 5. numeric한 값을 가지지 않은 컬럼들 중 unique한 값을 가장 많이 가지는 컬럼의 이름과
#  unique한 값의 개수는 몇 개인지를 구하시오.

# numeric한 값을 가지고 있지 않을 컬럼
# print(bank.info()) # job, marital, education, default, housing, loan, contact, month, poutcome, y
# print(bank.head(10))

bankNoNum = bank.drop(columns=["age", "balance", "day", "duration", "campaign", "pdays", "previous"], axis=1)
# print(bankNoNum.info())

# print(bankNoNum.columns) # column명

uniqueCount = 0
uniqueCol = ""

for col in bankNoNum.columns:
    # print(bankNoNum[col].unique())
    if uniqueCount < len(bankNoNum[col].unique()):
        uniqueCount = len(bankNoNum[col].unique())
        uniqueCol = col

# 5번 답
# print(uniqueCol, uniqueCount)

########################################################################################################

# 6. balance 컬럼값들의 평균값 이상을 가지는 데이터를 ID값을 기준으로 내림차순 정렬했을 때
# 상위 100개 데이터의 balance값의 평균은 얼마인가?

# print(bank.head())
# print(bank.info())
# print(bank["balance"].mean()) # 1422.6578....

# print(bank.head())

# balance 컬럼값들의 평균값이상 데이터
bankOverBalMean = bank[bank["balance"] > bank["balance"].mean()]
# print(bankOverBalMean.head())

# ID 기준으로 정렬하기 ==> ID의 행방은...???? index를 기준으로
bankOverBalMean = bankOverBalMean.sort_index(ascending=False)
bankOverBalMean100 = bankOverBalMean.iloc[:100, :]

# 6번 답.
# print(bankOverBalMean100.balance.mean())

########################################################################################################

# 7. 가장 많이 마케팅(전화)을 집행했던 날짜는 언제인가? (데이터 그대로 일(숫자), 달(영문)으로 표기)

bankGroup = bank.groupby(["day", "month"])

# print(bankGroup.head())

theDay = ""
maxCall = 0

for key, group in bankGroup:
    # print("**key : ", key)
    # print("**number : ", len(group))
    if maxCall <= len(group):
        maxCall = len(group)
        theDay = key
    # print()

# 7번 답
print(theDay, maxCall) # (15, 'may') 114

########################################################################################################

# 8번, 9번 답???
ageBalCorr = bank[["age", "balance"]].corr()
# print(ageBalCorr)
# sns.heatmap(ageBalCorr, cmap="RdBu_r", annot=True, fmt=".5f")
# plt.show()

########################################################################################################

# 10 ~ 12번 stroke.csv 파일 사용

# 10. 성별이 Male인 환자들의 age의 평균값(소수점 3자리까지, 반올림)을 구하시오.

stroke = pd.read_csv("./Data/healthcare-dataset-stroke-data.csv")

# print(stroke.head())
# print(stroke.info())
# print(stroke.isnull().sum()) # bmi 만 201개의 결측치 존재
# print()

strokeAgeAvg = stroke.groupby("gender").age.mean()

# print(strokeAgeAvg)
# 10번 답
# print(round(strokeAgeAvg["Male"], 3))

########################################################################################################

# 11. bmi 컬럼의 결측치를 bmi 컬럼의 결측치를 제외한 나머지 값들의 평균값으로 채웠을 경우 bmi 컬럼의 평균을 소숫점 이하 3자리까지 구하시오.

# print(stroke.head(10))

bmiAge = stroke["bmi"].mean()
# print(bmiAge)

# 결측치를 평균값으로 채움
stroke["bmi2"] = stroke["bmi"].fillna(bmiAge)
# print(stroke.head(10))

# bmi컬럼의 평균 구하기
# 11번 답
# print(round(stroke.bmi2.mean(), 3))


########################################################################################################

# 12. bmi컬럼의 각 결측치들을 결측치를 가진 환자 나이대(10단위)의 평균 bmi값으로 대체한 후
# 대체된 컬럼의 평균을 소숫점 이하 3자리(반올림)까지 구하시오.
#  (10살 단위 변환 예: (0~9:0, 10~19:10, 20~29:20))

# 대체 나이 컬럼은 age2
stroke["age2"] = stroke["age"] // 10

# print(stroke[["age","bmi"]].head(30))

# 나이로 그룹 묶어서 평균 구하려고..
strokeGroup = stroke.groupby("age2")

# 나이대 평균 bmi 구하기
fillVal = strokeGroup.bmi.mean()
# print(fillVal)
"""
age2
0.0    18.869935
1.0    24.906598
2.0    28.136920
3.0    31.205864
4.0    31.446099
5.0    31.750435
6.0    31.004068
7.0    29.378168
8.0    28.281319

그러니까 age2 가 6.0이면 31.004068가 입력되어있으면 되는거 아녀
"""

# print(stroke.bmi.head(30))

# 일단 이거 병합해야지...
newStroke = pd.merge(stroke, fillVal, how="left", left_on="age2", right_on="age2")

# 새로운 bmi_y는 나이대별 평균 bmi
# print(newStroke[["age2", "bmi_y"]].head(30))

# 근데 나는 bmi의 결측치만을 나이대별 평균 bmi로 채우고 싶어

stroke["bmi3"] = stroke["bmi"].fillna(newStroke["bmi_y"])
# print(stroke[["age2", "bmi3"]].head(30))

# print(stroke.head())

# 이제 우리가 원하는 대체된 bmi 컬럼 ==> bmi3 의 평균을 구합시다
# 12번 답
# print(round(stroke.bmi3.mean(), 3))