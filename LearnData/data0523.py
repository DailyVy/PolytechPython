import pandas as pd
# seaborn 내의 타이타닉, 펭귄 데이터 셋을 로드하기 위해서
import seaborn as sns

# seaborn 내 데이터셋
print(sns.get_dataset_names())

# 실행시 column 컬럼 전체가 표현되도록 셋팅
pd.set_option("display.max_columns", None)

# # 타이타닉 데이터셋 로드
# df_titanic = sns.load_dataset('titanic')
# print(df_titanic.head())
# print()
# # NaN를 확인하는 방법 1. info()
# print(df_titanic.info())
# # deck 열이 굉장히 NaN이 많이 있는 것을 확인
# #  value_counts() ==> NaN이 몇 개 인지를 파악
# #  dropna=False, dropna="", dropna=0 (bool : False 의미)
# print(df_titanic['deck'].value_counts(dropna=False)) # NaN을 포함해서 그룹을 지어줌
# print(df_titanic['deck'].value_counts(dropna=True)) # NaN을 빼고 그룹을 지어줌
#
# # NaN를 확인하는 방법 2. isnull() ==> True, False로 나온다.
# #  True, False로 나오면 mask를 씌울 수 있겠찌
# print(df_titanic.head().isnull())
# # isnull().all(), isnull().any()
# #  all : 각각의 열의 데이터가 모두 null인지를 확인해서 True, False로 반환
# #  any : 열의 데이터 중에 하나라도 null인지를 확인
# print("=============================all()===================================")
# print(df_titanic.head().isnull().all())
# print("=============================any()===================================")
# print(df_titanic.head(50).isnull().any())
# # 데이터프레임에서 하나라도 null이 있으면 True를 반환하고 싶을 경우
# print(df_titanic.isnull().any()) # 열 기준으로 하나라도 null 인게 있으면 true로 반환
# print("==============================any().any()===============================")
# print(df_titanic.isnull().any().any()) # True : isnull().any()중에 하나라도 True 이면 True를 반환하는 것
# print("======================================================================")
#
# # 각 열에서 NaN인 데이터의 갯수를 반환
# # sum() 대신에 count도 사용 가능, 하지만 sum을 많이 사용하는 편
# #  sum(axis 옵션), isnull 자체가 column 기준으로 계산하는 메서드
# #  axis=0 : column, axis=1 : row (일반적으로는 axis=0이 row고 axis=1이 col인데..)
# #  해당 모듈, 특정한 모듈이 컬럼 단위로 계산하는 모듈이면 axis=0 : col .. ?
# print(df_titanic.isnull().sum()) # df_titanic.isnull().sum(axis=0)
# print(df_titanic.isnull().sum(axis=1)) # 0번째 행에서 NaN이 1개 존재 .. ~ 890번째 행에서 NaN 1개 존재
# # count : 열의 갯수를 counting. 옵션에 dropna 같은 내용이 없음
# #  count() 자체는 NaN을 배제하고 카운팅
# #  isnull.sum() 을 몰라도 시리즈 연산을 하면 각 열의 NaN 갯수 확인 가능
# #  시리즈 연산 : 숫자 (+, -, *) 시리즈, 시리즈 + 10
# print(df_titanic.count())
# print(len(df_titanic) - df_titanic.count())
# print("======================================================================")
#
# # NaN 확인하는 방법은 여러가지가 있는 것을 확인
#
# # 여러분이 학습시킨다고하면 Deck 열은 사용하는 게 좋을까요?
# #  Deck 열은 NaN이 688개 정도 되기 때문에 80% 정도가 NaN
# #  유추하는게 오히려 성능에 악영향을 미칠 수 있으므로 해당 컬럼은 삭제
# # drop
# print(df_titanic.head())
# df_drop = df_titanic.drop(columns=['deck'])
# print("======df_thresh====")
# # NaN이 몇 개 이상인 열을 삭제하고 싶을 때 (X)
# # NaN이 아닌 값이 최소 몇 개 이상 나와야 된다는 것(그보다 적게 나오면 drop) (O)
# #  dropna(axis=1, thresh=몇개)
# #  thresh 는 NaN 이 몇 개 있는 기준이 아니라 유효한 데이터 갯수의 기준이다
# #  thresh = 500을 주면 500미만 입력된 값들은 날아감
# df_thresh = df_titanic.dropna(axis=1, thresh=200) # col을 날릴거니까 axis=1
# # print(df_drop.head())
# print(df_thresh.head())
#
# ## 2022-05-24 오후 수업 : 인공지능 개론 대신..
# # age열에 NaN가 있는 행을 삭제
# #  특정한 열을 가져오고 싶을 때 subset이라는 옵션을 사용할 수 있다.
# #  행을 지울거니까 axis=0
# #  how='any' 하나라도 NaN이 있으면 삭제하겠다.
# #  여기에서는 ['age'] 열이 하나라서 how에 any를 쓰든 all을 쓰든 같다.
# #  하지만 subset에 열이 두 개 들어간다면..?? how='all', how='any'와 달라진다.
# df_age = df_titanic.dropna(subset=['age'], axis=0, how='any')
# # df_age2 = df_titanic.dropna(subset=['age', 'deck'], axis=0, how='all') # age와 deck의 값이 둘 다 NaN일 때 행 삭제
# print(df_age, len(df_age))
#
# # age 열에 NaN일 경우, mean값을 채워 넣자
# # mean(axis옵션), 0: col, 1: row
# # 값을 채워 넣을 때, 경우에 따라서 학습 모델에 의해 추정된 값을 사용하기도 한다.
# mean_age = df_titanic['age'].mean()
# print(mean_age) # 29.6991176...
# # fillna 메서드 : NaN replace 어떤 값
# # df_fillna = df_titanic['age'].fillna(int(mean_age)) # 29로 채워짐
# # print(df_fillna)
# df_fillna = df_titanic['age'].fillna(mean_age) # 29.6991176으로 채워짐
# print(df_titanic.head(10), '\n' , df_fillna.head(10))
#
# # ffill, bfill (Forwarding, Backwarding)
# # embark_town 결측치 2개를 채워넣자
# df_ffill = df_titanic['embark_town'].fillna(method='ffill')
# df_bfill = df_titanic['embark_town'].fillna(method='bfill')
# # todo. 실제 정상적으로 값이 들어갔는지 확인합시다.

