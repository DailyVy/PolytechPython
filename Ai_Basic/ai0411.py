# 함수
# 더하기 곱하기 빼기 함수 작성
a = 3
b = 4
# print(a + b)
# 함수로..
# add / sub 함수 작성
# 파라미터 이름은 마음대로 지정하면 됨 (단, 의미있는 이름으로)
def add(num_add1, num_add2):
    return num_add1 + num_add2

def sub(num_sub1, num_sub2):
    return num_sub1 - num_sub2

def mul(num_mul1, num_mul2):
    return num_mul1 * num_mul2

def div(num_div1, num_div2):
    if num_div2 == 0:
        return 0
    else:
        return num_div1 / num_div2

# 함수를 사용하기 위해서는 함수를 호출
result_add = add(a,b)
result_sub = sub(a,b)
print(result_add, result_sub, add(a, b), sub(100, 5))

# 함수 종류는 입출력에 따라 4가지 존재
# 입력이 있고 출력도 있는 것은 위의 add, sub, mul, div 예제

# 입력x, 출력만 있는 함수 (출력은 return을 말한다)
# 입력 파라미터가 없더라도 반드시 괄호는 해줘야 함
def add_5_6():
    return 5 + 6
# 1 ~ 100 까지 더하는 함수를 하나 작성(입력x, 출력은 100까지 누적된 값을 리턴
def accum_100():
    sum = 0
    for idx in range(101):
        sum += idx
    return sum

print(accum_100())

# 입력은 있지만 return이 없는 함수 작성
def mul(num1, num2):
    print(num1 * num2)

rtn_val = mul(11, 22)
print(f'return value is {rtn_val}')

# 함수의 입력, 출력이 모두 없는 케이스는 한 버 ㄴ실습해보세요.
def inputoutputx():
    print("None")

inputoutputx()

# 함수 호출시에 다양한 방법으로 호출해보자
c = 5
d = 3
mul(num1=2, num2=5), mul(33, 44), mul(num2=2, num1=3), mul(c,d)



def func_kwargs(**kwargs):
    print(kwargs)

func_kwargs(a=1, b=3)


def myFunc(**kwargs):
    for item in kwargs.items():
        print(item)

myFunc(x=100, y=200, z='abc')