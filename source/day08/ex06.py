#%%
### 데이터프레임에 pipe() 적용

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]

# 각 열의 NaN 찾기 - 데이터프레임 전달하면 데이터프레임 반환
def missing_value(x):
    return x.isnull()

# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 시리즈 반환
def missing_count(x):
    return missing_value(x).sum()

# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값 반환
def total_number_missing(x):
    return missing_count(x).sum()
# %%
# 데이터프레임에 pipe() 메소드로 함수 매핑
result_df = df.pipe(missing_value)
print(result_df.head())
print(type(result_df))
# %%
# 데이터프레임을 입력받으면 각 열의 누락 데이터 개수를 시리즈 형태로 반환
result_series = df.pipe(missing_count)
print(result_series)
print(type(result_series))
# %%
# 데이터프레임을 입력받으면 각 열의 누락 데이터의 개수를 합산하여 반환
result_value = df.pipe(total_number_missing)
print(result_value)
print(type(result_value))
# %%
