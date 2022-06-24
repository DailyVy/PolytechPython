### 1교시
# 제어문 - if
# print(8 in [1,2,3,4,5]) # False
# score = 20
# message = "Success" if score >= 60 else "Failure"
# print(message)

money = 3000
if money > 3000:
    print("Take Taxi")
else:
    print("Take Bus")

sum_var = 0
for i in range(10):
    sum_var += i
print(sum_var)

# 조건문 not

sum_var = 0
if not sum_var:  # not False 즉 True
    print(sum_var)

# 조건문 or
# money = 3000
card = True
if money > 3000 or card:  # front condition(False) or rear condition(True)
    print("Take Taxi")
else:
    pass  # 아무 것도 하지 않겠다.

# in: for 문에 많이 사용됨
# if문에서도 종종 사용되므로 이해 필요 (~ 가 있는가?)
list_var = [1, 2, 3, 4, 5]
if 8 in list_var:
    print("8 is in the list")
else:
    print("Can't find input number")

# if else statement 자체를 한 줄로 표현
score = 20

msg = "Success" if score >= 60 else "Failure"
print(msg)

if not 'a' in 'Hello, How are you':
    print("Sorry, I can't find 'a'")
else:
    print("a is in the string")

if "Python" in ("Java","Python","Ruby"):
    print("I like Python!")
else: pass

if 'a' in 'Hello, how are you' or 'b' in 'World':
    print("a or b")
else:
    print("Nope")

if 1 in (1,2,3) and 2 in [3,4,5]:
    print("Both")
else:
    print("Neither")