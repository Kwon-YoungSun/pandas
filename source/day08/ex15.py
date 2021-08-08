#%%

### 데이터 집계

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 정렬
grouped = df.groupby(['class'])

# 1. 각 그룹에 대한 모든 열의 표준편차를 집계하여 데이터프레임으로 반환
std_all = grouped.std()
print(std_all)
print()
print(type(std_all))
print()

# 2. 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환
std_fare = grouped.fare.std()
print(std_fare)
print()
print(type(std_fare))
# %%
# 그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인자로 전달
def min_max(x):                 # 최대값 - 최소값
    return x.max() - x.min()

# 3. 각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())
# %%

# 4. 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print()

# 5. 각 열마다 다른 함수를 적용하여 집계
agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
print(agg_sep.head())
# %%