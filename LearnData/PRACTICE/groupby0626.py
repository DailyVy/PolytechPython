import pandas as pd
import numpy as np


pd.set_option("display.max_columns", None)

titanicPath = "../Data/Titanic/train.csv"
titanic = pd.read_csv(titanicPath)

print(titanic.shape) # (891, 12)
print(titanic.head())
print(titanic.info())
print(titanic.isnull().sum()) # Age : 177, Cabin : 687, Embarked : 2
print(titanic.describe())
