##########################################숙제####################################################
# 데이터 변경하기
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
# 넓이가 100 이상인 vehicle 의 경우에는 vehicle -> truck으로 변경, x, y, width, height

########## 1. No split!!!!! 리스트 활용하지 말고!!!!!!!!!!!!!!!!!!!
print("\n=========================split 사용 X, 리스트 X, 오직 문자열로만===========================\n")
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 40 40 100 100 vehicle 20 20 150 50 vehicle 30 30 295 90"

str_txt = str_txt + ' v' # :"vehicle ~ v 앞, 처음 v부터 뒤의 v의 앞까지 데이터를 묶기 위해. 마지막 부분은 v가 존재하지 않으니 일부러 넣어줌
temp_txt = '' # 결과를 임시 저장하기 위한 변수 선언
first_i = 0 # str_txt의 첫번째 인덱스

# 첫번째 v인덱스~두번째 v인덱스-1 까지 같은 데이터 묶음
# 0번째 인덱스는 무조건 v로 시작하므로 그 다음 v를 찾기 위해 일부러 1부터 range 시작
for i in range(1,len(str_txt)): # 문자열 길이 만큼 for문 돌려서 v의 인덱스 찾기
    if str_txt[i] == 'v':
        data_bundle = str_txt[first_i:i-1] # 첫번째 v부터 두번째 v 앞의 공백까지 슬라이싱(공백 미포함)
        # print(data_bundle) # 데이터 묶음확인
        first_i = i # 첫번째 v 업데이트

        # 이제 각 데이터 묶음 별로 확인!!
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
                    else:
                        temp_txt = temp_txt + ' ' + data_bundle

str_txt = temp_txt.lstrip() # 왼쪽 공백 지우기
print(str_txt)


########## 2. 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기
print("\n=========================리스트와 문자열 함수 split 이용하여 동일 결과 도출하기 ===========================\n")
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 40 40 100 100 vehicle 20 20 150 50 vehicle 30 30 95 90"

list_txt = str_txt.split()

# 리스트 안 index, value 확인
# for i, name in enumerate(list_txt):
#     print(i, name)
# vehicle은 0 ,5, 10, 15 ... 5i 마다 존재 (i= 0,1,2...)
# width는 3, 8, 13, ... 5i + 3 마다 존재 (i= 0,1,2,...)

for i in range(0,len(list_txt),5): # 0부터 리스트의 마지막 인덱스까지, step 5씩! 즉 0, 5, 10, ...
    if int(list_txt[i+3]) >= 100: # width 값이 100 이상일 경우
        list_txt[i] = "truck" # truck으로 값 변경

str_txt = ' '.join(list_txt) # 리스트를 문자열로 변환
print(str_txt) # 값 확인
