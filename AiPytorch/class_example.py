# pytorch 기반의 딥러닝 모델을 생성하는 github
# 일반적으로 class를 많이 사용해서 구현이 되어 있음
# class 상속과 관련해서 간단하게 실습
# class명(부모클래스), 부모클래스에 있는 것을 그대로 사용하기 위해 super
# 다중 상속.......

# 상속 : 컴퓨터와 노트북
class Computer:
    # __init__ 은 클래스가 객체를 생성할 때 제일 먼저 수행되는 코드
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def browse(self):
        print("web searching")

# Labtop class는 computer class를 상속받아 구현
class Labtop(Computer):
    def __init__(self, cpu, ram, battery):
        # 자식클래스에서 부모클래스의 내용을 그대로 사용하고 싶을 때
        # super().부모클래스의 메서드(인자)
        super().__init__(cpu, ram) # 부모 클래스의 init 메서드를 그대로 사용하겠다
        self.battery = battery

    def move(self):
        print("Labtop is portable")

# Rectangle 넓이 둘레 계산, square(정사각형)<==rectangle 상속
# cube 정육면체: 상속을 받아서 처리
# 상속에 상속을 간단하게 실습
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # 넓이 구하는 함수
    def area(self):
        return self.width * self.height
    # 둘레 구하는 함수
    def perimeter(self):
        return 2 * (self.width + self.height)

    def area_temp(self):
        print("inh ==> inh : 상속에 상속")
        return self.width * self.height

# 상속안받은 Square 클래스
class Square:
    def __init__(self, width):
        self.width = width
    # 넓이 구하는 함수
    def area(self):
        return self.width ** 2
    # 둘레 구하는 함수
    def perimeter(self):
        return 4 * (self.width)

# 상속받은 SquareInh 클래스

class SquareInh(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
    def area_temp(self):
        print("inh : 상속")
        return self.width ** 2


# super() vs super(SquareInh, self) 상속에 상속을 받은 것에 뭐...?
# 상속받은 메서드
# 상속에 상속 받은 메서드
class Cube(SquareInh):
    def surface_area(self):
        # SquareInh ==> Rect ==> area_tmp의 메서드
        sur_area = super(SquareInh, self).area_temp()
        # 정육면체의 넓이는 w*h*6
        return sur_area * 6
    def volumne(self):
        # SquareInh 클래스의 area_temp 메서드
        vol = super().area_temp() * self.width
        return vol

if __name__ == "__main__":
    # Rectangle, Square class example

    print("============Rectangle============")
    r = Rectangle(5, 3)
    print(r.width, r.height)
    print(r.area(), r.perimeter())

    print("============Square============")
    s = Square(3)
    print(s.area())
    print(s.perimeter())

    print("============SquareInh============")
    si = SquareInh(5)
    print(si.area())
    print(si.perimeter())

    print("============Cube============")
    c = Cube(2)
    print(c.surface_area())
    print(c.volumne())

