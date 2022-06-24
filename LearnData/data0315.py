# list add/delete, modify ...
list_a = [1, "2", 4.2] # list_a는 변수. 1, "2", 4.2도 메모리 상에서 어느 객체로 존재한다.
print(f'{list_a}', id(list_a))
# id 값을 한 번 체크해보자. list는 mutable한 자료형
# 따라서 수정을 하더라도 새로운 객체를 생성하는 것이 아니라 동일한 주소 값을 참조
list_a[1] = 4
print(f'{list_a}', id(list_a))

# list + 연산(extend)
list_a = list_a + [5, 6] # [1, 4, 4.2, 5, 6]
print(f'{list_a}', id(list_a)) # 얘는 주소 값이 다르죵
# 특정 인덱스의 값을 삭제
del list_a[2]
print(list_a)

# list append, sort 내장 함수 테스트
print("===================append, sort 사용===================\n")
test_list = [1,2,3]
test_list.append([4,5,6,7,8]) # list안에 리스트 추가 [1,2,3,[4,5,6,7,8]]
test_list.append("string")
print(test_list)
# 추가한 리스트를 sort하기 위해서는? sort는 새로운 객체로 들어가는게 아니고 그대로 적용이 된다.
test_list[3].sort(reverse=True)
print(test_list, test_list[3])
# test_list_1 = [1,4,2,9,10,99]
# test_list_1.sort()
# print(test_list_1)

# reverse test (sort x) ==> 단순히 뒤짚는 역할
tmp_list = ['a', 'b', 'd', 'c']
tmp_list.reverse()
print(tmp_list, tmp_list.index('d'))

# list insert, remove 함수 사용
print("===================insert, remove 사용===================\n")
print(tmp_list)
tmp_list.insert(0, [1,2,3]) # insert(인덱스, 넣고자 하는 자료형의 데이터)
print(tmp_list)
tmp_list[0].remove(1) # remove(값) 리스트에서 1을 삭제
print(tmp_list)
tmp_list.remove('d')
print(tmp_list)


# pop, count, extend
print("===================pop, count, extend 사용===================\n")
tmp_list.pop()
print(tmp_list)
tmp_list.pop(0) # pop(인덱스), pop()은 맨 마지막 요소를 반환하고 삭제
print(tmp_list, tmp_list.count('c'))
tmp_list.extend([1,2,3])
print(tmp_list)

# Homework 3월 말까지
# 1. 정수형, 실수형, 문자열 및 '리스트 내 리스트' 등을 포함하여 자신을 소개하는 리스트를 만들고,
# 리스트 인덱싱과 슬라이싱 기법 등을 이용하여 자기 소개하는 것 표현해보기
# 2. 문자열 변수에서 특정 인덱싱으로 접근 후 문자열을 변경할 수 있는가? 답변 및 가능한 방법 코드 작성 및 제출,
# mutable, immutable 자료형 정리해보기.
# 3. List에서 Append,insert, extend 차이점, remove/pop 차이점, 각각 예제 코드 작성 및 설명
# 4. 기존 파싱 코드에서 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기
# 5. 기존 파싱 코드에서 데이터를 어덯게 만들면 더욱 효율적으로 처리할 수 있는지
# - Data 형식 변경 및 추가, 코드 작성 결과 확인(조건은 동일함, 크기가 100보다 크면 vehicle에서 truck으로)

# tuple
print("===================tuple입니다===================\n")

# dictionary 자료형은 {key:value, ..., key:value}
print("===================dictionary입니다===================\n")

a = {1: 'a', 2: 'b'}
# 딕셔너리에 특정 key:value 쌍을 넣고 싶을 때
# Dict[key] = 'value'
a[3] = 'c'
a[4] = 'd'
a[5] = 'e'
a['name'] = ["Choi", "Kim", "Yu", "Lee"]
print(a)

del a[1] # a라는 딕셔너리 변수에서 key값이 1인 쌍을 삭제
print(a)

a = {'Dept':['AI-Engr.', 'Smart Elect.'], 'StudentNum' : [22, 50]}
# 딕셔너리의 특정 값에 접근할 대는 딕셔너리의 키 값으로 접근
print(a['Dept'], a['StudentNum'])

# key 값 중복시 하나만 남기고 나머지는 삭제 or 무시
a = {'1': 'a', '2': 'b', '3': 'c', '1': 'd'} # key값 중복
print(a, a['1']) # key값 중복하면 기존에 있던 key값을 날려버리네?

a = {
    ('name', 'age') : (["Choi", "Kim", "Yu", "Lee"], [22, 23, 24, 25])
}
print(a)