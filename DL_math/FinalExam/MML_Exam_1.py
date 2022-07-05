################## 2022.07.05 Final Exam ###############

# 1. Matrix multiplication 코드를 작성하고, "MML_Exam_1.py"로 저장하여 제출하시오.
## 조건 1. 라이브러리를 사용하지 말고 직접 구현할 것
## 조건 2. n x m 매트릭스 생성하고, n x m * m x n = n x n 의 결과가 나오도록 입력 데이터 생성할 것
##  (입력 데이터 생성하는 부분 함수로 작성), n, m : >= 3 and <= 20,
##  * matrix multiplication(Not Element-wise multiplication)

# 코드 제출 전 Octave Online 을 통하여 3x3 matrix 곱하기 결과 먼저 확인해 볼 것

import numpy as np

np.random.seed(8)


# matrix는 10미만의 숫자로 구성되게 해야지..
def gen_data(mat, n, m):
    for i in range(n):
        for j in range(m):
            mat[i][j] = np.random.randint(10)
    return mat

def matmul(mat1, mat2, result):
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            sumVal = 0
            for k in range(len(mat2)):
                sumVal += mat1[i][k] * mat2[k][j]
            result[i][j] = sumVal

    return result

if __name__ == "__main__":

    "..."

    n = np.random.randint(3, 20)
    m = np.random.randint(3, 20)

    print(n, m)

    mat1 = np.zeros((n, m))
    mat2 = np.zeros((m, n))

    # print(mat1)
    # print(mat2)

    result = np.zeros((n, n))

    print(result)

    mat1 = gen_data(mat1, n, m)
    mat2 = gen_data(mat2, m, n)

    print(mat1)
    print(mat2)

    result = matmul(mat1, mat2, result)

    print(result, result.shape)