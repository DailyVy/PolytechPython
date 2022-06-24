import pandas as pd

# header = 0(default), 첫번째 행을 컬럼명으로 쓰겠다~
# header = None, 첫번째 행을 컬럼명으로 불러오지 않겠다! ==> 정수형 인덱스가 자동적으로 할당
df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# 데이터프레임 df의 내용을 일부 확인
# print(df.head())
# print()
# print(df.tail())

# # 출력 옵션 조절
# # 모든 열을 출력
pd.set_option('display.max_columns', None)
# # 모든 행 출력
# pd.set_option("display.max_rows", None)
# # 행 출력 개수를 조절
# pd.options.display.max_rows = 60

# # df의 모양과 형태를 알기 위해. (크기) ==> tuple 형식으로 반환(398, 9)
# print(df.shape)
# print(df.info())
# print(df.describe(include='all')) # 산술데이터 + 비 산술데이터
# print(df.describe(include=['object'])) # 비 산술데이터만~
# print()
# # 모든 열이 각각 몇 개인지 확인할 때 : df.count() ==> dropna 옵션 없음
# print(df.count())

# # DF에서 특정 열이 가지고 있는 고유 값이 각각 몇 개 인지 확인
# # NaN은 카운트를 하기 싫을 때, dropna = True
# unique_value = df['origin'].value_counts()
# unique_value = df['origin'].value_counts(dropna=True)
# print(unique_value, type(unique_value)) # Series
#
# # 평균값, 중앙값, 최대값, 최소값
# # 모든 열에 대해서 각각 평균 값을 보고 싶을 때
# # df.mean(), df.median(), df.max(), df.min()
# # mpg 컬럼에 대한 평균값
# print(df.mpg.mean(), df['mpg'].mean())
# # mpg, weight 컬럼에 대한 평균 값
# print()
# print(df[['mpg', 'weight']].mean()) # median은 각자 나중에 실습
# # 최대값/최소값(max/min()),
# # object type(string:문자열) : ASCII 변경해서 sorting 후 min/max 결과를 반환
# print()
# print(df[['mpg', 'weight']].max())
# print(df[['horsepower', 'name']].max())
# print(df['horsepower'].min(), df['horsepower'].max())
# # 모든 행 출력
# pd.set_option("display.max_rows", None)
# print(df['horsepower'])
# print(df.info())
#
# # 표준편차 (스스로 확인해보세요)
# print(df.describe())
# print()
# print(df['mpg'].std())
# print(df[['cylinders', 'displacement']].std())
# # 상관계수
# print()
# print(df.corr())
# print(df[['mpg', 'weight']].corr()) # 차가 무거우면 나가기 힘드니까 음의 상관관계~~~
# print()
# print(df['mpg'].corr(df.displacement, method='spearman')) # mpg, displacement의 스피어만 상관계수

# Data전처리, horsepower의 경우, '?'가 포함되어 있음 ==> 상관계수를 구할 수 없음
# 1. ? ==> NaN으로 변경(replace()메서드 사용)
# 어림짐작 해서 넣으면 데이터에 영향을 줄 수 있기 때문에 이 데이터는 날려야 합니다.
# 2. NaN의 데이터는 행단위로 삭제 (dropna())
# 3. type 자체를 float으로 변경 (astyoe('float'))
# 4. corr() 더 수행.

import numpy as np # (NaN)의 값으로 대체하기 위해 import
# 1. ? ==> NaN으로 변경(replace()메서드 사용)
df['horsepower'].replace('?', np.nan, inplace=True)
# df1 = df['horsepower'].replace('?', np.nan)
# 2. NaN의 데이터는 행단위로 삭제 (dropna())
df.dropna(axis=0, inplace=True)
# 3. type 자체를 float으로 변경 (astyoe('float'))
df['horsepower'] = df['horsepower'].astype('float') # 문자열을 실수형으로
print(df['horsepower'].dtype)
# 4. corr() 더 수행.
print(df.corr())

# horsepower 통계
print(df['horsepower'].min(), df['horsepower'].max(), df['horsepower'].median(), df['horsepower'].mean())