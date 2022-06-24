# import pandas as pd
# import numpy as np
#
# np_arr = np.array(range(5))
# print(np_arr, type(np_arr))
#
# array_4 = np.array(range(5))
# print(array_4)
#
# arr = np.array([0,1,2,3,4], dtype=float)
# print(arr, arr.dtype)
# print(arr.astype(int))
#
# list_1 = [0, 1, 2, 3]
# arr = np.array(list_1)
# print(arr)
# print(arr.ndim)
# print(arr.shape)
#
# list_2 = [[0,1,2],[3,4,5]]
# arr = np.array(list_2)
# print(arr)
# print(arr.ndim)
# print(arr.shape)
#
# arr = np.array([0,1,2,3,4,5])
# print(f'arr.shape: {arr.shape}') # (6,)
# print(f'배열 요소의 수: {arr.size}') # 6
# print(f'배열의 길이: {len(arr)}') # 6
#
# data = pd.Series([1,2,3,4])
# print(data)
# print(type(data))
# print(data.values)
# print(type(data.values))
#
# data = pd.Series([1,2,3,4], dtype="float")
# print(data.dtype)


class maxMachine:
    def __init__(self):
        self.numbers = []

    def addNumber(self, n):
        self.numbers.append(n)

    def removeNumber(self, n): # 간단하게 remove 메서드를 사용해주면 되는 거였음
        if n in self.numbers:
            del self.numbers[self.numbers.index(n)]
        else:
            pass

    def getMax(self):
        return max(self.numbers)

# myMachine = maxMachine()
# myMachine.addNumber(2)

def main():
    myMachine = maxMachine()

    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myMachine.addNumber(1)
    myMachine.addNumber(2)
    myMachine.addNumber(3)
    myMachine.addNumber(2)

    print(myMachine.getMax()) # 3

    myMachine.removeNumber(3) # 3없어지고 [1,2,2]

    print(myMachine.getMax()) # 2

    myMachine.removeNumber(2) # [1,2]

    print(myMachine.getMax()) # 2


if __name__ == "__main__":
    main()
