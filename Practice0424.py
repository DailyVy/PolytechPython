def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

f1 = open("test.txt", "w")
f1.write("Life is too short")

f1.close()

f2 = open("test.txt", "r")
print(f2.read())

f2.close()

# user_input = input("저장할 내용을 입력하세요.")
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

with open('test.txt', 'w') as f:
    f.write("Life is too short\nYou need java")

f = open('test.txt', 'r')
body = f.read()
f.close()

print(body)

body = body.replace("java", "python")

f = open("test.txt", "w")
f.write(body)
f.close()

# f = open("D:/DailyVy/newfile.txt", 'w', encoding='utf8')
# for i in range(1,11):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
# f.close()

# f = open("D:/DailyVy/newfile.txt", "r", encoding="utf8")

# readline
# while True:
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close()

# readlines
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# read
# data = f.read()
# print(data)
# f.close()
#
# with open("newfile2.txt", "w") as f:
#     f.write("Life is too short, you need python")