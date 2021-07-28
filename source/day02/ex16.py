# 라이브러리 불러오기
from numpy import subtract
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())        # 마지막 5행 표시
print()
print(type(df))
print()

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.tail())  # 마지막 5행 표시
print()
print(type(addition))
print()

# 데이터프레임끼리 연산하기(addition - df)
subtraction = addition - df
print(subtraction.tail())       # 마지막 5행 표시
print()
print(type(subtraction))

