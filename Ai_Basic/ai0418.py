# 1교시 - 함수
# 매개변수(parameter)의 개수가 정해지지 않았을 때
# def func(*args):
def add_many(*args):
    result = 0 # return 변수 정의
    for i in args: # args가 list일 경우, list의 값 자체를 가지고 올 수 있음
        result += i
    return result

# main 함수
rtn_val = []
# 가변인자를 넘기고 싶을 때 : (1, 2), (1, 2, 3), (1, 2, 3, 4), ....
rtn_val.append(add_many(1, 2, 3, 4, 5))
rtn_val.append(add_many(1, 2, 3, 4))
rtn_val.append(add_many(1, 2, 3))
print(rtn_val) # [15, 10, 6]

# 리스트를 넘길 때는? *를 붙이자
var_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tmp = add_many(*var_list)
print(tmp) # 55

# 더하기, 곱하기하는 함수를 만들자
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
        return result

print(add_mul('add', 1, 2, 3, 4, 5)) # 15
print(add_mul('mul', 1, 2, 3, 4, 5)) # 120

################################################################################
# Lane_Detection.py (.java, .c)
# def pre-processing():
# def hough_transform():
# def select_lane():
# def draw_lane():

# main (Lane_Detection.py import)
"""
pre-precessing()
hough_transform()
select_lane()
draw_lane()
"""
################################################################################

# 2교시
# 키워드 파라미터 연습
# **kwargs 처럼 **를 붙이면 매개변수  kwargs는 딕셔너리가 된다. ==> 내장함수 사용 가능
def func_kwargs(**kwargs):
    print(kwargs)
    print(kwargs.items())

func_kwargs(a=3, b=4)

# 딕셔너리 복습
# dict_var = {'a':1, 'b':3}
# print(dict_var.items()) # [('a', 1), ('b', 2)] : 리스트 튜플로 반환
# print(dict_var.keys()) # 리스트로 반환 ['a', 'b'] ==> 결과 값 자체를 활용하기 위해서는 list(dict_var.keys())
# print(list(dict_var.keys()))
# print(dict_var.values()) # 리스트로 반환 [1, 2]

def func_kwargs_ex(**kwargs):
    for items in kwargs.items():
        print(items)

func_kwargs_ex(x=100, y=200, z='abc')

def add_mul(a, b):
    return (a+b), (a*b)

print("result = %d, %d" % add_mul(2, 4))
print(f'result = {add_mul(2,4)}, {type(add_mul(2,4))}') # 변수 형태로 받으면 튜플을 없앨 수 있다고?, 어떻게 하면 좋을지?
a, b = add_mul(2, 4)
print(f'result = {a}, {b}') # 요렇게!!!
print()

# 초깃값 설정하기
# 입력 o, 출력 x 함수 - 함수의 출력은 항상 return
def say_myself(name, age, dept="AI_Engr."):
    print(f'name is {name}')
    print(f'age is {age}')
    print(f'dept is {dept}\n')

say_myself("Bigyeol", 33)
say_myself("Yuna", 33, dept="Fig.Skate")

# 변수의 사용 범위
# 지역 변수: 특정 함수 내에서 사용하는 변수들
# 전역 변수: 어떤 함수에서도 해당 변수를 호출해서 사용 가능 (공유)
# 전역 변수: 일반적으로 함수 밖에서 정의를 함, python에서는 global 예약어를 이용해서 명시적으로 표현
a = 1

def vartest(a):
    a = a + 1
    print(a)

vartest(a) # 함수에서 2로 변화가 되었지만 # 103 line의 print 결과
print(a) # 출력을 해보면 1로 출력된다.

# 3교시
# 변수명 명명 규칙
# global 변수는 gLocalVal
local_var = 0
def varTest1(input):
    # 109 line의 local_var과 varTest1 함수 내의 lacal_var 다르다.
    global local_var # 하지만 global을 이용하여 전역변수로 선언, 함수 밖에 잇는 local_var변수를 함수 내에서도 사용 가능
    local_var = input + 1 # local_var은 함수 내의 변수(지역변수), 함수 밖에서 사용할 수 없다.

# varTest1(3) #
print(local_var)

def varTest2(input):
    global local_var
    local_var = input * 2

varTest2(3) # input이 3이니까 6이되서 나옴
print(f'local_var={local_var}') # 6
print()

# lambda 함수
add = lambda a, b: a + b
print(add(3, 4))
print()

### Practice
# 함수 범위
a = 1
def varTest(a):
    a = a + 1

varTest(a)
print(a) # 1

def varTest1(inner_var):
    inner_var = inner_var + 1

varTest1(3)
# print(inner_var) # inner_var은 함수 내의 변수!

# Global / lambda
# global
aa = 1
def globaltest(a):
    global aa
    aa = a + 1

globaltest(3) # aa =4
print(aa) # 4

# lambda
add = lambda a, b: a + b
result = add(3, 4)
print(result)

# 4교시 - 클래스
