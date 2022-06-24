# 2022-03-14 AI 기초 프로그래밍
# 인덱싱과 슬라이싱
# a = "Life is too short, You need Python"
#
# str2 = "My name is bigyeol"
# lenStr2 = len(str2)
# print(lenStr2)
# print(str2[-7])
#
# str2[-7] = "B"
# str2[:-7] ==> "My name is "
# str2[lenStr2-6:] ==> "gyeol"
# str2 = str2[:-7] + "B" + str2[lenStr2-6:]
# print(str2)


# 객체에 대해서 잠깐만 보고 갑시다.
# a = 10
# b = 10
# c = 11
#
# print(id(a), id(b), id(c), id(a+b+c)) # id란 메모리 주소를 가져오는 것
# a와 b는 메모리 주소가 같지만 a+b 는 새로운 객체를 생성하여 새로운 메모리 공간에 할당이 된다.

# 문자열 포매팅
# print("%10s"%"hello I am bigyeol")
#
# number = 10
# day = 'three'
# str1 = 'I ate %d apples.\nSo I was sick for %s days.' % (number, day)
# print(str1)
# str1 = f'I ate {number} appels.\nSo I was sick for {day} days.'
# print(str1)
#
# str1 = '%4s\n%4s\n%4s\n%4s\n%4s' % ('a', 'ab', 'abc', 'abcd','abcde') # 할당된 공간을 넘어가면 그냥 그대로 출력하네
# print(str1)
#
# str1 = '%-10sjane' % ('hi')
# print(str1, len(str1))
#
# print(f"{3.14159265:0.4f}")
# str2 = f"{3.14159265:10.3f}"
# print(str2, len(str2))
#
# print(f'{3.1415:=^10.3}\n')
#
# # 문자열 관련 함수
#
# str1 = """
# It is the first time that a South Korea-made TV show has won a prize at the Critics Choice,
# given by a group of 500 film and TV broadcast critics in North America.
# On the film side, Bong Joon-ho's Oscar-winning satire "Parasite" grabbed two Critics Choice titles,
# including best foreign language film and best direction in 2020.
# """
#
# cnt_a = str1.count('Critics')
# print(str1.find("time"), str1.find('w'), str1.index('h'), str1.find('Korea'))
# print(str1.upper())
# print(str1.lower())
# print(str1)
#
# str1 = "123456789"
# print(",".join(str1))
# print('.'.join(str1))
# print('-'.join(str1))
#
# str_list = "Life is too short"
# print(str_list.replace("short", "long"))
# print(str_list.replace("Life", "Sleeping time"))
# print(str_list)
#
# str_list = str_list.split()
# print(str_list, type(str_list))
#
# str_list = "****".join(str_list)
# print(str_list, type(str_list))


# ##########################################숙제####################################################
# # 데이터 변경하기
# # 넓이가 100 이상인 vehicle 의 경우에는 vehicle -> truck으로 변경, x, y, width, height


# List를 만들어 보자
list1 = [1, 2, 0.1, "string"]
print(f'{list1}')
# 평수, 방 갯수, [방#1, 방#2, 방#3,], 층수, 가격
list2 = [30, 3, ["study", "bed", "clothes"],
         "10층", "3억"]
print(list2)
# list. indexing, slicing
str2 = f'My house area is {list2[0]:"^9.2f},\n' \
       f'there are {len(list2[-3])} rooms.\n' \
       f'I like the {list2[-3][1]}room.\n'
print(str2)
# list +, *, list 길이 구하기. 등 해볼 것.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2 # [1, 2, 3, 4, 5, 6]
print(list3)
list4 = list1 * 3 # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(list4, len(list4)) # , 9