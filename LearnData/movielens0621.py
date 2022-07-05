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
# print(f'{movies_df.shape} \n {movies_df.head()}')
# print(f'{tags_df.shape} \n {tags_df.head()}')

print("==============================rating_df분석===============================")
# 1. 평점 데이터(rating_df)의 데이터 분석(기초 통계)
# 평점을 준 유저는 총 몇 명인가요?
# rating_df.groupby를 해주면 user별로 뭉치겠죠. 그 길이를 구하면 총 유저의 수겠지
# unique()라는 메서드로도 셀 수 있음

# print(len(rating_df["userId"].value_counts())) # 그냥 이건 내가 해봄.. 610

# print(f'User: {len(rating_df.groupby(["userId"]))}') # 맞넹 610명
# print(f'User_using Unique() : {len(rating_df.userId.unique())}')

# 평점을 받은 영화의 수는 몇 개일까요?
# 9742개의 영화가 있고 평점을 받은 영화는 9724개 인것을 확인! 42랑 24야.. 같은거 아님...
# rating_df.movieId.unique()
# print(f'# Movie: {len(rating_df.groupby(["movieId"]))}') # 9724
# print(f'unique() # Movie: {len(rating_df.movieId.unique())}')

# 평점의 평균, 표준편차 등을 확인
# print(f' Mean Rating : {rating_df["rating"].mean()}')
# print(f' Mean Rating : {rating_df.rating.mean()}') # 3.50~
# print(f' Std Rating : {rating_df.rating.std()}') # 1.04~

# rating_df 의 기본 정보 확인
# print(rating_df.info())
# 통계에 대한 데이터를 확인하기 위해서는 describe() 메서드 사용
# print(rating_df.describe())
# NaN 유무 확인 메서드 : isnull
# print(rating_df.isnull().sum())


print("==============================groupby를 활용한 통계 연습===============================")
# 2. groupby 를 활용한 통계 연습
# user별 평점 평균 (userId 가 1인 사람의 평균 평점, 2인 사람의 평균 평점)
# print(rating_df.groupby("userId")["rating"].mean()) # my version
# print(rating_df.groupby("userId").mean()["rating"]) # prof. version 둘 다 결과는 같다.

userAvgRat = rating_df.groupby("userId")["rating"].mean()

# user별 평점별 평가 횟수
# 1번 user가 1점을 몇 번 줬고, 2점을 몇번 줬는지
# print(rating_df.groupby("userId")["rating"].value_counts(sort=False)) # my version
# print(rating_df.groupby(["userId", "rating"]).size()) # prof. version

# user가 평점을 몇 번 줬는지.. (count())
# print(rating_df.groupby("userId")["movieId"].count())

movieCount = rating_df.groupby("userId")["movieId"].count()

print("======================새로운 데이터 프레임 생성=====================")
# user가 평균적으로 준 평점과 평점을 준 영화의 수에 대한 DataFrame을 생성
# dataframe name = stat_df

# pd.DataFrame 이용
stat_df_test = pd.DataFrame([userAvgRat, movieCount])

stat_df_test = stat_df_test.transpose()
stat_df_test["movieId"] = stat_df_test["movieId"].astype(int) # 데이터프레임으로 생성하고 나니 movie갯수가 float길래 int로 변환
stat_df_test.rename(columns={"rating" : "avg Rating", "movieId" : "# of movie rating"}, inplace=True)
# print(stat_df_test)
# print(stat_df_test.info())

# pd.concat 이용
stat_df_cc = pd.concat([userAvgRat, movieCount], axis = 1)

stat_df_cc.rename(columns={"rating" : "avg Rating", "movieId" : "# of movie rating"}, inplace=True)
# print(stat_df_cc)
# print(stat_df_cc.info())

# 교수님 version ==> pd.DataFrame, 딕셔너리타입으로~~
stat_df = pd.DataFrame({
    "rating_mean" : rating_df.groupby("userId")["rating"].mean(),
    "movie_count" : rating_df.groupby("userId")["movieId"].count()
})
# print(stat_df)

stat_df2 = pd.DataFrame({
    "rating_mean" : userAvgRat,
    "movie_count" : movieCount
})
# print(stat_df2)

############################ 2022-06-28 ###########################

# 2. 영화별 평균 평점이 얼마인지, 얼마나 많은 평가를 받았는지 등에 대해서 통계
# movie_stat_df 를 생성하고, mean, count 등을 확인해보자.
movie_stat_df = pd.DataFrame({
    # count() : NaN을 카운트 하지 않습니다.
    "cnt_user_ratings" : rating_df.groupby("movieId")["userId"].count(),
    "mean_ratings" : rating_df.groupby("movieId")["rating"].mean(),
    "std_ratings" : rating_df.groupby("movieId")["rating"].std()
})

