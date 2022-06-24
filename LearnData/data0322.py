import pandas as pd
# as : alias name 약자 (pandas.DataFrame.. 사용을 해야하는데 alias name을 쓰게 되면 pd.DataFrame 이런식으로 가능)
# 참고로 numpy는 np로 많이 사용
# import numpy as np

# # pandas의 Series는 Dictionary 타입을 인자로 가짐 (리스트도 되긴 하지만...)
# # dictionary type 의 정의
# dict_data = {'a':1, 'b':2, 'c':3}
#
# sr_dict = pd.Series(dict_data)
# print(sr_dict)
# print(type(sr_dict))
# print('\n')
#
# # 리스트를 인자로 넣어보자!!
# list_data = ['2022-03-22', 3.1415926535, 'ABC', 100, True]
# sr_list = pd.Series(list_data)
# print(sr_list)
# print(type(sr_list))
#
# idx = sr_list.index # rangeIndex(start, end, step) 인덱스 확인: RangeIndex(start=0, stop=5, step=1) 즉 0 1 2 3 4
# val = sr_list.values # value 확인하기
# print(idx, val)

# print("\n===================튜플-> 시리즈===================\n")
# # 튜플 자료형을 판다스의 시리즈로 변환
# # index라는 예약어, 지정어를 통하여 index도 지정
# tup_data = ('이근혁', '19xx-xx-xx', '남', True)
# sr = pd.Series(tup_data, index=["이름", "생년월일", "성별", "학생여부"])
# print(sr)
#
#
# print("\n===================시리즈 원소선택===================\n")
# # 시리즈의 원소를 선택 (1개)
# print(sr[0], sr["생년월일"])
# # 여러개의 원소를 선택 [[,]] 콤마로구분
# print(sr[[0, 1]])
# print(sr[['생년월일', '성별']])
# # slicing으로 여러개의 원소를 선택 [] 한 개(대괄호 한개)
# print(sr[0:2]) # 0:2 ==> 0,1(last index -1 번째까지)
# print(sr["이름":"성별"]) # last index -1 이 아니고, 이름~성별까지!!

# # 튜플을 시리즈로 변환(index 옵션에 index name 지정)
# tup_data = ("이근혁", "19xx-xx-xx", "남", True)
# sr = pd.Series(tup_data, index=["이름","생년월일","성별","학생여부"])
# print(sr)
# print(type(sr)) # 결과 <class 'pandas.core.series.Series'>
# print('\n')
#
# # 원소를 1개 선택
# print(sr[0]) # 이근혁 - 정수형 인덱스
# print(sr["이름"]) # 이근혁 - index name
# print('\n')
#
# # 여러 개의 원소를 선택 (인덱스 리스트 활용)
# print(sr[[1, 2]]) # 19xx-xx-xx, 남 => 시리즈형태로 반환되는 구나
# print('\n')
# print(sr[["생년월일", "성별"]]) #위와 같음
# print('\n')
#
# # 여러 개의 원소를 선택(인덱스 범위 지정, 1~1: 따라서 하나만)
# print(sr[1:2]) # 슬라이싱 sr[1]만 나오겠당, 근데 인덱스로 원소 하나 선택한 거랑 다르게 index name과 value 값이 같이 나와
# print('\n')
# print(sr["생년월일":"성별"]) # 어? 이거는 그럼 성별 앞까지인가 ==> 놉!! 명시적이라 생년월일, 성별 둘다 나옴


print("\n======================데이터프레임============================\n")
# Dictionary to DataFrame
dict_data = {
    'c0' : [1,2,3],
    'c1' : [4,5,6],
    'c2' : [7,8,9]
}
df_dict = pd.DataFrame(dict_data)
print(df_dict)

# List to DataFrame, index, columns 라는 파라미터에 row, column이름 정해주기
df_list = pd.DataFrame([[23, '남', '대구'],[24, '여', '부산']],
                       index=['이근혁', '최윤정'], columns=['나이', '성별', '지역'])
print(df_list)
print(df_list.index, df_list.columns)

# index, column 이름 변경
df_list.index = ['학생1', '학생2']
print(df_list)
df_list.columns = ['Age', 'Sex', 'Home']
print(df_list)
# rename 함수 사용
df_cpy = df_list.rename(index={'학생1':'김근형', '학생2':'정경임'})
print(df_cpy)
df_cpy.rename(columns={'Home':'고향'}, inplace=True) # 원본객체 변경
print(df_cpy)

