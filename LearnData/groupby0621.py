# Titanic
import pandas as pd
import numpy as np
import seaborn as sns # dataset load 용도
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)

titanic = sns.load_dataset("titanic")
# print(titanic.info)

# 모든 행과 5개의 열을 가지고 와서 dataframe 생성
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
# df["count"] = 1
print(f'승객 수 : {len(df)}')
print(df.head())

print("========================groupby==========================")
# groupby 실습 (SQL, DB 시간에 다룬 내용)
# class별로 그룹을 한 번 지어봅시다.
# class 열을 기반으로 group 객체 생성
grouped = df.groupby(["class"])
print(grouped.head())
print(grouped.sum()) # 나이의 경우는 sum이 의미가 없음

print("========================================================")
# 그룹 객체를 iteration을 돌면서 출력
# 그룹 객체(grouped) : key [first, second, third]
for key, group in grouped:
    print('* key: ', key)
    print('* number: ', len(group))
    print(group.head())
    print()
# 이런식으로 데이터를 볼 때 group을 활용하면 직관적으로 볼 수 있다.


print("========================연산=============================")
# 연산 메서드 적용
# 연산 메서드 사용시에는 연산이 가능한 열에 대해서만 선택적으로 연산을 수행
# 문자열을 포함한 sex, class 열은 제외하고 숫자형 데이터에 대해서만 평균을 구해보자
# 숫자형 데이터에 대해서만 평균을 구해보자
average = grouped.mean()
print(average) # 이거보니까 first class(0.63) 사람들의 survived가 third class(0.24)에 비해 높았네
# 결과 : 1등석의 경우 평균나이가 제일 많고, 구조확률이 약 63%로 제일 높음

print("===================개별 그룹 선택========================")
# 개별 그룹 선택(first or second class 선택 등)
group3 = grouped.get_group("Third") # class가 Third인 것만 가지고 옴
print(group3.head())

print("===================그룹을 sex, class로 나누어보자==================")
grouped_two = df.groupby(["class", "sex"]) # 먼저 class로 나누고 그다음 male, female로 나뉨

# for key, group in grouped_two:
#     print(" ** key : ", key)
#     print(" ** number : ", len(group))
#     print(group.head())
#     print()

# grouped_two 라는 객체에 대해서 연산 메서드를 적용
average_two = grouped_two.mean()
print(average_two)
# multi index (class, sex)
"""
여성의 구조확률이 남성에 비해 확연히 높다. 
특히 first, second 클래스의 female은 대부분이 구조되었고
남성의 경우 first class 의 남성이 다른 두 class보다 생존률이 보다 높다.

                     age        fare  survived
class  sex                                    
First  female  34.611765  106.125798  0.968085
       male    41.281386   67.226127  0.368852
Second female  28.722973   21.970121  0.921053
       male    30.740707   19.741782  0.157407
Third  female  21.750000   16.118810  0.500000
       male    26.507589   12.661633  0.135447
"""
# todo. 이거 그래프로 나타내봅시다 :)

# average_two["survived"].plot(kind="bar", figsize=(10, 8))
# plt.title("Survived rate according to Class and Sex")
# plt.show()


print("===========================개별 그룹 선택하기 (튜플형태로 입력)========================")
# 개별 그룹 선택 (first or second class 선택 등등)
# 멀티인덱스 형태로 되어있는 그룹에서 개별 그룹을 가지고 오고 싶을 때
# 튜플 형태로 컬럼을 지정하면 된다. (First group, Second group, Third group, ... )
#  e.g.  3등석의 여성의 데이터를 가지고 오고 싶을 때 : ('Third', 'female')
group3f = grouped_two.get_group(('Third', 'female'))
print(group3f.head())

print("=====================filtering===========================")
# Filtering
# e.g. 나이 평균이 30보다 작은 그룹만을 filtering해서 df 로 반환
average = grouped.mean()
print(average)
print()
# 평균 나이가 30미만인 그룹(클래스)는 second, third 그룹
age_filter = grouped.filter(lambda x : x.age.mean() < 30)
print(age_filter) # qna. 이거.. filter된거 맞아..??? 아닌거 같은데..? index4를 보면 class third인데 age 35.0 이 나오고 있는데?
