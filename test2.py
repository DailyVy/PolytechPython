data_bundle = "vehicle 0 0 150 50"

temp = len(data_bundle)
# print(temp)
count = 0 # 뒤에서부터 1. height, 2. width, 3. y, 4. x ==> 우리는 width를 찾아야함 즉, count가 2 일때

# 뒤에서 부터 data_bundle 내에서 공백 찾기 ==> width는 뒤에서 첫번째 공백과 두번재 공백 사이 존재
for j in range(len(data_bundle), 0, -1):  # 17 ~ 1 까지
    # print(j)
    if data_bundle[j-1] == ' ': # data_bundle[16]~[0] 까지
        count += 1 #
        # print(data_bundle[j-1], j-1)
        data = data_bundle[j:temp] # 공백 바로 뒤 부터 ~ 다음 공백까지 슬라이싱
        print(count, data)
        temp = j-1
        if count == 2: # width 는 count가 2일때!
            print(data)
            if int(data) >= 100:
                data_is = data_bundle.replace("vehicle", "truck")
print(data_is)