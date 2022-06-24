import random

# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number) # index가 number

def random_pop(data):
    number = random.choice(data) # random.choice는 입력받은 리스트에서 무작위로 하나 택하여 돌려준다.
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data: print(random_pop(data))
