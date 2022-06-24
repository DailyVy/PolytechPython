# Homework 3월 말까지
# 1. 정수형, 실수형, 문자열 및 '리스트 내 리스트' 등을 포함하여 자신을 소개하는 리스트를 만들고,
# 리스트 인덱싱과 슬라이싱 기법 등을 이용하여 자기 소개하는 것 표현해보기
# 2. 문자열 변수에서 특정 인덱싱으로 접근 후 문자열을 변경할 수 있는가? 답변 및 가능한 방법 코드 작성 및 제출,
# mutable, immutable 자료형 정리해보기.
# 3. List에서 Append,insert, extend 차이점, remove/pop 차이점, 각각 예제 코드 작성 및 설명
# 4. 기존 파싱 코드에서 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기
# 5. 기존 파싱 코드에서 데이터를 어덯게 만들면 더욱 효율적으로 처리할 수 있는지
# - Data 형식 변경 및 추가, 코드 작성 결과 확인(조건은 동일함, 크기가 100보다 크면 vehicle에서 truck으로)


# 1.
print("\n=================================================================================================\n")
print("1. 정수형, 실수형, 문자열 및 '리스트 내 리스트' 등을 포함하여 자신을 소개하는 리스트를 만들고,\n"
      " 리스트 인덱싱과 슬라이싱 기법 등을 이용하여 자기 소개하는 것 표현해보기\n")
# 이름(문자열), 나이(정수), 고향(튜플), 전공(문자열), 가족관계(리스트),
# 고양이 이름 및 몸무게(딕셔너리-문자열,실수), 취미(리스트), 좋아하는 음식(세트)
choi_BG = ["최비결", 33, ("경상남도","창원"), "화학", ["어머니", "아버지", "동생", "고양이"],
           {"Cat": "쁨", "Weight": 4.5}, ["해외 여행", "서점 방문","음악 감상"],{"파스타", "떡볶이"}]

# 각 리스트 인덱스 확인
# index = 0
# for i in choi_BG:
#     print(f'{index} : {i}')
#     index += 1

print(f'제 이름은 {choi_BG[0]}이며, 나이는 {choi_BG[1]}입니다.\n'
      f'저는 {choi_BG[2][0]}의 {choi_BG[2][1]}에서 자랐으며, 전공은 {choi_BG[3]}입니다.\n'
      f'가족은 총 {len(choi_BG[4])}명이며, {choi_BG[4][0]}, {choi_BG[4][1]}, '
      f'{choi_BG[4][2]}은 현재 {choi_BG[2][1]}에 거주중입니다.\n'
      f'그리고 {choi_BG[4][-1]}가 있는데 이름은 \'{choi_BG[5]["Cat"]}\'입니다. '
      f'최근에 몸무게를 쟀을 때 {choi_BG[5]["Weight"]}kg 이었습니다.\n'
      f'저는 {choi_BG[6][0]}을 가는 것을 좋아하는데 꼭 그 나라의 {choi_BG[6][1][:3]}\b을 {choi_BG[6][1][3:]}하곤 합니다. \n'
      f'또한 {choi_BG[6][2]}도 즐깁니다.'
      f'좋아하는 음식은 {list(choi_BG[7])[0]}와 {list(choi_BG[7])[1]}입니다.')

# 2.
print("\n=================================================================================================\n")
print("2. 문자열 변수에서 특정 인덱싱으로 접근 후 문자열을 변경할 수 있는가?\n"
      "답변 및 가능한 방법 코드 작성 및 제출, mutable, immutable 자료형 정리해보기.\n")
print("문자열 변수에서 특정 인덱싱으로 접근하여 문자열 변경은 불가능하다! ==> 문자열은 immutable한 자료형\n")
address = "15 Gukchaebosang-ro 43-gil, Seo-gu, Daegu"
print("address = \"15 Gukchaebosang-ro 43-gil, Seo-gu, Daegu\"")
print("address[-5] 의 값은",address[-5]) # D
print('''address[-5] = \"B\" 을 입력하면 다음과 같은 TypeError가 발생한다.
TypeError: 'str' object does not support item assignment''')
# address[-5] = "B" # TypeError: 'str' object does not support item assignment 발생
print("\n따라서 문자열을 바꾸고 싶다면 조합 또는 replace로 다시 새로운 객체에 할당하는 방법이 있다.\n")
new_address = address[:-5] + "T" + address[-4:]
print(f"new_address = address[:-5] + \"T\" + address[-4:]\nnew_address ==> {new_address} ") # new_address = address[:-5] + "T" + address[-4:]
new2_address = address.replace("D","B")
print(f"new2_address = address.replace(\"D\",\"B\")\nnew2_address ==> {new2_address}\n")
print(f"replace를 사용했지만 실제 address는 바뀌지 않았다. \nprint(address) ==> {address}") # 15 Gukchaebosang-ro 43-gil, Seo-gu, Daegu

print('''
mutable 자료형 : 리스트, 딕셔너리, 집합
immutable 자료형 : 정수, 실수, 문자열, 튜플 ==> 딕셔너리의 key 로 사용 가능!
''')
# mutable 자료형 : 리스트, 딕셔너리, 집합
# immutable 자료형 : 정수, 실수, 문자열, 튜플 ==> 딕셔너리의 key 로 사용 가능!
dict_a = {1: "one", 2.1: "two point one", "a" : "string", (3, 5): "tuple"} # immutable 자료형을 key로 사용
print(dict_a)
print("""
리스트, 딕셔너리, 세트를 key로 입력하면 각각 TypeError가 발생한다.TypeError: unhashable type: 'list'
TypeError: unhashable type: 'list'
TypeError: unhashable type: 'dict'
TypeError: unhashable type: 'set'
""")
# dict_b = {[1,2]: 3} # 리스트를 key로 입력했을 때 ==> TypeError: unhashable type: 'list'
# dict_c = {{1:2} : 3} # 딕셔너리를 key로 입력했을 때 ==> TypeError: unhashable type: 'dict'
# dict_d = { {1,2,3} : 4} # 세트를 key로 입력했을 때 ==> TypeError: unhashable type: 'set'


