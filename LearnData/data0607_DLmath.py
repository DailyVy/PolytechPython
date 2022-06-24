import pandas as pd
import numpy as np
import seaborn as sns # dataset load 용도

# titanic 데이터 셋
titanic = sns.load_dataset("titanic")
# age, fare 2개 열로 dataframe 만들기
df = titanic.loc[:, ['age', 'fare']] # 모든 행과 'age', 'fare' 열
# 실습을 하기 위해 ten이라는 열을 만듭시다.
df['ten'] = 10
print(df.head())

# 하고자 하는 것은 함수매핑
# 특정 원소, 시리즈에 사용자 함수를 매핑
# 10을 더하는 사용자 함수 정의/구현
def add_10(n):
    return n + 10

# 두 객체의 합을 구하는 함수
def add_two_obj(a, b):
    return a + b

# 1) 개별 원소에 함수 매핑
# 1-1) 시리즈 원소에 함수를 매핑 : 시리즈객체.apply(매핑 함수(사용자 함수 명))
sr1 = df["age"].apply(add_10)
print(sr1.head())
sr_add10 = df["age"] + 10
print(sr_add10.head())

# 시리즈 객체와 숫자를 이용해서 add_two_obj 사용자 함수 적용
sr2 = df["age"].apply(add_two_obj, b=10)
print(sr2.head())
# ==> sr1, sr_add10, sr2 결과 다 똑같다.

# 함수를 간단하게 표현하는 람다도 활용 가능
print("========================람다 사용===========================")
sr3 = df["age"].apply(lambda x: add_10(x)) # x = df["age]가 매핑이 되어서 들어갈거임
print(sr3.head())

# 1-2) DataFrame에서 함수를 매핑하기 위해서는 df.applymap()
df_map = df.applymap(add_10)
print(df.head())
print(df_map.head())

# 2) 시리즈 객체에 함수 매핑
# null 여부 체크 사용자 함수
def missing_Value(series):
    return series.isnull()

result = df.apply(missing_Value, axis=0) # 행방향 : 함수 적용은 열
result2 = df.apply(missing_Value, axis=1)
print(result.head(20)) # 데이터프레임 반환
print(result.head(20))

# 시리즈가 입력되어서 하나의 값으로 출력하는 함수 작성
# 최대값-최소값을 반환하는 사용자 함수
def min_max(x):
    return x.max() - x.min()

# 최종적으로는 DataFrame이 입력이 되지만 출력은 시리즈임
result = df.apply(min_max)
print(result)
print(type(result)) # <class 'pandas.core.series.Series'> ==> 시리즈 반환

# concat(concatenate), merge 실습
# 데이터는 슬라이드 5페이지
df1 = pd.DataFrame(
    {
        "A" : ['a0', 'a1', 'a2'],
        "B" : ['b0', 'b1', 'b2'],
        "C" : ['c0', 'c1', 'c2']
    },
    index = [0, 1, 2]
)
df2 = pd.DataFrame(
    {
        "A" : ['0a', 'a1'],
        "B" : ['0b', 'b1'],
        "D" : ['0d', 'd1']
    },
    index = [0, 1]
)
print("df1, df2")
print(df1)
print(df2)

print()
print("=================concat================")
# 1. concat
#  2개의 데이터프레임을 단순히 연결
result_concat1 = pd.concat([df1, df2]) # 기존 인덱스 유지
result_concat2 = pd.concat([df1, df2], ignore_index=True) # ignore_index 가 True이면 새로 인덱스를 0부터 부여
print(result_concat1) # 인덱스가 0 1 2 0 1
print(result_concat2) # 인덱스가 0 1 2 3 4
# axis = 0:default, axis = 1도 해보기
result_concat1_axis1 = pd.concat([df1, df2], axis=1)
print(result_concat1_axis1)
result_concat2_axis1 = pd.concat([df1, df2], axis=1, ignore_index=True)
print(result_concat2_axis1)

print()
print("====================merge=================")
# 2. merge [default how='inner', on = None]
#  on = None은 중복되는 컬럼을 모두 merge
#  df1, df2가 기준이면 'on=None' == 'on=[A, B]' ==> A, B를 기준으로 merge를 하겠다.
merge1 = pd.merge(df1, df2)
print(merge1)
merge2 = pd.merge(df1, df2, how='outer', on='A')
print(merge2)
merge3 = pd.merge(df1, df2, how='outer', on=['A','B'])
print(merge3)
merge4 = pd.merge(df1, df2, how='inner', on=['A','B'])
print(merge4)
merge5 = pd.merge(df1, df2, how='inner', on='A')
print(merge5)


print()
##################################################################
# stock price.xlsx, stock valuation.xlsx 로 실습합시다.

df1 = pd.read_excel('stock price.xlsx')
df2 = pd.read_excel('stock valuation.xlsx')

# 같은 컬럼은 id밖에 없다.
# on=None(on='id')
# 중복되는 것만 추출
# default 가 inner, on=None
merge_inner = pd.merge(df1, df2)
print(merge_inner)

merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer)

# Left Join 하나만
# DB: select * from df1 left outer join df2 on df1.stock_name = df2.name

merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
merge_inner = pd.merge(df1, df2, how='inner', left_on='stock_name', right_on='name')
merge_outer = pd.merge(df1, df2, how='outer', left_on='stock_name', right_on='name')
# 이것도 inner로 찍어보고 outer로 찍어봅시다.
print(merge_left)
print(merge_inner)
print(merge_outer)