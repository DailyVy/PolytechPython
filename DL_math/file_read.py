def read_value(file_name):
    rtn_list = []
    # 데이터의 row 총 개수를 받아보고 싶다(train/test data set을 나누기 위해서)
    cnt = 0
    # 예외처리
    try:
        f = open(file_name, "r") # r: read, w: write, rw:read and write, ...
        while True:
            line = f.readline() # 73  80  75  152 \n이 들어가 있다.
            # print(line.rstrip("\n"))
            if not line: break # line이 없으면 break
            # new line(\n)을 제거(rstrip)하고, 탭(\t)으로 split
            # ==> map을 이용하여 float형태로 변환
            # ==> map object를 리스트로 바꿔줌
            # ==> 이걸 rtn_list에 append, 즉, list 안에 list가 들어간다.
            # [[73.0, 80.0, 75., 152.], [93., 88., ...]
            rtn_list.append(list(map(float, line.rstrip("\n").split("\t"))))
            cnt += 1
        f.close()
    except FileNotFoundError as e:
        print(e)

    return rtn_list, cnt

if __name__ == "__main__":
    rtn_list = read_value("score_mlr03.txt")
    print(rtn_list)