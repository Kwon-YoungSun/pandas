#%%

### 그룹 객체 필터링

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 정렬
grouped = df.groupby(['class'])

# --------------------------------------------------------------
# 데이터 개수가 200개 이상인 그룹만을 필터링하여 데이터프레임으로 변환
# First와 Third인 그룹의 데이터만 추출됨
grouped_filter = grouped.filter(lambda x: len(x) >= 200)
print(grouped_filter.head())
print()
print(type(grouped_filter))
# %%

# age 열의 평균이 30보다 작은 그룹만을 필터링하여 데이터프레임으로 변환
age_filter = grouped.filter(lambda x: x.age.mean() < 30)
print(age_filter.tail())
print()
print(type(age_filter))

# %%