##### 펭귄 ######
df_pg = sns.load_dataset('penguins')
print(df_pg.info())

# 1. 결측치 데이터(NaN)처리
#  sex(성별) 는 11개의 데이터가 NaN, 성별의 경우 유추해서 정하기가 어려움 ==> 날리는 게 낫지뭐
#  결측치가 있는 데이터 추출?
print(df_pg.isnull().sum())
# NaN이 하나라도 포함되어 있는 데이터를 추출하고 싶은데, 행 기준임..!
#  isnull()은 default가 col이라서 행 방향은 axis=1
print(df_pg.isnull().any(axis=1))  # 결측치가 하나라도 있는 행에 대해서 True, False
# 마스크를 씌워서 True인 녀석만 가지고 오고 싶다..!
print(df_pg[df_pg.isnull().any(axis=1)])  # 원본 데이터 역할에 덮어쓰면 True인 녀석만 들고 온다.

# todo. 내가 한 거
# 3, 339번 인덱스와 성별 컬럼은 drop
print("=================3, 339번 인덱스와 성별 컬럼은 drop=================")
df_drop = df_pg.drop([3, 339])
df_drop = df_drop.drop(['sex'], axis=1)
print(df_drop.head())
print(df_drop.tail(10))

print("=================3, 339번 인덱스와 성별 컬럼은 drop 22222 =================")
df_ddrop = df_pg.dropna(subset=['sex', 'bill_length_mm'], axis=0, how='all')
df_ddrop = df_ddrop.drop(['sex'], axis=1)
print(df_ddrop.head())
print(df_ddrop.tail(10))

# df_pgdrop = df_pg.dropna(subset=['sex'], axis=0) # how에 any를 주든.. all을 주든...
# print(df_pgdrop.head(10))