# 3.
print("\n=================================================================================================\n")
print("3. List에서 Append,insert, extend 차이점, remove/pop 차이점, 각각 예제 코드 작성 및 설명\n")
#3
a_list = ["a", "b", "c"]
print("a_list =", a_list)
print("append 는 리스트에서 가장 \"마지막\"에 요소를 추가하는 것이다.")
a_list.append("e")
print(a_list, ": a_list.append('e') 결과\n") # ['a', 'b', 'c', 'e']
print("insert 는 리스트에서 원하는 인덱스에 요소를 추가할 수 있다.")
a_list.insert(3, "d")
print(a_list, ": a_list.insert(3, 'd'), 3번 인덱스에 'd'가 삽입되었다.\n") # ['a', 'b', 'c', 'd', 'e']
print("extend 는 + 연산과 같다. \
       \nappend([리스트])의 경우 리스트 내에 리스트가 삽입되는 반면, extend는 말그대로 리스트가 확장된다.\
       \n이것 저것 넣어본 결과 정수, 실수형 불가 나머지 입력 가능, 그러나 딕셔너리는 key만 입력된다.")
# a_list.extend(2) # 정수 Error!
# a_list.extend(2.3) # 실수 Error!
a_list.extend("f") # 문자열 가능
a_list.extend(("g","h")) # 튜플 가능
a_list.extend(["i"]) # 리스트 가능
a_list.extend({"j"}) # 세트 가능
a_list.extend({1:"k", 2:"l"}) # 딕셔너리는 key만 입력된다.
a_list.extend({"a":3, "b":4}) # 딕셔너리는 key만 입력된다.
print(a_list) # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1, 2, 'a', 'b']

print("\nremove는 리스트 내 요소를 삭제하는 함수이다.\n단, 같은 요소가 존재할 시 가장 첫 번째로 나오는 요소를 삭제한다.")
a_list.remove("a")
print(a_list, ": a_list.remove('a'), 맨 처음의 'a'만 삭제되었다.\n") # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1, 2, 'a', 'b']

print("pop()은 리스트의 \"맨 마지막 요소\"를 돌려주고 삭제한다")
a_list.pop()
print(a_list, ": a_list.pop() 결과")
print("반환되는 마지막 요소는", a_list.pop(), f"이며 남은 a_list 요소들은 \n{a_list}이다") # a : 맨 마지막 요소 확인
print("pop(n)은 n 위치에 인덱스값을 넣어 원하는 요소를 돌려주고 삭제할 수 있다.")
a_list.pop(0)
print(f"a_list.pop(0)의 결과는 {a_list} 0번째인 'b'를 삭제하였다.")


# 4
print("\n=================================================================================================\n")
print("4. 기존 파싱 코드에서 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기\n")
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250" # 기존 예제
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 40 40 100 100 vehicle 20 20 50 50"

list_txt = str_txt.split() # 공백을 기준으로 나눔

# 리스트 안 index, value 확인
# for i, name in enumerate(list_txt):
#     print(i, name)
# vehicle은 0 ,5, 10, 15 ... 5i 마다 존재 (i= 0,1,2...)
# width는 3, 8, 13, ... 5i + 3 마다 존재 (i= 0,1,2,...)

for i in range(0,len(list_txt),5): # 0부터 리스트의 마지막 인덱스까지, step 5씩! 즉 0, 5, 10, ...
    if int(list_txt[i+3]) >= 100: # width 값이 100 이상일 경우
        list_txt[i] = "truck" # truck으로 값 변경

str_txt = ' '.join(list_txt) # 리스트를 문자열로 변환
print(str_txt) # 값 확인


# 5
print("\n=================================================================================================\n")
print("""5. 기존 파싱 코드에서 데이터를 어떻게 만들면 더욱 효율적으로 처리할 수 있는지
Data 형식 변경 및 추가, 코드 작성 결과 확인(조건은 동일함, 크기가 100보다 크면 vehicle에서 truck으로)""")
# 교수님이 힌트를 주심, 주로 json 파일을 이용한다고 함
# json 파일이 뭔지 찾아보니 파이썬의 dict와 아주 유사하다. key와 value로 표시하고, key는 ""로 묶어서 사용한다.
# dict와 유사하니 최근에 배웠던 pandas의 데이터프레임으로 변환하면 데이터를 한눈에 볼 수 있고 데이터 처리가 더 편리할 듯하다.
# 실제로 찾아보니 read_json()이나 json_normalize()를 사용하여 JSON문자열을 읽고 DataFrame반환하는 함수가 있다.

# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 40 40 100 100 vehicle 20 20 50 50"
# str_txt의 데이터를 vehicle.json에 json 형태로 나름대로 저장해보았다.

# pandas를 이용해 vehicle.json 을 데이터프레임 형태로 불러올 것이다.
import pandas as pd

df = pd.read_json('vehicle.json') # JSON
print(df)

for i in range(len(df)): # 행 전체
    if df.loc[i, "width"] >= 100: # i행의 "width" column의 값이 100 이상일 때
        df.loc[i, "class"] = "truck" # i행의 "class" 값을 "truck"으로 바인딩

print(df) # width 100 이상을 truck으로 수정 완료
