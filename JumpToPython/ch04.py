# def add_mul(choice, *args):
#     if choice == 'add':
#         result = 0
#         for i in args:
#             result = result + i # 받은 인자 모두 더하기
#     elif choice == 'mul':
#         result = 1
#         for i in args:
#             result = result * i # 받은 인자 모두 곱하기
#     return result
#
# a = add_mul("add", 1,2,3,4,5,6,7,8,9,10)
# b = add_mul("mul", 1,2,3,4,5)
# print(a,b)
#
# def say_myself(name, old, man=True):
#     print("나의 이름은 %s입니다." % name)
#     print("나이는 %d입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")
#
# say_myself("Bi", 33, False)

# add = lambda a, b: a+b
# result = add(3,4)
# print(result)



# 사용자 입력과 출력

# print("life""is""too short")
# print("life"+"is"+"too short")
#
# for i in range(10):
#     print(i, end = ' ')


# 파일 읽고 쓰기
# f = open("새파일.txt", 'w', encoding='utf8') # 파일명, 파일 열기 모드, 인코딩(encoding = "utf8")
# for i in range(1, 11):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# readline.py - 한줄 불러오기
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'r', encoding='utf8')
# line = f.readline()
# print(line)
# line = f.readline()
# print(line)
# f.close()

# readline_all.py
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'r', encoding='utf8')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line) # 빈 줄 없애고 싶으면 매개변수 end = '' 넣어주기
# f.close()

# while 1:
#     data = input()
#     if not data: break
#     print(data)

# readlines 사용 - 모든 파일의 줄을 리스트 형태로 저장
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'r', encoding='utf8')
# lines = f.readlines()
# print(lines) # 리스트 형태로 저장 됨
# for line in lines:
#     print(line)
# f.close()

# read 함수 사용
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'r', encoding='utf8')
# data = f.read()
# print(data)
# f.close()

# adddata.py
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'a', encoding='utf8')
#
# for i in range(11, 20):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# 파일 close()는 꼭 해줘야 한다.
# f = open("D:/DailyVy/JumpToPython/새파일.txt", 'w', encoding="utf8")
# f.write("Life is too short, you need python")
# f.close()

# 파일 close() 자동으로 하려면? ==> with문을 사용합시다!
# with open("새파일.txt", "w", encoding="utf8") as f:
#     f.write("A month ago, My mom took a tumble during her early morning workout")


######################### sys모듈로 매개변수 주기 - 명령프롬프트에서 입력한 값 출력하기!!!
# # sys1.py
# import sys # sys모듈 사용하기 위해 임포트!
# # argv는 명령 창에서 입력하는 인수를 의미!!!
# args = sys.argv[1:] # 명령창에서 sys.py aaa bbb ccc 로 입력하면 argv[0]은 sys1.py, argv[1]은 aaa 이런식으로
# for i in args:
#     print(i)
# # 나는 ch04.py에 저장했으므로 PS D:\DailyVy\JumpToPython> python ch04.py aaa bbb ccc 입력

# # sys2.py
# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ') # 대문자로 변해서 나오겠지?
#################################################


##########################연습문제#######################
#1. (is_odd) 함수 작성

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

#2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자. 입력값 개수는 정해져 있지 않음
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2)) # 1.5
print(avg_numbers(1,2,3,4,5)) # 3.0

#3. 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램 -> 오류 수정하기
# input1 = int(input("첫번째 숫자를 입력하세요: "))
# input2 = int(input("두번째 숫자를 입력하세요: "))
#
# total = input1 + input2
# print(f"두 수의 합은 {total} 입니다.")

#4. 3번

#5. text.txt 파일에 문자열 저장 후 출력 -> 오류 수정하기
# f1 = open("text.txt", 'w', encoding="utf8")
# f1.write("Life is too short")
# f1.close()
#
# f2 = open("text.txt", "r")
# print(f2.read())
# f2.close()

#6. 입력한 내용 파일에 저장하는 프로그램
# user_input = input("저장할 내용을 입력하세요: ")
# f = open("text.txt", 'a', encoding='utf8')
# f.write(user_input)
# f.write('\n')
# f.close()

#7.
# f = open("text.txt", "r", encoding="utf8")
# body = f.read()
# f.close()
#
# body = body.replace("java", "python")
#
# f = open('text.txt', 'w', encoding="utf8")
# f.write(body)
# f.close()

with open('text.txt', 'w', encoding="utf8") as f:
    f.write("Done!!! Wrap it up!")