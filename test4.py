# a = [1,2,3,4,5]
# a.pop(2) # index pop
# print(a)

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f'이름:{self.name}, 나이:{self.age}, 성별:{self.sex}')

# areum = Human("조아름", 25, "여자")
# print(areum.name)
# print(areum.age)
# print(areum.sex)
# areum.who() # Human.who(areum)

areum = Human("모름", 0, "모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()
