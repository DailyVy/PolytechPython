# 04/25 Midterm 문제
# split 및 pop 구현

def str_split(input_str):
    blk = " " # blank
    input_str = input_str + blk # 마지막에 공백추가, 공백을 기준으로 나눠 줄 것
    index = 0
    result = [] # 리턴할 값은 리스트로
    for i in range(len(input_str)):
        if input_str[i] == blk:
            data = input_str[index:i].strip() # 공백 제거를 위한 데이터 정렬
            if data == "":
                continue
            result.append(data)
            index = i
    return result



str_test = "abc          def     ghij klmn    opq     "
print(str_split(str_test))
str_test = "abc d"
print(str_split(str_test))
str_test = "abc d e f g"
print(str_split(str_test))

input_list = [1,2,3,5,6,9]

def impl_pop(*index):
    global input_list
    if index == ():
        pop_num = input_list[-1]
        input_list = input_list[:-1] # assign을 해주면서 local 변수가 됨
        # del input_list[-1] # assign안하고 이거 써주면 전역변수처럼 활용
        return pop_num
    elif int(index[0]) >= 0 and int(index[0]) < len(input_list):
        index = int(index[0])
        pop_num = input_list[index]
        input_list = input_list[:index] + input_list[index+1:]
        return pop_num
    else:
        return -1


print(impl_pop(), input_list)
print(impl_pop(3), input_list)
print(impl_pop(5), input_list)
print(impl_pop(), input_list)
print(impl_pop(1), input_list)
print(impl_pop(2), input_list)

