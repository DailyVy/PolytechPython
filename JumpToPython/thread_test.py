import threading # 스레드를 생성하기 위한 threading 모듈
import time

# 처음
# def long_task(): # 5초의 시간이 걸리는 함수
#     for i in range(5):
#         time.sleep(1) # 1초간 대기
#         print(f'working:{str(i)}\n')
#
# print("Start")
# for i in range(5): # long_task()를 5번 반복하니 총 25초의 시간이 걸린다.
#     long_task()
#
# print("End")

# 수정 : Start, End가 먼저 출력
# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print(f'working:{str(i)}\n')
# print("Strat")
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task) # 스레드를 생성한다.
#     threads.append(t)
#
# for t in threads:
#     t.start() # 스레드 실행
#
# print("End")


# 수정2 : Start, 스레드, End 출력
def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join() # join 으로 스레드가 종료될 때가지 기다린다.
print("End")