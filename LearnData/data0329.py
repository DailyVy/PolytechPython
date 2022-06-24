import pandas as pd

# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
# dictionary type의 exam_data 선언/value assign
exam_data = {
    "이름" : ["노영하", "김근형", "정경임"],
    "AI기초" : [ 90, 90, 95 ],
    "자료구조" : [90, 90, 95],
    "영어" : [90, 90, 95],
    "웹프로그래밍" : [90, 90, 95]
}
df = pd.DataFrame(exam_data)
print(df)

# '자료구조' 컬럼만 선택
dataStruct = df["자료구조"]
# dataStruct_2 = df.자료구조 # 위와 같다.
print(dataStruct)
# print(dataStruct_2)
print(type(dataStruct)) # Series로 나온다.

# 여러 개의 컬럼 데이터를 가지고 오고 싶음 ==> 반환되는 자료형은?
# DataFrame
# ai_web = df[ "AI기초", "웹프로그래밍" ] # Error! [] 대괄호 하나 안에서 콤마(,)로 구분하면 row, column으로 인식됨!!
# 그렇다고 실제 df[row, column] 넣으면 이것도 에러야
ai_web = df[[ "AI기초", "웹프로그래밍" ]]
print(ai_web)
print(type(ai_web)) # DataFrame

datastructure = df[["자료구조"]] # datastructure에 반환되는 타입은? ==> DataFrame
print(datastructure)
print(type(datastructure))


# reindex, set_index
# set_index : 특정 열을 새로운 index로 사용하겠다.
df.set_index("이름", inplace=True) # 원본 객체 수정
print(df)
# df1 = df.set_index("이름")
# print(df)
# print(df1)

# 데이터프레임 df의 특정 원소 1개 선택
point1 = df.loc["노영하", "영어",]
point2 = df.iloc[0, 2]
print(point1, point2)
print(type(point1))

# 특정 원소 2개 이상 선택 (노영하's 영어, 웹프로그래밍 점수)
c = df.loc["노영하", ["영어","웹프로그래밍"]]
d = df.iloc[0, [2,3]]
e = df.iloc[0, 2:]
print(c)
print(d)
print(e)

# df에서 2개 이상의 행과 열로부터 데이터를 가지고 와보자.
# 노영하, 김근형의 영어, 웹프로그래밍 점수
noh_kim = df.loc[["노영하","김근형"], "영어":"웹프로그래밍"]
noh_kim2 = df.loc["노영하":"김근형", ["영어","웹프로그래밍"]]
noh_kim3 = df.iloc[0:2, 2:]
noh_kim4 = df.iloc[[0,1], [2,3]]
print(noh_kim)
print(noh_kim2)
print(noh_kim3)
print(noh_kim4)
# 노영하, 정경임의 자료구조, 웹프로그래밍 점수
noh_jung = df.loc[["노영하", "정경임"], ["자료구조","웹프로그래밍"]]
noh_jung2 = df.iloc[[0,2],[1,3]]
print(noh_jung)
print(noh_jung2)
# 김근형, 정경임의 AI기초 ~ 영어
kim_jung = df.iloc[1:, :3]
kim_jung2 = df.iloc[[1,2],[0,1,2]]
kim_jung3 = df.loc[["김근형","정경임"],["AI기초","자료구조","영어"]]
kim_jung4 = df.loc["김근형":"정경임","AI기초":"영어"]
print(kim_jung)
print(kim_jung2)
print(kim_jung3)
print(kim_jung4)

print("\n")
# 새로운 열 추가 및 데이터 assign
print(df)
df["ML"] = [80, 100, 100]
print(df)
# 새로운 행 추가
# index가 3인 행을 추가하고 모든 컬럼의 값들은 0로 세팅
df.loc[3] = 0
df.loc[4] = [90, 90, 90, 90, 90]
print(df)

# 새로운 행 추가 시 기존 행을 복사
df.loc['이시영'] = df.loc[4]
print(df)

# 원소 값 변경
df1 = df.copy() # df 복사
# print(df1.iloc[0][0]) # 어 나오긴 하네?, 예전엔 이렇게 접근했다. 하지만 [ , ] 로 하세영
df1.iloc[0, [1,2,3]] = [100,100,100]
print(df1)
# 0, 1행, [1,2,3]열의 데이터를 변경
df1.iloc[[0,1],[1,2,3]] = [[90,90,90],[80,80,80]]
print(df1)
# 데이터 변경
print("\n")
df1.loc[[3][:2]] =[80,80,80,90,100] # :2인데 전체 행이 바뀌네??? loc이라 그런가??? 저 슬라이싱은 iloc이니까?
print(df1)
# df1.iloc[[3][:2]] =[10,20] # Error 발생 shape mismatch
df1.iloc[[3][:2]] =[10] # 원하는 모양이 다름 행 전체가 바뀜
print(df1)
df1.iloc[[3][:2]] =50 # 원하는 모양이 다름 행 전체가 바뀜
print(df1)
df1.iloc[3,:6] =[70,60,50,40,40]
print(df1)
# df1.loc["노영하", :2] = [0,10]

print("\n")
# Transpose
df2 = df.T
print(df2)

print("\n================reindex()=================\n")
# reindex()
dict_data = {
    'c0' : [1, 2, 3],
    'c1' : [5, 4, 6],
    'c2' : [7, 8, 9]
}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
# df = pd.DataFrame(dict_data)
print(df)
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index, fill_value=0)
print(ndf)

# 정렬 - 행기준
ndf = df.sort_index(ascending=False)
print(ndf)
# 정렬 - 열 기준 : by= 이용해서 기준 컬럼 지정
ndf = df.sort_values(by="c1", ascending=False)
print(ndf)