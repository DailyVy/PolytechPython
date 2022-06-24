# 시간 측정
import time

start_time = time.time()
array = list(range(1, 10000))
for i in array:
    for j in array:
        tmp = i * j
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력 => time: 9.12399673461914




# N^2 정렬 (N = 100,000) ==> 분 단위가 나올 수도
from random import randint

# list 생성 및 랜덤 값 append
arr= []
arr_lib = []
for _ in range(100000):
    arr.append(randint(1, 10000)) # 1~10000사이의 랜덤한 함수
    arr_lib.append(randint(1, 10000))
start_time = time.time()

# sort
# for i in range(len(arr)):
#     min_idx = 1
#     for j in range(i+1, len(arr)):
#         if arr[min_idx] > arr[j]:
#             min_idx = j
#     arr[i], arr[min_idx] = arr[min_idx], arr[i]
# print(arr[0:10])

# list 내부 함수 sort()
arr_lib.sort()
end_time = time.time()
# print(f'선택 정렬 성능 측정(시간): {(end_time - start_time):.4f}') # 선택 정렬 성능 측정(시간): 743.2954
print(arr_lib[0:10]) # [3529, 8977, 1243, 1547, 6052, 9893, 4422, 2043, 7524, 3177]
print(f'기본 정렬 라이브러리 사용 측정(시간): {(end_time - start_time):.4f}') # 기본 정렬 라이브러리 사용 측정(시간): 0.0170
