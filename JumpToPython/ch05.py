################################## 클래스를 해봅시다 #######################################

# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num):
#         self.result += num
#         return self.result
#
# cal1 = Calculator() # cal1은 객체고요, cal1은 Caculator의 인스턴스(관계위주로 설명)예요!
# cal2 = Calculator()
#
# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))


# 사칙연산 클래스 만들기

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#
# a = FourCal()
# b = FourCal()
#
# # print(type(a)) # <class '__main__.FourCal'> : 객체 a의 타입은 FourCal의 클래스이다.
#
# a.setdata(4,2) # FourCal.setdata(a, 4, 2) 와 같다.
# print(a.first)
# print(a.second)
# print(id(a.first), id(a.second))
# b.setdata(3, 7)
# print(b.first)
# print(b.second)
# print(id(b.first), id(b.second))



# 사칙연산 클래스 만들기 다시!!!

# class FourCal:
#     def setdata(self, first, second): # 두 숫자 입력받는 메소드
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# a = FourCal()
# b = FourCal()
#
# # a.setdata(4,2)
# # b.setdata(3,8)
# # print(a.first, a.second, id(a.first))
# # print(b.first, b.second, id(b.first))
#
# print(a.add(), b.add())
# print(a.sub(), b.sub())
# print(a.mul(), b.mul())
# print(a.div(), b.div())


# 생성자!(Constructor)를 구현해보자!
# 생성자란 객체가 생성될 때 자동으로 호출되는 메서드, __init__ 사용하면 이 메서드는 생성자가 된다.

# class FourCal:
#     def __init__(self, first, second):
#         self.first = first
#         self.second = second
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal() # 오류발생, 생성자 __init__이 호출되었는데 매개변수값이 존재하지 않기 때문
# a = FourCal(5, 2)
# print(a.first, a.second)


# 클래스 상속하기
# class MoreFourCal(FourCal): # 비교 : class FourCal: 클래스를 상속하기 위해서는 클래스 뒤 ()안에 상속할 클래스 이름 입력!
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
# b = MoreFourCal(2, 10)
# print(b.add(), b.sub(), b.mul(), b.div()) # FourCal의 기능 사용가능
# print(b.pow())


# 메서드 오버라이딩(Method Overridng)
# 부모클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것

# a = FourCal(4,0)
# print(a.div() # ZeroDivisionError 에러발생

# class SafeFourCal(FourCal):
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
#
# a = SafeFourCal(4,0)
# print(a.div()) # 0을 리턴


# 클래스 변수
# class Family:
#     lastname = "김" # lastname이 바로 클래스변수!!
#
# print(Family.lastname)
#
# a = Family()
# b = Family()
#
# print(a.lastname, b.lastname)
#
# Family.lastname = "박" # 클래스변수 값을 바꿔볼까??
# a = Family()
# b = Family()
#
# print(a.lastname, b.lastname) # 박 박
# # 클래스 변수 값을 변경했더니 객체의 lastname값도 모두 변경된다!!!
# # 즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다!
# # 객체변수는 독립적인데~ 클래스변수는 모든 객체에 공유되는구나!
#
# print(id(Family.lastname),id(a.lastname), id(b.lastname)) # 어라 다 똑같넹??? ==> 같은 메모리를 가리켜!!


# 모듈
# 함수 or 변수 or 클래스를 모아 놓은 파일
# 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
# import mod1 # import 모듈이름 : 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어!! 단, 경로 조심!!
#
# print(mod1.sub(4,2)) # 모듈이름.함수이름
# print(mod1.add(6,3))
#
# from mod1 import add # from 모듈이름 import 모듈함수
# print(add(6,3))
# print(sub(3,4)) # 얜 import 안해서 에러!

# import mod2 # 변수, 클래스, 함수가 포함 된 파일
#
# # print(mod2.PI)
# # a = mod2.Math()
# # print(a.solv(2))
# # print(mod2.add(mod2.PI,4.4))
#
# # 반지름이 5인 원의 넓이 구하기
# a = mod2.Math()
# print(a.solv(5))




