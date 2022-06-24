# 나뭉's Code

input_list = [1,2,3,5,6,9]

def impl_pop(index = False):
    if (index == False):
        element = input_list[-1]
        del input_list[-1]
        return element

    elif (index < 0) | (index >= len(input_list)):
        return -1

    else:
        element = input_list[index]
        del input_list[index]
        return element

print(impl_pop(), input_list)
print(impl_pop(3), input_list)