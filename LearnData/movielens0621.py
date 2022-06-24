import pandas as pd
import os  # path를 사용하기 위해
import matplotlib.pyplot as plt

# 컬럼 수가 많아도 다 display 하기 위해서
pd.set_option("display.max_columns", None)

# 파일을 불러와야해
path = "./ml-latest-small/"
# data를 Load 후 dataframe에 로드
#  rating.csv : 실제 사용자가 특정 영화에 몇 점을 줬는지 작성한 테이블
#  movies.csv : 영화 이름과 장르
#  tags.csv : 실제 사용자가 달아놓은 재미있는, 무서운, 등의 태그가 달려있음
rating_df = pd.read_csv(os.path.join(path + "ratings.csv"),
                        encoding="utf-8") # encoding 해주어야 한다.
movies_df = pd.read_csv(os.path.join(path + "movies.csv"),
                        encoding="utf-8")
tags_df = pd.read_csv(os.path.join(path + "tags.csv"),
                      encoding= "utf-8")

print("=============================데이터는 어떻게 구성===============================")
# 0. 데이터가 어떻게 구성되어 있는지 확인해봅시다.
print(f'{rating_df.shape} \n {rating_df.head()}') # timestamp는 평점을 받은 시점이라고한다. 굳이 사용하진 않을 거 같고
print(f'{movies_df.shape} \n {movies_df.head()}')
print(f'{tags_df.shape} \n {tags_df.head()}')

print("==============================rating_df분석===============================")
# 1. 평점 데이터(rating_df)의 데이터 분석(기초 통계)
# 평점을 준 유저는 총 몇 명인가요?
# rating_df.groupby를 해주면 user별로 뭉치겠죠. 그 길이를 구하면 총 유저의 수겠지
# unique()라는 메서드로도 셀 수 있음

# print(len(rating_df["userId"].value_counts())) # 그냥 이건 내가 해봄.. 610

print(f'User: {len(rating_df.groupby(["userId"]))}') # 맞넹 610명
print(f'User_using Unique() : {len(rating_df.userId.unique())}')

# 평점을 받은 영화의 수는 몇 개일까요?
# 9742개의 영화가 있고 평점을 받은 영화는 9724개 인것을 확인! 42랑 24야.. 같은거 아님...
# rating_df.movieId.unique()
print(f'# Movie: {len(rating_df.groupby(["movieId"]))}') # 9724
print(f'unique() # Movie: {len(rating_df.movieId.unique())}')

# 평점의 평균, 표준편차 등을 확인
# print(f' Mean Rating : {rating_df["rating"].mean()}')
print(f' Mean Rating : {rating_df.rating.mean()}') # 3.50~
print(f' Std Rating : {rating_df.rating.std()}') # 1.04~

# rating_df 의 기본 정보 확인
print(rating_df.info())
# 통계에 대한 데이터를 확인하기 위해서는 describe() 메서드 사용
print(rating_df.describe())
# NaN 유무 확인 메서드 : isnull
print(rating_df.isnull().sum())


print("==============================groupby를 활용한 통계 연습===============================")
# 2. groupby 를 활용한 통계 연습
# user별 평점 평균 (userId 가 1인 사람의 평균 평점, 2인 사람의 평균 평점)
# print(rating_df.groupby("userId")["rating"].mean()) # my version
print(rating_df.groupby("userId").mean()["rating"]) # prof. version 둘 다 결과는 같다.

userAvgRat = rating_df.groupby("userId")["rating"].mean()

# user별 평점별 평가 횟수
# 1번 user가 1점을 몇 번 줬고, 2점을 몇번 줬는지
# print(rating_df.groupby("userId")["rating"].value_counts(sort=False)) # my version
print(rating_df.groupby(["userId", "rating"]).size()) # prof. version

# user가 평점을 몇 번 줬는지.. (count())
print(rating_df.groupby("userId")["movieId"].count())

movieCount = rating_df.groupby("userId")["movieId"].count()

print("======================새로운 데이터 프레임 생성=====================")
# user가 평균적으로 준 평점과 평점을 준 영화의 수에 대한 DataFrame을 생성
# dataframe name = stat_df

# pd.DataFrame 이용
stat_df_test = pd.DataFrame([userAvgRat, movieCount])

stat_df_test = stat_df_test.transpose()
stat_df_test["movieId"] = stat_df_test["movieId"].astype(int) # 데이터프레임으로 생성하고 나니 movie갯수가 float길래 int로 변환
stat_df_test.rename(columns={"rating" : "avg Rating", "movieId" : "# of movie rating"}, inplace=True)
print(stat_df_test)
print(stat_df_test.info())

# pd.concat 이용
stat_df_cc = pd.concat([userAvgRat, movieCount], axis = 1)

stat_df_cc.rename(columns={"rating" : "avg Rating", "movieId" : "# of movie rating"}, inplace=True)
print(stat_df_cc)
print(stat_df_cc.info())

# 교수님 version ==> pd.DataFrame, 딕셔너리타입으로~~
stat_df = pd.DataFrame({
    "rating_mean" : rating_df.groupby("userId")["rating"].mean(),
    "movie_count" : rating_df.groupby("userId")["movieId"].count()
})
print(stat_df)

stat_df2 = pd.DataFrame({
    "rating_mean" : userAvgRat,
    "movie_count" : movieCount
})
print(stat_df2)