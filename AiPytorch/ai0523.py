from sklearn.datasets import load_boston

import numpy as np
import torch
from PIL import Image

## 1교시

# # 3D Tensor
# # Color Image : 3D (w, h, channel)
# # channel : R, G, B (종류는 많다.. YUV, LUV, ... )
# # 1 channel Image : Greyscale Image(흑백영상)
# # batch-size * 1 channel Image ==> 3D
#
# # from PIL import Image
# dog = np.array(Image.open('dog.4.jpg').resize((224, 224)))  # resize(224, 224) 하면 안됨 괄호 두개!
# # numpy to tensor
# dog_tensor = torch.from_numpy(dog)
# # 3D Tensor print
# print(f'size and dimension of the dog color image: '
#       f'{dog_tensor.size()}, {dog_tensor.dim()}')
# # 4D Tensor : color images 가 여러 개 들어가 있는 데이터셋 자체가 4D tensor
# data_path = "./dataset_CatDog/training_set/dogs/"
#
# # 특정 문자를 포함한 모든 것을 가지고 오기 위해서 glob
# from glob import glob
# dogs = glob(data_path + "*.jpg")
# # glob 결과는 리스트로 반환
# print(dogs[:2])
#
# # 64 x 224 x 224 x 3 : 일단 이미지 64개만 가지고 오자
# img_list = []
# for dog in dogs[:64]:
#     # img_list.append(dog)
#     img_list.append(np.array(Image.open(dog).resize((224, 224))))
#
# # => 이거 리스트 내포 형식으로 만들어봅시다.
# img_list2 = [np.array(Image.open(dog).resize((224, 224))) for dog in dogs[:64]]
#
# # 한번 찍어보자
# print(img_list[0])
# # print(img_list2[0])
#
# # 최종적으로 np.array 로 4D 형식으로.. 바꿔주기 위해서 여태까지 작업한 것임
# dogs_imgs = np.array(img_list)
# print(dogs_imgs.size, dogs_imgs.shape, dogs_imgs.ndim) # 9633792 (64, 224, 224, 3) 4 -> size = 64*224*224*3
# # numpy to tensor
# dogs_tensor = torch.from_numpy(dogs_imgs)
# print(dogs_tensor.size(), dogs_tensor.dim()) # torch.Size([64, 224, 224, 3]) 4
# # numpy 를 쓰는 이유는 [[]] 를 많이 쓰는데 이걸 numpy 가 잘 지원하기 때문이당


## 2교시

# pytorch 에서 자주 사용되는 함수
# 내가 사용하지 않더라도 함수가 어떤 의미인지 알고는 있자!

# 1. broadcasting
#  Matrix A, B 가 있으면 덧셈 뺄셈 할 때는 두 Matrix의 크기가 같아야 함
#  행렬의 곱 : A Matrix의 col 크기와 B Matrix의 Row 크기가 같아야 함.
#  파이토치에서는 자동으로 크기를 맞추어서 연산을 수행 : 브로드캐스팅 연산

# 1 x 2 행렬 : [ [ 1, 2 ] ] : 2D 형태로 표현
m1 = torch.FloatTensor([[3, 3]])
m2 = torch.FloatTensor([[2, 2]])
print(m1 + m2)

# 이번엔 크기가 다른 걸로 해봅시다
#  m2 를 1 x 1 벡터(실수) 정의, m1(1 x 2) + m2 (1 x 2) 를 해보자고
m2 = torch.FloatTensor([2])
#  m1 = [[3, 3]], m2 = [2] ==> (broadcasting) m2 = [[2, 2]] 로 자동으로 동일한 값으로 확장한다.
print(m1 + m2)  # 앞의 결과와 같다.

# m1(1x2), m2(2x1) matrix
# m1 + m2 를 한다면..??? ==> broadcasting 을 통해서 m1, m2 모두 2x2로 확장해서 계산
"""
m1 = [
    [1, 2],
    [1, 2]
]
m2 = [
    [3, 3],
    [4, 4]
]
"""
m1 = torch.FloatTensor([[1, 2]])
m2 = torch.FloatTensor([[3], [4]])
print(m1.shape, m2.shape)
print(m1 + m2)

# 2. in-place 연산 (덮어쓰기 연산 : pandas 할 때 많이 했어)
#  in-place : _(언더바) 사용
a = torch.FloatTensor([[1, 2], [3, 4]])
# b = torch.FloatTensor([[1, 2], [3, 4]])

# broadcasting + in-place
print("확인해봅시당")
print(f'{a.add_(2)}\n{a}')  # add_(2) 하면 broadcasting(2=> 2x2인 매트릭스가 2로 차있음) 후 in-place 연산 수행

# 3. matrix 곱, element-wise 곱

# 3-1) Matrix multiplication : tensor.matmul(tensor) -> e.g)m1.matmul(m2)
# 3-2) element-wise multiplication (tensor * tensor): m1 * m2 or m1.mul(m2)

# m1 : 2x2 matrix, m2 : 2x1 matrix ==> matmul : 2x1 matrix
m1 = torch.FloatTensor([[1, 2], [3, 4]])  # 2x2
m2 = torch.FloatTensor([[1], [2]])  # 2x1
print(m1.shape, m2.shape, m1.matmul(m2))

