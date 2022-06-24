# 예외 처리

# index error와 zero devision이 발생하는 코드가 있는 함수 하나 작성
# def proc_error():
#     f = open("temp.txt", "w", encoding="utf8")
#     try:
#         # f.write("Hello, World!")
#         # f = open("foo.txt", "r", encoding="utf8")
#         # aa = 3 / 0
#         # a = [1, 2]
#         # print(a[3])  # list index out of range
#         # b = 4 / 0
#     # except:
#     #     print("Error가 발생할 거 같은뎅..?")
#     # except IndexError as e:
#     #     # class IndexError(Exception):
#     #     #   def __str__(self):
#     #     #       return "list index out of range"
#     #     # print("out of range for list a")
#     #     print(e)
#     # except ZeroDivisionError as e:
#     #     print("Can't Divided by Zero")
#     except (ZeroDivisionError, IndexError, FileNotFoundError) as e:
#         print(e)
#     finally:
#         print("수행되었습니다.")
#         f.close()


# proc_error()

# 예외 처리  2
# 나이를 입력받는 함수
# Django Framework, Flask가 됐던
# input text form 에 나이를 입력받는다..

# todo : 99살까지만 입력되도록 합시다...
# class MyError(Exception): # 파이썬 내장 클래스인 Exception클래스를 상속하여 생성
#     def __str__(self):
#         return "나이는 1 ~ 99 까지 가능합니다."
#
# def input_age():
#     # input : 반환형이 문자열 ==> int(정수형)으로 casting
#     while True:
#         try:
#             age = int(input("나이를 입력하세요(숫자만) : "))
#             if 0 < age < 100:
#                 break
#             else:
#                 # print("나이를 잘못 입력하였습니다. 1 ~ 99까지 입력가능합니다.")
#                 raise MyError
#         # except ValueError as e:
#         #     print(e)
#         except ValueError:
#             print("다시 입력해주세요! 나이는 숫자만 입력 가능합니다.")
#         except MyError as e:
#             print(e)
#     return age
#
#
# print(input_age()) # 스물, 이렇게 입력하면 ValueError가 발생함


# 자기자신만의 예외클래스 작성하기
# 내장되어 있는 예외 클래스가 아니라
# 직접 작성한 예외처리 코드로 예외를 처리하고 싶을 때
# Exception 클래스를 상속받아서 생성 가능
#
# class MyError2(Exception):
#     # pass
#     def __str__(self):
#         return "무슨 소릴 하는거야"
#
#
# # 별명을 출력하는 함수에서 "바보"가 들어오면 작성한 MyError 예외 클래스 호출
# # 강제로 에러 발생시키는 방법 : raise 사용
#
# # 1. raise MyError2 를 통해 비정상 종료 (어떤 에러가 나왔는지는 에러에 명시됨)
#
# def say_nick(nick):
#     if nick == "바보":
#         raise MyError2
#     print(nick)
#
#
# # say_nick("천재")
# # say_nick("바보")
#
# # 2. 비정상적인 종료보다는 Try, Except를 이용해서 정상종료
# try:
#     say_nick("천재")
#     say_nick("바보")
# except MyError2:
#     print("허용되지 않은 별명입니다.")
#
# # 3. MyError as e를 통해서 정해진 Error message를 출력하고자 할 때
# # __str__
# try:
#     say_nick("천재")
#     say_nick("바보")
# except MyError2 as e:
#     print(e)
#
#
# # 함수의 입력 인자, (bool, list): bool이 true일 때는 리스트를 출력
# # 아니면 정해놓은 Error 발생 (NotAccessList)
# class NotAccessList(Exception):
#     def __str__(self):
#         return "List에 접근 권한이 없습니다."
#
#
# def list_access(in_bool, in_list):
#     if in_bool:
#         print(in_list[:])  # print(in_list)
#     else:
#         raise NotAccessList
#
#
# try:
#     list_access(1, [1, 2, 3, 4])
#     list_access(0, [1, 2, 3, 4])
# except NotAccessList as e:
#     print(e)

# filter, map, zip..
# 리스트를 입력받아 양수만 리턴하는 함수 (positive)
# 중첩 리스트 제외. (ex: [1, 2, [1, 2, -3], 33, 41] ==> X
# [1, 2, -3, -4, ..]
def rtn_positive(in_list):
    rtn_list = []
    for val in in_list:
        if val > 0:
            rtn_list.append(val)
    return rtn_list


print(rtn_positive([1, -1, 2, -2, 3, -3]))


# filter
# filter에서 사용할 양수만 반환하는 함수를 작성할 경우
def func_positive(x):
    return x > 0


# filter(f, iterable한 자료형의 변수)
# 함수의 반환 값이 참인 것만 묶어서 반환
print(list(filter(func_positive, [-1, 2, 3, 4, 0, 5, -7])))  # [2, 3, 4, 5]

# lambda
print(list(filter(lambda x: x > 0, [-1, 2, 3, 4, 0, 5, -7])))  # [2, 3, 4, 5]
## 예상 결과값:
print(list(filter(lambda x: x * 2, [-1, 2, 3, 4, 0, 5, -7])))  # [-1, 2, 3, 4, 5, -7]
# filter, map, 파이썬에서 가장 많이 사용하는 형태: 리스트 내포..
# list comprehension : 리스트 안에 제어문을 넣어서 원하는 결과값을 리스트 형태로 얻고자 할 때
positive_value = [value for value in [-1, 2, 3, 4, 0, 5, -7] if value > 0]  # [2, 3, 4, 5]
print(positive_value)


# 결론적으로는 익숙하지 않으면 함수로 한 번 내려서 표현해보자


# map: 입력리스트를 *2해서 반환하는 함수를 적용
def twice(x): return x * 2  # 함수 형태로 한 번 만들어 보세요.


in_list = [1, 2, 3, 4]
print(list(map(twice, in_list)))  # [2, 4, 6, 8]
twice_list = [value * 2 for value in in_list]
print(twice_list)  # # [2, 4, 6, 8]


######## 2022-05-10 ######
# isinstance(object, class) : object가 class의 인스턴스인가?

# 간단하게 클래스를 만들어봅시다.
class Person:
    pass


class Student(Person):
    pass


class Male:
    pass


# 객체를 생성해봅시다.
a = Person()
b = Student()
c = Male()
print(isinstance(a, Person))
print(isinstance(b, Person))  # True : 오! Person을 상속받아 만든 Student의 객체인 b는 Person의 인스턴스이기도 하다.
print(isinstance(b, Student))
print(isinstance(c, Person))
print(isinstance(c, Male))

# zip : 인덱스가 동일한 것끼리 묶어서 튜플로 반환,
# 동일한 개수의 iterable한 순서가 있는 객체에서
# 동일한 index끼리 묶는 것
list_1 = [1, 2, 3]
list_2 = [2, 4, 5]
list_3 = list(zip(list_1, list_2))
print(list_3)
print(list(zip('abc', "def")))
