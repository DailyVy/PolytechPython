# 2. DB에는 총 101개의 문서가 존재하고, DB에 저장된 문서로 모두 Vectorization을 수행하였다.
# 첫번재 문서의 Vectorization 결과는 다음과 같앗다.
# vec_doc_1 = [0.2, 0.4, 0.02, 0.1, 0.9, 0.8]
# 100개의 문서 중 첫번째 문서와 가자 ㅇ유사한 문서를 검색하는 코드를 작성하ㅗㄱ, "MML_Exam_2.py"로 저장하여 제출하시오.

## 조건 1: 100 x 6 array를 만들고 np.random.seed(1234)로 랜덤값이 고정으로 출력되게 셋팅 후,
##  np.random.random() 함수를 사용하여 각 컬러므이 갑승ㄹ 랜덤하게 생성
## 조건 2: Inner Production을 사용하여 가장 유사도가 높은 문서(row)를 선택할 것
##  (Inner Production을 이요하는 부분은 함수로 만들 것,
#    출력: (인덱스, 값)) *** 값을 소수점 3째자리에서 반올림 (0.2456 ==> 0.25)



import numpy as np

def inner_product(vectors, in_vec):
    max = (0, 0)
    maxIndex = max[0]
    maxValue = max[1]

    for i in range(len(vectors)):
        sumVal = 0
        print(vectors[i])
        for j in range(len(vectors[i])):
            tempVal = vectors[i][j] * in_vec[j]
            sumVal += tempVal
            # print(in_vec[j])
            if sumVal >= maxValue:
                maxValue = sumVal
                maxIndex = i

    max = (maxIndex, f'{round(maxValue, 2):.2f}')
    return max

if __name__ == "__main__":
    np.random.seed(1234)
    doc_vec = np.zeros((100, 6))

    print(doc_vec.shape)

    for i in range(100):
        for j in range(6):
            doc_vec[i][j] = np.random.random()

    print(doc_vec)

    vec_doc_1 = [0.2, 0.4, 0.02, 0.1, 0.9, 0.8]

    print(inner_product(doc_vec, vec_doc_1))