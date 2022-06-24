# String Operation : +, *
# + : Concatenation
# * : 반복 연산

# str1 = "Hi Everyone"
# str2 = "My name is ..."
# str3 = "****************"
#
# print(f'{str3*10}\n{str1 + str2},\n'
#       f'This Block is comment block\n'\
#       f'{str3*10}')
#
# print(f'{str3*10}\n{str1 , str2},\n'
#       f'This Block is comment block\n'\
#       f'{str3*10}')


# 인덱싱과 슬라이싱
str2 = "20220308Sunny"
print('Today weather is '+ '\"' +str2[-5:] + '\"')
print('오늘 날짜는 ' + str2[:4] + '년 ' + str2[4:6] + '월 ' + str2[6:8] + '일 ')
print(f'오늘 날짜는 {str2[:4]}년 {str2[4:6]}월 {str2[6:8]}일')
print(f'Today weather is {str2[-5:]}, and date is {str2[:8]}')