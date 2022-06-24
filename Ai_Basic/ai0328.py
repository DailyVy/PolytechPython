# 2022-03-28
# 1교시
# 딕셔너리

# a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
# print(a.keys())
#
# for k in a.keys():
#     print(k)
#
# print('name' in a)
# print('email' in a)
#
# print(a.get("nokey")) # 없으면 None 반환
# print(a["nokey"]) # 에러 발생
# 에러가 발생하지 않는다는 가정하에는 똑같지 않나? ==> 상시적으로 메모리로 접근할 때는 a[key]가 더 좋습니다.

# Practice 2
a = {
    'name' : ["김근형", "정경임", "이은주", "이시영", "안원영", "최지호"],
    'ID' : [220100, 220101, 220102, 220103, 220104, 220105]
}
list_tmp = ["name", "ID"]
print(a)

dict_keys = a.keys()
for i in dict_keys:
    print(i)
for i in list_tmp:
    print(i)
list_tmp.append("Phone-Number")
# dict_keys.append("Phone-Number") # dict_keys.append 는 존재하지 않음

# list 형으로 변경 (형 변환: 내가 원하는 자료형으로 변경)
# dict_list = ['name', 'ID, ....., N] => key가 100개가 있을 때 key 값을 변경하고 싶다?
# key 값을 재 가공하고 싶을 때 형 변환 후 사용
dict_list = list(a.keys())
dict_list.append("Phone-Number")
print(dict_list, dict_list[0])
# list 뿐만 아니라 원하는 자료형으로 형은 변환 가능
b = '123'
c = int(b) # 문자열 "123"을 정수형 123으로 변환 후 c변수에 바인딩(assign?)
print(type(b), b, type(c), c)
print(dict_list[0])
print(f'{dict_keys}\n{dict_list}\n{list_tmp}')

# values, items
print(a.values(), type(a.values()))
print(a.items(), type(a.items()))

# clear, in, get
# dictionary에 데이터 추가 (phone number라는 키 값에 전화번호 value)
a["Phone Number"] = ["010-1234-5678"]
print(a)
b = a # binding ==> a, b는 메모리 주소가 같다. ==> a 수정하면 b도 수정된다!!!
copy_a = a.copy() # 새로운 객체 생성 ==> 새로운 메모리 주소 할당
print(id(a), id(b), id(copy_a))

a.clear()
print(a, b, copy_a) # a를 지웠더니 b도 지워짐(메모리 주소를 공유하기 때문에) 하지만 copy_a는 새로운 객체이므로 변동 없음

# in, get
# in (a 라는 dictionary에 ~~의 key값이 있니?)
print('name' in a, 'addr' in a, 'name' in copy_a, 'addr' in copy_a)
# get example
print(a.get('name'), a.get('addr')) # None None
print(a.get('addr', 'Default')) # Default
# print(a['name']) # Error? ==> KeyError: 'name'


# 2교시
# Set
s1 = set([3,1,2,4])
list_a = [3,1,2,4]
s2 = set("HELLO")
# s1, s2 : 중복이 없으며, 순서가 없다.
print(s1, list_a, s2)
# set 자료형은 access가 불가능하고, 하고 싶은 경우 다른 자료형으로 변환
s1_tuple = tuple(s1)
print(type(s1_tuple), s1_tuple, s1_tuple[0], s1_tuple[1])
# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5])
s2 = set([2,3,5,6])
print(f'교집합={s1.intersection(s2)}, 합집합={s1.union(s2)}, 차집합={s1.difference(s2)}')
# 값 하나 추가(add), 여러 개 추가(update), 삭제(remove)
s1.add(6)
print(s1)
s1.update([6,7,8,9])
print(s1, "리스트 update")
s1.update((10,11,12,13))
print(s1, "튜플 update")
s1.update({13,14,15,16})
print(s1, "set update")
s1.update({17:'a',18:'b'})
print(s1, "dictionary update, key값만 들어간다")
s1.remove(1)
print(s1)


# 3교시
# Bool 자료형 Example
a = True
b = False
print(type(a), type(b))
print(f'1==1? {1==1}, 1==2? {1==2}, 1<2? {1<2}')

# Bool 문자열일 경우, 하나라도 있으면 True, 아니면 False
# str_t = "" 될 때까지 하나씩 찍어보고, False가 되면 while문에서 break;

str_t = "HELLO"

# while 문 뒤에 오는 조건문이 True일 때까지 계속 반복해서 아래 문장 수행
while str_t: # 처음에는 True ==> ""(False)
# while str_t == True: # 이렇게 잘 쓰지 않아요
# while len(str_t) > 0:
    print(len(str_t), str_t)
    str_t = str_t[:len(str_t)-1]

if 1:
    print("True")

if []:
    print("True")
else:
    print("False")

list_a = [1,2,3,4,...,None]
# list_a에서 특정 작업을 수행 후, 마지막이 됐을 때, 즉 []일 때 뭔가를 수행하고 싶을 경우
if list_a:
    print("True")
else:
    print("False")

if [1,2,3]:
    print("True")
else:
    print("False")

# Bool 내장 함수
print(f'"python"은 True? False? {bool("python")}')


# 4교시
### Variable assignment Skip
a = 1
# if a = 1: # a==1 을 안쓰면 Error나용
#     print("True")

# 복사
# a.copy(), b = a(주소값 공유, 복사 개념 X)
a = [1,2,3]
b = a[:] # b = a 와 다름, 리스트를 슬라이싱해서 변수에 assign할 경우 새로운 객체 생성하고 b는 새로 생성된 객체의 주소를 참조.
c = a.copy()
d = a
e = [1,2,3] # 얘도 새로운 객체 생성
print(id(a), id(b), id(c), id(d), id(e), a is d, a is e)
a[2] = ['1','2']
print(a, d) # a, d: [1,2,['1','2']]


# 변수 만들기
a, b = ("coding", "life",)
print(type(a), type(b), a, b)
(a, b) = ("coding", "life",)
print(type(a), type(b), a, b)
[a, b] = ["coding", "life"]
print(type(a), type(b), a, b)
a = ("coding", "life",)
print(type(a), a)
a = "coding", "life",
print(type(a), a)

# Swap
a, b = 3, 10
print(a, b)
a, b = b, a
print(a, b)


#### 제어문