movie_stat_df.reset_index(inplace=True) # join default가 안되서 다시 index를 리셋해줌,아까보니 movieId가 index더라고

print(movie_stat_df.head())

# movieId 만 나오고 title이 없으니까 join을 써서 title이 나오게 하려고 한다.
# join 하기 전에 평점을 가장 많이 받은 영화순(movieId)으로 sorting (내림차순)
# sort_valus(by=["컬럼명"])
movie_stat_df.sort_values(by=["cnt_user_ratings"],
                          ascending=False, inplace=True)
print(movie_stat_df.head())

# 이제 Join 해봅시다. movie_stat_df 와 movies_df
# merge는 default가 inner, 모든 컬럼이 중복되는 녀석을 기준으로 한다.
df_join_movies = pd.merge(movie_stat_df, movies_df,
                          how="left",
                          left_on="movieId", # left의 key값
                          right_on="movieId")
print("===================================================================")
print(df_join_movies.head())
print(f'{len(df_join_movies)}\n{df_join_movies}') # 9724
# len(rating_df.groupby(["movieId"]))가 9724개였거든, 평점받은 영화의 갯수가..!

# 결과는 같지만 다르게도 join 해볼까...??
df_join_movies1 = pd.merge(movie_stat_df, movies_df) # movieId가 index면 오류나니까 reset_index해줘
df_join_movies2 = pd.merge(movie_stat_df, movies_df, how="inner", on="movieId")

print(f'{len(df_join_movies1)}\n{df_join_movies1}')
print(f'{len(df_join_movies2)}\n{df_join_movies2}')


# 특정 영화에 대해서 평점 분포 등을 살펴보자.
# Forest Gump : 356 (movieId)
# Matrix : 2571
# 평점의 분포를 histogram 으로 표현
# pandas hist() 메서드 이용
# hist = rating_df[rating_df["movieId"] == 356]["rating"].hist()
# plt.show()

# movieId가 356이고, rating이 2이하인 데이터
print(rating_df[(rating_df.movieId == 356) & (rating_df.rating <= 2.0)])
# qna. 왜 and, or로 쓰면 안될까? ==> 비트연산자만 사용가능하더라... &랑 |
#  왠지는 모르겠는지 버전문제일 수도 있고.. ^^ 뭔가 꼬여서 그랬나봄
#  JSON annotation 할 때 'or'로 적용안됐던 이유가 이건가봐 ==> 근데 얜 |로 해도 안돼..

print()
# movieId가 356이거나 2571번인 영화정보
print(rating_df[(rating_df.movieId == 356) | (rating_df.movieId == 2571)])


# userId 가 1인 사람이 평점 4.0 이상을 준 영화를 [평점, timestamp]
# 기준으로 내림차순 정렬 후 제목과 장르를 출력 (DataFrame)

userId1_4 = rating_df[(rating_df.userId == 1) & (rating_df.rating >= 4.0)]
# print(userId1_4)
userId1_4 = userId1_4.sort_values(by=["rating", "timestamp"], ascending=False)
# 제목과 장르를 출력하려면 merge 해야겠네
userId1_4_join = pd.merge(userId1_4, movies_df, how="left", left_on="movieId", right_on="movieId")
print(userId1_4_join.head(10))
# 이제 제목과 장르만 출력해보자
print("=================================This is what you want=================================")
print(userId1_4_join.loc[:, ["title", "genres"]].head(10))
print(len(userId1_4_join))

# 교수님 풀이
# 1. 내림차순 정렬 한 후 df와 movies_df를 merge함으로써 해당 문제롤 해결
# 2. 내림차순 정렬 한 결과의 movieId를 가지고와서
#  ==> movies_df에서 해당 movieId에 대한 영화정보를 가지고 오는 방버

# 2로 풀어봅시다.
# 1) userId 가 1인 사람이 평점 4.0 이상을 준 영화
# rating_df[(rating_df.userId == 1) & (rating_df.rating >= 4.0)]
# 2) 평점과 timestamp 기준으로 내림차순
# rating_df[(rating_df.userId == 1)
#           & (rating_df.rating >= 4.0)].sort_values(by=["rating", "timestamp"],
#                                                    ascending=False)
# 3) 1), 2)번을 만족하는 movieId를 가지고 옴 ==> series 형태일 거야
movie_ids = rating_df[(rating_df.userId == 1)
          & (rating_df.rating >= 4.0)].sort_values(by=["rating", "timestamp"],
                                                   ascending=False)["movieId"]
# loc으로 movieId에 접근하려고 함
movie_df_index = movies_df.set_index("movieId")
# print(movie_df_index.head())
extract_movies_df = movie_df_index[["title", "genres"]].loc[movie_ids]
print(extract_movies_df.head(10))

# check 한 번 해보세요.