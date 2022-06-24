#Chapter2. 자료형

# say = '"Python is very easy." he says'
# print(say)
# # multiline = "Life is too short\nYou need python"
# multiline = '''Life is too short
# You need python\f'''
# print(multiline)
# "print("="*50)
# print("My Program")
# print("="*50)"

# p.112 연습문제
# 1. 홍길동씨의 평균 점수 구하기
Hong = {'국어':80, '영어':75, '수학':55}
Grade = list(Hong.values())
print(f"홍길동의 평균 점수는 {(Grade[0]+Grade[1]+Grade[2])/len(Grade)}입니다.") # 소수점 표기는 :.4f 이런식으로

# 2. 자연수 13이 홀수인지 짝수인지 - 나머지 0 판별
num = 13
if num % 2 == 0:
    print(f'{num}은 짝수입니다.')
else:
    print(f'{num}은 홀수입니다.')

# 3. 홍길동씨의 주민등록번호 - 슬라이싱 이용하기
pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# 4. 주민등록번호 뒷자리의 맨 첫 번째 숫자는 성별을 나타낸다. 주민등록번호에서 성별을 나타내는 숫자를 출력해보자. - 인덱싱
pin = '881120-1068234'
print(pin[-7])
pin2 = pin.split('-') # ['881120','1068234']
print(pin2[1][0])

# 5. replace 함수 이용하여 a:b:c:d 를 a#b#c#d 로 바꾸기
a = "a:b:c:d"
b = a.replace(":","#") # 원본은 변경이 안되니 저장을 해주어야한다.
print(a, b, sep="\n")

# 6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자.
a = [1,3,5,4,2]
a.sort() # a.sort(reverse=True)를 이용하여 한문장으로 할 수 있다.
a.reverse()
print(a)

# 7.['Life', 'is', 'too', 'short']를 문자열로 바꾸기! - join 함수 이용
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)를 만들어보자. - 더하기 이용
a = (1,2,3)
a = a + (4,)
print(a)

# 9. 객관식

# 10. 딕셔너리 a 에서 'B'에 해당하는 값 추출하기 - 딕셔너리의 pop함수 사용
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # {'A':90, 'C':70} 출력 되도록
print(result) # 80 출력

# 11. a 리스트에서 중복 숫자 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

# 12. 서술형
