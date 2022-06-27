import pandas as pd

# pandas 연습 1
# dict_data = {'a' : 1, 'b' : 2, 'c' : 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환
# 딕셔너리와 시리즈의 구조가 비슷하기 때문에 딕셔너리를 시리즈로 변환하는 법을 많이 사용
# sr = pd.Series(dict_data)
# print(sr)
# print(type(sr))

# list_data = ["2022-06-26", 3.141592, 'ABC', 100, True]
# sr1 = pd.Series(list_data)
# print(sr1)

# idx = sr1.index
# val = sr1.values
# print(idx, val)

# print("\n======================== 튜플 --> 시리즈 ==========================")
# tup_data = ("최비결", "1991-02-05", "여", True)
# sr3 = pd.Series(tup_data, index=["이름", "생년월일", "성별", "학생여부"])
# print(sr3)
#
# print("\n======================== 시리즈 원소 선택 ==========================")
# # 시리즈 원소 선택하기
# print(sr3[0])
# print(sr3["생년월일"])
# print()
# print(sr3[["성별", "학생여부"]])
# print(sr3[2:])
# print(sr3["생년월일":"성별"])
#
# print("\n======================== 데이터프레임 ==========================")
# dict_data = {
#     'c0' : [1, 2, 3],
#     'c1' : [4, 5, 6],
#     'c2' : [7, 8, 9]
# }
# df_dict = pd.DataFrame(dict_data)
# print(df_dict)
# df_dict2 = pd.DataFrame(dict_data, index=["1행", "2행", "3행"])
# # df_dict3 = pd.DataFrame(dict_data, index=["1행", "2행", "3행"], columns=["1열", "2열", "3열"])
# #   위와 같이 하면 data가 들어가지 않음
# # df_dict3 = pd.DataFrame(dict_data, index=["1행", "2행", "3행"], columns={"c0":"1열", "c1":"2열", "c2":"3열"})
# #  위와 같이하면 column 명이 바뀌지 않음
# print(df_dict2)
# # print(df_dict3)
#
# # col 명 바꾸기
# df_dict3 = df_dict2.rename(columns={"c0":"1열", "c1":"2열", "c2":"3열"})
# print(df_dict3)
# # 아니면 .index, .columns 로 변경하면 됨
# cat_df = pd.DataFrame({
#     "쁨이" : [3, "여", "삼색이"],
#     "치즈" : [5, "남", "치즈"]
# })
# cat_df.index = ["나이", "성별", "색깔"]
# print(cat_df)
# cat_df2 = cat_df.transpose()
# print(cat_df2)
#
# cat_df1 = cat_df.drop("치즈", axis=1) # 열 삭제는 1, 행 삭제는 0
# cat_df1 = cat_df1.drop("나이")
# print(cat_df1)


# pandas 연습 2

exam_data = {
    "Name" : ["노영하", "김근형", "정경임"],
    "AI 기초" : [90, 90, 95],
    "자료구조" : [80, 90, 95],
    "영어" : [70, 60, 75],
    "웹프로그래밍" : [80, 90, 70]
}

exam_df = pd.DataFrame(exam_data)
print(exam_df)

dataStruct = exam_df["자료구조"]
print(dataStruct, type(dataStruct))
dataStructDf = exam_df[["자료구조"]]
print(dataStructDf, type(dataStructDf))

aiWeb = exam_df[["AI 기초", "웹프로그래밍"]]
print(aiWeb)
print(type(aiWeb))

# set_index : 특정 열을 새로운 index로 사용
exam_df.set_index("Name", inplace=True)
print(exam_df)
# 새로운 열추가
exam_df["ML"] = [90, 100, 95]
print(exam_df)
# 새로운 행추가
exam_df.loc["이시영"] = [100, 95, 100, 60, 90]
print(exam_df)
exam_df.loc[1] = 0
# exam_df.iloc[1] = 0 # 위와 천지차이
print(exam_df)

exam_df.iloc[0, :2] = 50
print(exam_df)

print("===============================================================")

dict_data = {
    'c0' : [1, 2, 3],
    'c1' : [5, 4, 6],
    'c2' : [7, 8, 9]
}

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index, fill_value=0)
print(ndf)

# 정렬 - 행 기준 .sort_index
ndf1 = ndf.sort_index(ascending=False)
print(ndf1)
# 정렬 - 열 기준 .sort_values : by 이용해서 기준 컬럼 지정
ndf2 = ndf.sort_values(by="c1", ascending=False)
print(ndf2)
ndf3 = ndf2.sort_values(by="c1", ascending=True)
print(ndf3)
