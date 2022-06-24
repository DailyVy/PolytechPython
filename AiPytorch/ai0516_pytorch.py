import time
import torch
from torch import cuda

# GPU 사용 가능 => True, GPU 사용 불가 => False
# print(cuda.is_available())
# 사용 가능 GPU 개수 체크
# print(cuda.device_count()) # 1

# torch 버전 체크
# print(torch.__version__) # 1.11.0

###### 4교시 ######
# 1D ~ ND 까지 실습

# 1D : Vector
# 텐서를 생성 : torch.FloatTensor() <- Dimension 입력(like numpy)
# 지난 주의 평균 온도를 벡터에 저장 => 리스트처럼 쓰면 됨
temp1D = torch.FloatTensor(
    [15, 17.2, 19.2, 22.3, 20.2, 19, 16]
)
print(temp1D.size(), temp1D.dim()) # torch.Size([7]), 1(dimension이 1차다)

# 리스트처럼 인덱싱, 슬라이싱 가능!!!
print(f'월, 화 평균온도는: {temp1D[0]}℃, {temp1D[1]:.2f}℃ 입니다.')
print(f'화~목 : {temp1D[1:4]}℃ 입니다.')

# 2D : Matrix(2 Dimensional Tensor)
# 정의 : [ [], [] ] ==> 리스트 내 리스트
temp2D = torch.FloatTensor(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
)
# 원래는 위처럼 표현 안하고 한줄에 표현을 한다.
# temp2D = torch.FloatTensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) 이렇게!
print(temp2D.size(), temp2D.dim()) # torch.Size([4, 3]) 2

# slicing (Matrix : 행렬(row, column), 첫번째가 row, 두번째가 column)
# -> 판다스하고 비슷할듯
# 첫번째 차원의 모든 것과 두번째 차원의 두번째 것
# 모든 행의 두번째 것
print(temp2D[:, 1])
# row의 3번째 요소들과, col의 모든 것
print(temp2D[2, :])
# 4x3 행렬의 [5, 6], [8, 9] 가지고 오기
print(temp2D[1:3, 1:])



## 보스턴 주택 가격 (from sklearn.datasets) ==> 이거 1.2버전부터 지워지나봄...
from sklearn.datasets import load_boston
# load_boston 메서드의 반환형이 numpy의 array
boston = load_boston()
print(boston.data)

# numpy to pytorch. ==> 2D 데이터를 보기 위해 torch에서 제공하는 메서드를 사용
boston_tensor = torch.from_numpy(boston.data)
print(boston_tensor.size(), boston_tensor.dim()) # torch.Size([506, 13]) 2

# 인덱스 기준으로 1, 11까지의 feature(cols)와 2개의 row를 가지고 오고 싶을 때
# 모든 features와 2개의 row
print(boston_tensor[[1,2], 1:12])