import time
from torch import cuda
import torch

print(torch.__version__)
print(cuda.is_available())
print(cuda.device_count())


# 1D : Vector
# 텐서를 생성 : torch.FloatTensor() <- Dimension 입력(numpy 처럼)
# 지난 주의 평균 온도를 벡터에 저장 ==> 리스트처럼 인덱싱, 슬라이싱 가능
temp1D = torch.FloatTensor(
    [15, 17, 19.2, 22.3, 20, 19, 16]
)
print(temp1D.size(), temp1D.dim()) # torch.Size([7]) 1

# indexing, slicing
print(f'월, 화 평균 온도는 : {temp1D[0]}, {temp1D[1]}')
print(f'화 ~ 목 평균온도는 : {temp1D[1:4]}')

# 2D : Matrix
# [ [], [] ]
temp2D = torch.FloatTensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(temp2D.size(), temp2D.dim()) # torch.Size([4, 3]) 2


