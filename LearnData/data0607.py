######################### 2교시 ##############################

import pandas as pd
import numpy as np

df = pd.read_csv("auto-mpg.csv", header=None) # 컬럼명 X

# 열 이름 지정
df.columns = ["mpg", "cylinders", "displacement", "horsepower", "weight",
              "acceleration", "model_year", "origin", "name"]

# 모든 열을 표시하기 위해서 set_option
pd.set_option("display.max_column", None)

print(df.head())

# 데이터 표준화
# 1. 익숙한 단위로 사용하자 (단위 환산)
#  mpg(mile per gallon) ==> kpl(km per litre)
#  1 mile : 1.690934 km, l gallon : 3.78541 litre (in America)
#  mpg to kpl = 1.690934 / 3.78541 ==> about 0.425
mpg_to_kpl = 1.690934 / 3.78541 # or about 0.425
df["kpl"] = df["mpg"] * mpg_to_kpl
print(df.head())

# 2. 자료형 변환 ==> 범주형 데이터 처리
#  컬럼의 속성을 분석해서 자료형을 변환(변경)
print(df.info()) # horsepower의 "?"는 dataFrame 변환 시 string으로 변환 ==> object
df["horsepower"].replace('?', np.nan, inplace=True) # ? => NaN 값으로 변환
df.dropna(subset=["horsepower"], axis=0, inplace=True) # NaN을 제거, row단위로 지울거고, 원본에 바로 적용

df["horsepower"] = df["horsepower"].astype("float") # 문자열을 실수형으로
print(df["horsepower"].dtype) # 해당 컬럼의 타입을 알아봅시다.
print(df.info()) # 398 non-null 에서 392 non-null이 되었고 horespower가 float로 변했음을 확인

# 3. 범주형 데이터 처리
#  1) numpy histogram을 이용해서 binning을 하고(bin갯수에 따라 자료를 나눠줌:binning)
#  2) pandas cut 함수를 이용하여 범주형 데이터로 변환
# horsepower를 (low, norm, high)로 변경
count, bin_divider = np.histogram(df["horsepower"], bins=3)
print(count, bin_divider)

# 범주형 데이터 변환하기 위해 cut 메서드 사용(bin이름을 지정)
bin_name = ["low", "norm", "high"] # bin 이름은 리스트로

df["horsepower_bin"] = pd.cut(x=df["horsepower"], # 적용할 데이터 배열 (리스트)
                          bins=bin_divider, # 경계값 리스트
                          labels = bin_name, # bin 이름
                          include_lowest=True) # 첫 경계값 포함
# 15행 정도 찍어보자
print(df[["horsepower", "horsepower_bin"]].head(15))

# 'low', 'norm', 'high' ==> [0, 1, 2] ==> one-hot encoding 방식 사용
# pandas에서는 one-hot encoding : dummies메서드 사용
hp_dummies = pd.get_dummies(df["horsepower_bin"])
print(hp_dummies.head(15))

# 4. 정규화
# 컬럼별 데이터의 범위가 차이가 많이 나면 학습에 영향을 미칠 수 있음
# 각 컬럼의 데이터들을 해당 컬럼의 최댓값으로 나누는 방법
# 정규화하기 전에는 필요에 따라 이상치 제거를 해주면 좋다.
#  1) 한 번 해보세요. (col/col.max)
#  2) [-6, -2, 2, 1, 3, 4] ==> -1 ~ 1사이로 한 번 변경해보세요.
#   2) 의 경우 max값(4)으로 나누면 안될거.... ==> -6의 크기가 제일 크니까 6으로 나누기..? 2-1)
#     아니면 min이 -6이고 max가 4니까 이 둘의 차이인 10으로 전부 나누기? 2-2)

# 2) 다음 리스트를 -1 ~ 1 값으로 바꿔보자(정규화)
test = [-6, -2, 2, 1, 3, 4]

# 2-1) 절대값이 제일 큰 걸로 나누기
test_abs = list(map(lambda x: abs(x), test)) # [abs(x) for x in test]
print(test_abs) # [6, 2, 2, 1, 3, 4]
print(max(test_abs)) #
test_abs_norm = list(map(lambda x: x / max(test_abs), test))
print(test_abs_norm)

# 2-2) min과 max의 차이로 나누기
divider = max(test) - min(test)
print(divider)
test_minMax_norm = list(map(lambda x: x / divider, test))
print(test_minMax_norm)


### 교수님 solution
# 리스트에서 절댓값을 취한 것중에 제일 큰 값으로 나누면 될 것 같은데
# normalize_data = [data / max([abs(val) for val in values]) for data in values]

### 데이터프레임 값을 정규화하자
# print(df.head())
# print(df["mpg"].max())

df_1 = df.drop(columns=["name", "horsepower_bin"], axis=1)
print(df_1.max())
df_1 = df_1 / df_1.max()
print(df_1.head())
df_1["name"] = df["name"]
df_1["horsepower_bin"] = df["horsepower_bin"]
print(df_1.head())

######################### 3교시 ##############################