# # 클래스 생성자부터 다시!
# class FourCal:
#     def __init__(self, first, second): # 객체가 생성될 때 자동 호출!!!!!
#         self.first = first
#         self.second = second
#     def add(self):
#         result = self.first + self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result
#
# a = FourCal(4, 2)
# b = FourCal(3, 7)
# print(a.add(), a.first, a.second, id(a.first))
# print(b.mul(), b.first, b.second, id(b.first))
#
# # 상속
# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result
#
# c = MoreFourCal(3, 2)
# print(c.pow(), c.add())
#
# # 메서드 오버라이딩 : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것!
# class SafeFourCal(FourCal): #일단 상속!
#     def div(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first / self.second
# d = SafeFourCal(4,0)
# print(d.add(),d.div())
#
# # 클래스 변수
# class Family:
#     lastname = "Choi"
#
# print(Family.lastname)
# e = Family()
# print(e.lastname)
#
# Family.lastname = "Park"
# print(e.lastname) # Park 으로 바귀었네!
# print(id(Family.lastname), id(e.lastname)) # 주소가 같다.

# 모듈 : 함수나 변수, 클래스를 모아둔 파일
# 모듈.함수이름
# import mod1
# from mod1 import add, sub
# from mod1 import * # mod1 모듈 안의 함수를 전부 import!

# if __name__==  "__main__": 의미
# 이 코드가 있는 파일을 실행할 때는 if문 다음의 문장 수행
# 하지만 이 파일을 모듈로서 불러와 다른 파일에서 실행할 때는 if문 아래 문장을 수행하지 않는다.

# 패키지 : 도트(.)를 이용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 해준다.
# 패키지는 파이썬 모듈로 이루어져 있다.
# import game.sound.echo # 모듈까지 접근(파일) import 이후 문자를 다 작성해줘야 메서드 실행할 수 있다.
# game.sound.echo.echo_test() # print("echo")라 echo
#
# from game.sound import echo # game.sound로부터 echo를 임포트 ==> echo.메서드
# echo.echo_test()
#
# from game.sound.echo import echo_test # echo_test함수를 직접 import
# echo_test()

# 안되는 예
# import game # game 디렉터리의 모듈 or game 디렉터리의 __init__.py에 정의한 것만 참조 가능하다!
# game.sound.echo.echo_test() # 이거 안됨

##### import할 때 가장 마지막 항목인 c는 모듈 또는 패키지!!! 즉
# import game.sound.echo.echo_test() 이건 안됨!!!!!! from을 통해 import echo_test() 는 가능하지만!
# from game.sound import echo.echo_test() 이것도 안됨!!!

# __init__.py의 용도
# from game.sound import * # 특정 디렉터리의 "모듈"을 *로 import 할때
# # __init__.py에 __all__변수를 설정해야 한다!!
# echo.echo_test() #.. 어 왜 되냐? => __all__ 변수 설정을 해줬기 때문에 된다! __all__=["echo"]
# # => 여기서 __all__이 의미하는 것은 sound디렉터리에서 *기호만 사용하여 import할 경우 이 곳에 정의된 echo모듈만 import된다는 것!
# # 어 그럼 echo말고 다른걸로 해보자
# wav.wav_test() # 역시 안되네 __all__ = ["echo","wav"] 해보자 ==> 된다!!!


# relative 패키지
# ==> render.py 에서 진행



###### 예외 처리 ==> 오류가 발생할 때, 오류 무시하고 싶으면 try, except문!
# f = open("test", "r", encoding="utf8") # FileNotFoundError
# print(4/0) # ZeroDiviosnError : division by zero

# a = [1, 2, 3]
# a[4] # IndexError: list index out of range

# 오류 예외 처리 기법 : try, except문
# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

# IndexError가 발생할 때 오류 메시지를 출력하는 작성 해보자!!
# try:
#     a = [1,2,3]
#     print(a[4])
# except IndexError as message:
#     print(message)
#
# # try ... finally 문
# f = open("text.txt", "a", encoding="utf8")
# try:
#     f.write("뭘하면 좋을까~\n")
# finally: # finally절은 예외 발생 여부에 상관없이 항상 수행!!!!
#     f.close()

