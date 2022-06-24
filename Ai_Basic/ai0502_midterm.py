# 중간고사 split, pop 풀이

def str_split(input_str):
    rtn_list = [] # 리턴할 리스트
    # " " 문자를 카운팅하는 방법으로 문제를 접근
    cnt = input_str.count((" ")) # 공백 문자가 몇 개 인지 카운트, qna:왜 소괄호를 왜 두개나 해줬지?
    for _ in range(cnt):
        # find: 해당되는 문자의 index값을 반환하는 내장함수
        # "abc d ef g"
        cmp_value = input_str[:input_str.find((" "))]
        if (cmp_value and cmp_value != " "):
            rtn_list.append(cmp_value)
        input_str = input_str[input_str.find((" ")) + 1:]
    rtn_list.append(input_str) # 마지막 문자가 뒤에 공백이 없을 경우 그냥 append해주면 된다.
    return rtn_list

# inpl_pop(): 제일 마지막 값이 나오기를 기대
# inpl_pop(index): 특정 인덱스에 해당하는 원소 값 반환
# 현재 ai0502_midterm.py 파일에서 제일 함수 내에 있지 않는 변수는 전역 변수
# input_list는 전역변수이고 다른 함수에서 모두 접근가능하다.
# global: global 을 명시하지 않으면 함수내에서 read는 되지만
# write(수정, 해당 변수의 내용을 조작)은 불가능

input_list = [1, 2, 3, 5, 6, 9]

def impl_pop(index=-1): # 아무것도 지정안했을 때는 파라미터를 default로
    # print(input_list[1])
    global input_list
    if (index >= len(input_list)):
        return -1
    # 마지막 인덱스 처리
    if (index == -1):
        rtn_value = input_list[index]
        input_list = input_list[:-1]
    # 맨 처음 인덱스 처리
    elif (index == 0):
        rtn_value = input_list[index]
        input_list = input_list[index+1:]
    # 중간 인덱스 처리
    else:
        rtn_value = input_list[index]
        input_list = input_list[:index] + input_list[index+1:]
    return rtn_value

def impl_push():
    # input_list = input_list[:3] # input_list 로컬변수 취급
    input_list_0 = input_list[:3] # input_list 는 전역변수수


print(impl_pop(0))
# sort_num = [1, 8, 10, 99, 2, ..., 0]