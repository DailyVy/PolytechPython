# 1부터 100까지 소수가 몇 개 있는지 ?

while(1):
    testNum = input("양의 정수를 입력하십시오> ")
    if (testNum.isdigit()): # istype()이 True 라도 데이터타입은 str이므로 int로 변환 후에 진행
        testNum = int(testNum)
        break

Num_list = [int(i) for i in range(1,testNum+1)] # 리스트 생성 : 1 ~ testNum에 입력된 숫자
print(Num_list)

prime_num = []

for num in Num_list:
    if num > 3:
        for i in range(2, num):
            if i + 1 == num:
                prime_num.append(num)
            elif num % i == 0:
                continue
    elif num == 2 or 3:
        prime_num.append(num)
print(prime_num)