# 여러 개의 오류
# try:
#     a = [1, 2]
#     print(a[3]) # IndexError
#     4/0 # ZeroDivisionError
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱 할 수 없습니다.")
# # ==> IndexErro가 먼저 일어났으므로 ZeroDivisionError는 나오지 않았다.
#
# try:
#     a = [1, 2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# list index out of range 만 출력되고 division by zero는 출력되지 않는다.

# 동시에 예외 처리하기 except () ==> 책과 다르게 동시에 예외처리가 안됨
# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)
# list index out of range 만 나오는걸...?


# # 오류 회피하기 except ErrorName:pass
# try:
#     f = open("나없는파일", 'r', encoding='utf8')
# except FileNotFoundError:
#     pass

# # 오류 일부러 발생시키기 ==> raise 명령어 사용
# class Bird:
#     def fly(self):
#         raise NotImplemented # 파이썬 내장 오류 : 작성해야 하는 부분이 구현되지 않았을 경우, 오류를 일으키기 위해 사용
#
# class Eagle(Bird):
#     def fly(self): # 메서드 오버라이딩
#         print("very fast")
#
# eagle = Eagle()
# eagle.fly()

# # 예외 만들기
# class MyError(Exception): # 파이썬 내장 클래스 Exception
#     # pass
#     def __str__(self):
#         return "허용되지 않은 별명입니다."
#
# def say_nick(nick):
#     if nick == "바보":
#         raise MyError()
#     print(nick)
#
# # say_nick("천사")
# # say_nick("바보")
#
# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e) # MyError 클래스에 def __str__(self): 없으면 출력하지 않음
#     # print("허용되지 않는 별명입니다.")


## 내장 함수

# # all(x) : 반복 가능한(iterable)자료형 x를 인수로 가짐 => True(x가 모두 참이면) or False
# # iterable data type : for문으로 값을 출력할 수 있는 것 ==> 리스트, 튜플, 문자열, 딕셔너리, 집합
# # 요소에 0 이 있으면 0은 거짓이므로 False를 반환
#
# # any(x) : all과 반대로 x 중 하나라도 참이 있으면 True, 모두 거짓이면 False
#
# # chr(i) : ASCII 코드 값을 입력받아 해당 문자를 출력하는 함수
# a = chr(97) # 'a'
# num_0 = chr(48) # 0
# print(a, num_0)
#
# # dir() 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
# # print(dir([1,2,3]))
#
# # divmod(a, b) => a / b 의 몫과 나머지 튜플형식으로 반환
# print(divmod(5,4)) # // %
#
# # enumerate : 열거하다라는 뜻, 순서가 있는 자료형(리스트, 튜플, 문자열)입력받아
# # 인덱스 값을 포함하는 enumerate 객체를 돌려준다. ==> for문과 함게 자주 사용
# for i, name in enumerate(['body', ' foo', 'bear','shoulder', 'feet']):
#     print(i, name)
# # 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
#
# # eval(expression) 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값 반환
# a = eval('1+2')
# b = eval("'hi' + 'a'")
# c = eval('divmod(4,3)')
# print(a,b,c)

