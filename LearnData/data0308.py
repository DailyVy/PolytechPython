# a = 123
# b = -1234
# print(a, b)
#
# fa = 12.345
# fb = -3.14159265
# fexpA = 4.24E3
# fexpB = 4.24E-3
#
# print(f'float number example: {fa}, {fb}, {fexpA}, {fexpB}') # f-문자열 (v3.6이상)
# print("float number example: {0}, {1}, {2}, {3}".format(fa, fb, fexpA, fexpB))
# print('float number example: {a}, {b}, {c}, {d}'.format(a=fa, b=fb, c=fexpA, d=fexpB))
#
# print(f'a의 16진수: {a:0x}, 실수 표현: {a:f}')
#
# #8진수 practice
# octA = 0o1777 # 8진수를 표기할 때 숫자 0 + 알파벳 o(O)
# print(octA)
#
# #16진수 (HexaDecimal)
# hexA = 0x1FF24 # 16진수를 표기할 때 숫자 0 + 알파벳 x(X)
# print(hexA)


# floating point example
# num = 0.0
#
# for idx in range(0, 100): # range(a, b) 는 a부터 b-1 의 값이다.
#    num += 0.1 # num = num + 0.1
#
# print(num) # 10이 나올 줄 알았는데 아니네
# print(f'소수점 아래 18자리 :{num : .18f}') # 소수점 아래 18자리 까지 표현


# num1 = 20
# num2 = 3
#
# sumR = f'{num1 + num2}' # 문자열로 포맷팅~ 이렇게도 되는구나
# print(sumR, type(sumR), f'{num1*num2}', f'{num1/num2}' )
#
# # 나누기 몫, 승수
# print(num1//num2)
# print(num1**num2)


# 구구단
# for i in range(1, 10):
#     i = i * 2
#     print(f'2 x {int(i/2)} = {i}')
# # 교수님
# for x in range(1,10):
#     print(f'2 x {x} = {2 * x}') # 아 굳이 i에 대한 식을 넣어줄 필요가 없구나


# 소수(Prime Number 구하기) 약수가 1과 자기 자신밖에 없는 수
# testNum = 10477
# for i in range(2, testNum):
#     if (testNum % i) == 0:
#         print(f'{testNum}은 소수가 아닙니다.')
#     else:
#         print(f'{testNum}은 소수!') # 이러면 여러개 나오는데 한번만 나오게 하는 방법은 없을까?

# testNum = int(input("양의 정수를 입력하십시오> "))
# testNum = 15
#
# if testNum > 2:
#     for i in range(2, testNum):
#         if (testNum % i) == 0:
#             print(f'{testNum} is not Prime Number')
#             break
#         else:
#             print(f'{testNum} is Prime Number!')
#             break
# elif testNum == 2:
#     print(f'{testNum} is Prime Number!')
# else:
#     print(f'{testNum} is not Prime Number')

#다른 분이 하신 거 보면 int(sqrt(testNum))으로만 해도 소수 판단 가능하다던데

# 숫자 입력할 때 까지!!!
# while(1):
#     testNum = input()
#     if(testNum.isdigit()):
#         break


# testNum = 7
#
# if testNum > 2:
#     for i in range(2, testNum):
#         if (testNum % i) == 0:
#             print(f'{testNum} is not Prime Number')
#         else:
#             print(f'{testNum} is Prime Number!')
# elif testNum == 2:
#     print(f'{testNum} is Prime Number!')
# else:
#     print(f'{testNum} is not Prime Number')

# 숫자만 입력할 수 있도록
while(1):
    testNum = input("양의 정수를 입력하십시오> ")
    if (testNum.isdigit()): # istype()이 True 라도 데이터타입은 str이므로 int로 변환 후에 진행
        testNum = int(testNum)
        break

if testNum > 2: # 입력 숫자가 2를 초과할 때
    for i in range(2, testNum): # 1부터 시작하면 1로 나누어 떨어져서 나머지가 소수여도 나머지가 0이 되므로 2부터 시작.
        if (testNum % i) == 0:
            print(f'{testNum} is not Prime Number') # 2부터 입력숫자 앞까지 범위를 돌았을 때 한번이라도 0이 나오면 소수 X
            break # 판별후 여러 줄 출력을 피하기 위해
    else: # if 문을 다 돈 뒤 if문 조건을 만족 하지 않았을 시(즉, 소수일 때) for문에서 빠져나와서 바로 소수임을 출력
        print(f'{testNum} is Prime Number')
elif testNum == 2: # 입력 숫자가 2일때
    print(f'{testNum} is Prime Number!')
else: # 그 외의 숫자가 입력됐을 때
    print(f'{testNum} is not Prime Number')