# element-wise 곱 : m1 * m2 크기가 다르기 때문에 원래는 수행 불가
#  계산을 하면 알아서 크기를 맞추어서 계산 (broadcasting)
print(m1 * m2)
print(m1.mul(m2))
"""
[1 2    [1 1
 3 4]    2 2]
"""

# gpu setting 확인
from torch import cuda

use_gpu = cuda.is_available()
print(use_gpu, torch.cuda.device_count())  # gpu 개수 확인

## 3교시

# import time
#
# a = torch.rand(20000, 20000)
# b = torch.rand(20000, 20000)
# start_time = time.time()
#
# if use_gpu:
#     a = a.cuda() # a 에다가 cuda를 쓰겠다고 하는 것
#     b = b.cuda()
#     a.matmul(b)
#     # start time, end time 찍고 빼면 그게 연산처리 시간
#
# end_time = time.time()
# print(end_time - start_time)

# 4. 평균 : tensor.mean()
t = torch.FloatTensor([[1, 2], [3, 4]])
print(t.mean())  # (1+2+3+4)/4

# cf) pandas에서 sum(axis=0): 기본적으로 0: row, 1: column
#  == 연산의 기본이 column 단위로 하는 연산이라면 : 0: column, 1: row

# torch, dim을 기준으로 연산이 가능
# dim 0, 1 이냐에 따라 연산을 할 수 있음
# dim = 0 : 첫번째 차원을 제거한다는 의미
#  matrix에서(2D: row, column)에서 첫번째 차원은 row, 두번째 차원은 column
# row를 배제하고 계산하고 싶을 때 (dim=0 옵션 적용)
#  0: 컬럼별로 계산, 1: row별로 계산
print(t.mean(dim=0))  # column끼리 계산 (1,3)의 평균, (2,4)의 평균
print(t.mean(dim=1))  # row끼리 계산 (1,2)의 평균, (3,4)의 평균
print(t.sum(dim=0))
print(t.sum(dim=1))

# 5. max, argmax
#  max : Tensor들의 원소 값 중에 제일 큰 값을 반환
#  argmax : Tensor들의 원소 값 중에 제일 큰 값의 "인덱스"를 반환
""" 
t = [1  2
     3  4]
0:1, 1:2, 2:3, 3:4
=> 일렬로 만든 다음에 출력
"""
print(t.max())
print(t.argmax())
# 쉬는 시간에 t.max(dim=0), t.argmax(dim=1) 내가 예상한 숫자가 나오는 지 확인..!
temp = torch.FloatTensor(
    [[3, 1, 2, 7, 5],
     [10, 2, 3, 1, 9],
     [4, 9, 2, 1, 3]])
print("=============")
print(temp.max(dim=0))
print("=============")
print(temp.argmax(dim=1))
print("=============")

# 6. view : 원소의 수(갯수)를 유지하면서 tensor의 shape을 변경
# numpy의 reshape 함수와 동일한 기능
# tensor의 크기, 차수를 변경하지만 총 원소의 갯수는 변화가 없다.
# 2x2x3 tensor 생성
t1 = torch.FloatTensor(
    [[[0, 1, 2],
      [3, 4, 5]],
     [[6, 7, 8],
      [9, 10, 11]]]
)
print(t.shape, t.dim())

# 3D --> 2D 텐서로 변경
t2 = t1.view([-1, 3])
# -1 : all(전체를 의미)
# 3 : 지정해준 col의 갯수
# 총 원소의 갯수는 12(2x2x3)
#  2d는 row와 col만 존재
#  row : -1는 col 갯수에 따라 row의 형태는 알아서 계산해달라는 의미
#  col은 3으로 지정했으니 row가 가질 수 있는 경우의 수는 4밖에 없다.(총 원소의 갯수는 12라서)
print(t2, t2.shape)

## 4교시
# 3차원 Tensor의 크기만 변경
# 2x2x3 ==> ?(batch-size) x 1 x 3 ==> t.view([-1, 1, 3])
# ? 값은 : 4 (2x2x3=12, ?x1x3=12 ==> ?==4)

# 7. squeeze <--> unsqueeze
# squeeze
# 3x1 matrix를 원소가 3개인 벡터형태로 변경
t = torch.FloatTensor([[0], [1], [2]])
t_sq = t.squeeze() # squeeze를 하면 1인 차원을 제거
print(t, t_sq, t.shape, t_sq.shape)

# unsqueeze
t = torch.FloatTensor([0, 1, 2]) # 벡터
t_row = t.unsqueeze(dim=0) # 0 : row에 1추가 (1x3), 1: col에 1추가 (3x1)
t_col = t.unsqueeze(dim=1) # 0 : row에 1추가 (1x3), 1: col에 1추가 (3x1)
print(t.shape, t_row.shape, t_col.shape)
print(t, t_row, t_col)

# 8. concatenate : 두 개의 텐서를 연결해서 하나의 텐서를 생성
# torch.cat 을 사용 (2x2 텐서를 생성하고 연결)
x = torch.FloatTensor([[1, 2], [3, 4]])
y = torch.FloatTensor([[5, 6], [7, 8]])

t_row = torch.cat([x, y], dim=0) # row 쪽으로 연결
t_col = torch.cat([x, y], dim=1) # column 쪽으로 연결
print(t_row, t_row.shape, t_col, t_col.shape)