# # filter(함수이름, 반복가능한 자료형) ==> 반환값이 참인 것만 묶어서 돌려줌
# def positive(l):
#     result = [] # 반환값이 참인 것만 걸러내서 저장할 변수
#     for i in l:
#         if i > 0: # i가 0보다 클 때
#             result.append(i) # 리스트에 i 추가
#     return result
# print(positive([1,-3,2,0,-5,6]))
#
# # 위의 positive 함수는 양수 값만 돌려줌 ==> filter 이용하여 간단하게!
# def positive(x):
#     return x>0
# print(list(filter(positive, [1,-3,2,0,-5,6])))
#
# # lambda 를 사용하면 더 간편하게 코드 작성 가능!!!
# # lambda: 함수를 생성할 때 사용하는 예약어(def와 유사), 한줄로 간결하게 만들 때 사용!!!
# # lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
# print(list(filter(lambda x : x>0, [1,-3,2,0,-5,6])))
#
# # hex(x) 정수값==>16진수
# print(hex(16))
#
# # id(object) 객체를 입력받아 객체의 고유 주소 값(레퍼런스) 반환
# a = 3
# print(id(3))
# print(id(a))
# b = a
# print(id(b))
# # ==> 3, a, b 모두 같은 객체를 가리킴
# print(id(4))
#
# # int(x) ==> 정수값 반환
# # int(x,radix) ==> radix진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌
# print(int('11',2)) # 2진수로 표현된 11의 10진수 값 구하기!! ==> 3
# print(int('1A', 16)) # 16진수로 표현된 1A의 10진수 값! ==> 26
#
# # isinstance(object, class) 첫번째인수 : 인스턴스, 두번째인수: 클래스
# # 입력받은 인스턴스가 해당 클래스의 인스턴스인지 판단 ==> True or False
# class Person: pass
#
# a = Person()
# print(isinstance(a, Person)) # True
#
# b = 3
# print(isinstance(b, Person)) # False
#
# # map(f, iterable) : 함수(f), 반복가능한(iterable) 자료형
# # 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
# def two_times(numberList):
#     result = []
#     for number in numberList:
#         result.append(number*2)
#     return result
# print(two_times([1,2,3,4]))
# # map 사용해 바꿔보자!
# def two_times(x): return x*2
# print(list(map(two_times, [1,2,3,4])))
# # lambda 사용
# print(list(map(lambda x: x*2, [1,2,3,4])))
#
# # oct(x) : 정수 ==> 8진수
#
# # open 함수 ==> r, w, a 뒤에 b가 붙으면 바이너리 파일!
# # f = open("20200126_125308.jpg", "rb")
# # f.close()
#
# # ord(c) 문자의 아스키코드 값을 돌려주는 함수. chr(i) 와 반대!
# print(ord('a'), ord('0'))
#
# # pow(x,y) : x**y
#
# # round(number[, ndigits]) : 반올림!!!!, ndigits는 소수점 자릿수!
# print(round(4.6))
# print(round(5.6789, 2))
#
# # sorted(iterable) : 입력값을 정렬 후 리스트로 반환, 리스트의 sort함수는 정렬만 할 뿐 반환은 X
# print(sorted([3,2,1]))
#
# # sum(iterable)
# print(sum([1,2,3,4]))
# print(sum((4,5,6)))
#
# # zip(*iterable) 동일한 개수로 이루어진 자료형을 묶어주는 역할 ==> 예제 확인
# a = list(zip([1,2,3],[4,5,6]))
# print(a) # [(1, 4), (2, 5), (3, 6)]
# b = list(zip([1,2,3],[4,5,6],[7,8,9]))
# print(b)

############라이브러리
# # pickle 모듈 : 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
# # pickle 모듈 내 dump함수 사용 => 딕셔너리 객체인 data를 그대로 파일에 저장
# # pickle.load() 원래 있는 딕셔너리 객체 상태 그대로 불러옴
# import pickle
#
# profile_file = open("profile.pickle", 'wb') # b:binary
# profile = {"이름":"최비결", "나이":33, "취미":["음악감상", "서점가기", "영어유튜브보기"]}
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()
#
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
#
#
# f = open("text.txt", "wb")
# data = {1: 'python', 2: 'java'}
# pickle.dump(data, f)
# f.close()
#
# f = open("text.txt", "rb")
# data = pickle.load(f)
# print(data)


## os 모듈 : 환경변수, 디렉터리, 파일 등의 os자원을 제어할 수 있게 하는 모듈
# import os
# f = os.popen('dir')
# print(f.read())


# shutil 파일 복사해주는 모듈
# import shutil
# shutil.copy("새파일.txt", "abc.txt")


## glob 모듈
# 특정 디렉터리에 있는 파일을 알아야 할 때!!
# glob(pathname)
# import glob
# print(glob.glob("D:/DailyVy/JumpToPython/ch*"))
# ['D:/DailyVy/JumpToPython\\ch02.py', 'D:/DailyVy/JumpToPython\\ch04.py', 'D:/DailyVy/JumpToPython\\ch05.py']

# tempfile 파일 임시로 만들어서 사용할 때
# import tempfile
# filename = tempfile.mkstemp() # 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
# print(filename)
# f = tempfile.TemporaryFile() # 임시저장공간으로 사용할 파일 객체를 돌려줌
# f.close() # 생성한 임시파일이 자동으로 삭제됨

