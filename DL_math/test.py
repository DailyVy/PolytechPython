import torch.cuda
from torch import cuda
use_gpu = cuda.is_available()
print(use_gpu, torch.cuda.device_count())