print("=================prof. ver. 3, 339번 인덱스와 성별 컬럼은 drop=================")
# 한번에 하려면..? todo. 혼자해보세영
# df_pg_nan = df_pg.drop(index=df_pg.isnull().index, columns=['sex']) # ..안돼요... 왜...?
# df_pg_nan = df_pg.drop(index=[3, 339] , columns=['sex']) #
df_pg_nan = df_pg.drop(index=df_pg[df_pg["bill_length_mm"].isnull()].index, columns=['sex'])

# 두번 나눠서...
df_pg.drop('sex', axis=1, inplace=True)
df_pg.dropna(subset=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'], how='all', inplace=True)
print(df_pg.head())

print()
print("======================중복 데이터 처리=======================")

# 2. 중복 데이터 처리
#  중복 데이터를 확인 duplicated() : 같은게 있으면 True, 없으면 False
#  기본적으로는 중복 데이터 삭제
print(df_pg.duplicated())  # 중복되는 데이터가 없는 것 처럼 보임

# 고의로 중복데이터를 넣어서 삭제하는 연습을 해봅시다.
# 중량이 제일 많이 나가는 데이터와 동일한 데이터를 추가해보자
print(df_pg['body_mass_g'].max(), df_pg.tail(2))  # max는 6300g, 제일 마지막 인덱스는 343번 ==> 344에 데이터를 추가하자
print("====마스킹=====")
print(df_pg[df_pg['body_mass_g'] == df_pg['body_mass_g'].max()])  # 중량 최대치인 값을 가진 행을 보여줌
# 344번째에 똑같은 걸 저장하자
df_pg.loc[344] = ['Gentoo', 'Biscoe', 49.2, 15.2, 221.0, 6300.0]
print(df_pg.tail())
# 다시 중복 데이터 확인
print(df_pg.duplicated())  # 344행에 True가 떴다.

# 중복데이터는 삭제해주세요.
# drop_duplicates()
df_pg.drop_duplicates(inplace=True)
print(df_pg)

######
dict_data = {
    'c0': ['a', 'a', 'b', 'a', 'b', 'a'],
    'c1': [1, 1, 1, 2, 2, 1],
    'c2': [1, 1, 2, 2, 2, 1],
}
df_dict = pd.DataFrame(dict_data)
print(df_dict)
print(df_dict.duplicated())

# 3. 이상치 데이터 처리
# 정규 분포를 따른 다는 가정하에 3시그마에 해당하는 부분은 날리는 게 좋습니다.
#  z-score 를 사용
#  z-score 함수 작성 : (데이터-평균)/표준편차
#  np.mean(), np.std() : 평균, 표준편차
import numpy as np

# z-score가 -2이하, 2이상되는 데이터(DataFrame)을 반환하는 함수
#  parameter로 데이터프레임과 컬럼(이 컬럼을 기준으로 이상치를 찾아), z-threshold
#  (x-μ)/std
# outlier(df_pg, 'body_mass_g', 2)
def outlier(df, col, z_threshold):
    # df[col] : x (e.g. df['body_mass_g'])
    zscore = abs((df[col] - np.mean(df[col])) / np.std(df[col])) # ±2 대신 2로 판단하기 위해 절댓값
    return df[zscore > z_threshold].index # true에 해당되는 것의 index값을 반환

# 이거 쓰면 z-score 2 이내의 값만 가지고 올 수 있다.
def inlier(df, col, z_threshold):
    # df[col] : x (e.g. df['body_mass_g'])
    zscore = abs((df[col] - np.mean(df[col])) / np.std(df[col])) # ±2 대신 2로 판단하기 위해 절댓값
    return df[zscore <= z_threshold].index # true에 해당되는 것의 index값을 반환


# z-score가 ±2 이상인 데이터를 뽑아봅시다.
# outlier는 결국 index를 반환하니까 df_pg.loc[outlier()]는 해당되는 녀석의 데이터프레임을 가지고 오는 것
print(df_pg.loc[outlier(df_pg, 'body_mass_g', 2)])
print(df_pg.loc[inlier(df_pg, 'body_mass_g', 2)]) # 333개의 행