##########################################숙제####################################################
# 데이터 변경하기
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
# 넓이가 100 이상인 vehicle 의 경우에는 vehicle -> truck으로 변경, x, y, width, height

########## 1. No split!!!!! 리스트 활용하지 말고!!!!!!!!!!!!!!!!!!!
print("\n=========================split 사용 X, 리스트 X, 오직 문자열로만===========================\n")
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 40 40 100 100 vehicle 20 20 150 50"
str_txt = str_txt + ' v' # :"vehicle ~" v, v의 앞을 기준으로 데이터를 나누기 위해. 마지막 부분은 v가 존재하지 않으니 일부러 넣어줌

temp_txt = '' # 결과를 임시 저장하기 위한 변수 선언
first_i = 0 # str_txt의 첫번째 인덱스

# 첫번째 v인덱스~두번째 v인덱스-1 까지 같은 데이터 묶음
# 0번째 인덱스는 무조건 v로 시작하므로 그 다음 v를 찾기 위해 일부러 1부터 range 시작
for i in range(1,len(str_txt)): # 문자열 길이 만큼 for문 돌려서 v의 인덱스 찾기, vehicle 바로 뒤의 공백은 v의 index + 7 에 등장
    if str_txt[i] == 'v':
        # print(i,i+7) # v 인덱스(i)와 첫 공백 인덱스(i+7)
        data_bundle = str_txt[first_i:i-1] # 첫번째 v부터 두번째 v 앞의 공백까지 슬라이싱(공백 미포함)
        # print(data_bundle) # 데이터 묶음확인
        first_i = i # 첫번째 v 업데이트

        # 이제 각 데이터 묶음 별로 확인!! (last_bundle 도 이와 같은 과정을 거친다)
        temp = len(data_bundle)
        count = 0 # 뒤에서부터 count, 1.height, 2.width, 3.y, 4.x 로 매겨줌==> 우리는 width를 찾아야함 즉, count가 2 일때
        # 뒤에서 부터 data_bundle 내에서 공백 찾기 ==> width는 뒤에서 첫번째 공백과 두번재 공백 사이 존재
        for j in range(len(data_bundle),0,-1): # 17 ~ 1 까지
            if data_bundle[j-1] == ' ': # data_bundle[16] ~ [0] 까지
                count += 1 # 1.height 부터
                data = data_bundle[j:temp] # 공백 바로 뒤부터 ~ 다음 공백까지 슬라이싱, 즉 data_bundle 내 숫자만 추출
                temp = j-1 # temp 업데이트
                if count == 2: # width는 count가 2일 때이다.
                    if int(data) >= 100:
                        temp_txt = temp_txt + ' ' + data_bundle.replace("vehicle", "truck") # temp_txt 에 문자열 더하기
                        # print(temp_txt)
                    else:
                        temp_txt = temp_txt + ' ' + data_bundle
                        # print(temp_txt)

# 마지막 데이터 묶음(last_bundle)은 맨 뒤에 공백이 존재하지 않으니 따로 슬라이싱한다.
# 위와 같은 과정e으로 width를 판별하여 replace를 한다.
# last_bundle = str_txt[first_i:]
# # print(last_bundle)
# temp = len(last_bundle)
# count = 0 # 뒤에서부터 1. height, 2. width, 3. y, 4. x ==> 우리는 width를 찾아야함 즉, count가 2 일때
# # 뒤에서 부터 data_bundle 내에서 공백 찾기 ==> width는 뒤에서 첫번째 공백과 두번재 공백 사이 존재
# for j in range(len(last_bundle), 0, -1):  # 17 ~ 1 까지
#     if last_bundle[j-1] == ' ': # data_bundle[16]~[0] 까지
#         count += 1 #
#         data = last_bundle[j:temp] # 공백 바로 뒤 부터 ~ 다음 공백까지 슬라이싱
#         temp = j-1
#         if count == 2: # width 는 count가 2일때!
#             if int(data) >= 100:
#                 temp_txt = temp_txt + ' ' + last_bundle.replace("vehicle", "truck")
#             else:
#                 temp_txt = temp_txt + ' ' + last_bundle

str_txt = temp_txt.lstrip() # 왼쪽 공백 지우기
print(str_txt)