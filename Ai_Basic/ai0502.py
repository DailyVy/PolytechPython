# class FourCal:
#     def __init__(self, first, second): # 생성자 구현
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


# class를 만들기 위해서는 class 클래스이름:
# 상속의 경우 class 클래스이름(상속받을 클래스명):
class FourCalc:
    # set_data라는 메서드 구현 (2개의 객체 변수를 셋팅)
    # 기본적으로 사칙연산을 위해 2개의 값이 필요
    # 생성자 : 객체를 생성할 대 Default로 무엇인가를 하고 싶을 때
    # __init__ 으로 정해져 있음
    def __init__(self, in_0, in_1): # 이렇게 해도 될까요? 내가 사용할 객체변수는 그냥 내가 지정할 뿐
        self.first = in_0
        self.second = in_1
    # def set_data(self, first, second):
    #     self.first = first # self.first 는 객체변수, first는 메서드의 parameter
    #     self.second = second
    # 더하기, 빼기, 곱하기, 나누기 메서드 작성
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

calc_0 = FourCalc(4, 2)
print(calc_0.add())

# FourCalc 클래스를 상속받아 MoreCalc 클래스를 하나 만들자
class MoreCalc(FourCalc):
    def __init__(self, first, second, third=1): # 부모클래스에도 __init__ 있었음! ==> super를 사용해보자
        # 객체를 생성할 때,
        # a = MoreCalc(1, 2, 3)
        # a = MoreCalc(1, 2) 둘 다 상관이 없다.
        # super() : 부모 클래스에 있는 메서드를 그대로 사용 가능함
        # self.first = first
        # self.second = second
        super().__init__(first,second) # 이 코드 자체가 위의 두 줄의 코드와 같다.
        self.third = third

    # FourCalc 상속을 받았기 때문에 사칙연산 모두 가능
    # FourCalc의 메서드에는 add, sub, mul, div
    # 새로운 메서드를 추가해봅시다.
    def pow(self):
        result = self.first ** self.second
        return result
    # overriding: 상속받은 클래스의 메서드를 수정할 수 있음
    # 오버로딩과 오버라이딩의 차이점은 오세진 교수님께 잘 배우세요.... 파이썬은 오버로딩... 안되나바...
    def add(self): # 세 개의 숫자를 더해서 반환함
        return super().add() + self.third # super().add()는 (self.first + self.second)리턴값
    # div 메서드를 오버라이딩 해보자
    # 기존 div에서는 ZeroDivde에 대한 처리가 없었음
    # 오버라이딩하는 메서드에서는 0으로 나눌 경우 0값을 리턴하는 것으로 작성
    def div(self):
        if self.second == 0:
            return 0
        else:
            return super().div()

# moreCalc_0 = MoreCalc(10, 0, 2)
# print(moreCalc_0.add())
# print(moreCalc_0.div())

try:
    a = [1, 2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)