# 다음 리스트를 -1 ~ 1 값으로 바꿔보자(정규화)
test = [-6, -2, 2, 1, 3, 4]

# 1. 절대값이 제일 큰 걸로 나누기
test_abs = list(map(lambda x: abs(x), test))
print(test_abs) # [6, 2, 2, 1, 3, 4]
print(max(test_abs)) #
test_abs_norm = list(map(lambda x: x / max(test_abs), test))
print(test_abs_norm)

# 2. min과 max의 차이로 나누기
divider = max(test) - min(test)
print(divider)
test_minMax_norm = list(map(lambda x: x / divider, test))
print(test_minMax_norm)