####### time 모듈 : 아주 유용!
# import time
# print(time.time()) # 현재 시간을 실수 형태로 돌려줌 1970년 1월 1일 0시 0분 0초 기준
# print(time.localtime()) # time.localtime(time.time()) 연도, 월, 일, 시, 분, 초, ....
# print(time.asctime()) # 위 localtime에 의해 반환된 튜플 형태의 값을 인수로 받아서 날짜, 시간을 알아보기 쉬운 형태로 돌려줌!!
# print(time.ctime()) # 항상 현재시간을 돌려줌
#
# a = time.strftime('%x', time.localtime()) # 현재 설정된 지역에 기반한 날짜 출력
# print(a)
# b = time.strftime('%c', time.localtime(time.time())) # 날짜와 시간을 출력함 ==> 책 예제와 달라
# print(b)
# c = time.strftime('%Z', time.localtime(time.time())) # 대한민국 표준시
# print(c)
# d = time.strftime('%X', time.localtime(time.time())) # 현재 설정된 지역에 기반한 시간 출력
# print(d)
# e = time.strftime('%Y', time.localtime(time.time())) # 연도출력
# print(e)
# f = time.strftime('%b', time.localtime(time.time())) # 달 줄임말
# print(f)
# g = time.strftime('%p', time.localtime(time.time())) # AM or PM
# print(g)

# time.sleep 루프 안에서 많이 사용. 일정한 시간 간격을 두고 루프 실행
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1) # 1초 간격으로 출력, 실수형태 가능


## calendar : 파이썬에서 달력 볼 수 있게 하는 모듈
# import calendar
# print(calendar.calendar(2022))
# # print(calendar.prcal(2022)) # 위와 같음
# print(calendar.prmonth(2022, 3)) # 2022년 3월 달력만
#
# # calendar.weekday(year, mon, day) # 요일정보 반환 - 월요일 0, 화요일 1,...
# print(calendar.weekday(2022, 3, 28)) # 월요일이니 0 반환
# # calendar.monthrange(year, mon) # 달의 1일이 무슨 요일인지, 그 달이 며칠까지 있는지 튜플로 반환
# print(calendar.monthrange(2022, 3)) # (1, 31) 화요일, 31일


## random : 난수를 발생시키는 모듈
# random, randint
# import random
# print(random.random()) # 0.0 ~ 1.0사이의 실수
# print(random.randint(1,10)) # 1과 10사이의 수 마지막 포함!!! 10포함!!!

# 함수 하나 만들기 random_pop.py
# random.choice(list) ==> 입력으로 받은 리스트에서 무작위로 하나를 선택해서 돌려준다.

# random.shuffle(list) ==> 리스트의 항목을 무작위로 섞고 싶을 때
# import random
# data = [1,2,3,4,5]
# random.shuffle(data)
# print(data)


## webbrowser  자신의 시스템에서 사용하는 기본 웹브라우저를 자동으로 실행하는 모듈
import webbrowser
# webbrowser.open("https://naver.com")
# webbrowser.open_new("https://google.com")

#################### 연습문제 ######################
# 1.
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self, val):
#         self.value += val
#         # return self.value
#
# class UpgradeCalculator(Calculator):
#     def minus(self, val):
#         self.value -= val
#
#
# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
# print(cal.value)
#

# 2. ==> 못품
# class Calculator:
#     def __init__(self):
#         self.value = 0
#     def add(self,val):
#         self.value += val
#
# class MaxLimitCalculator(Calculator):
#     def add(self, val):
#         self.value = self.value + val
#         if self.value >= 100:
#             return 100
#         else:
#             return self.value
#
# cal = MaxLimitCalculator()
# cal.add(50)
# print(cal.value)
# cal.add(60)
# print(cal.value)


# 3.
# 3-1.
print(all([1, 2, abs(-3)-3])) # False, False가 하나라도 있으면 False반환
print(chr(ord('a')) == 'a') # True. ord('a')는 a의 아스키코드 값 반환, chr은 아스키 코드 값의 문자 반환

# 4. filter와 lambda 이용하여 음수 모두 제거
# filter(함수이름, 반복가능한 자료형)
a = [1, -2, 3, -5, 8, -3]

# def positive(x):
#     return x > 0
# print(list(filter(positive, a)))

# lambda
print(list(filter(lambda x: x>0 , a)))
