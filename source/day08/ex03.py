#%%

### 데이터프레임에 apply(axis=0) 적용
### 시리즈를 입력받고 시리즈를 반환하는 함수를 매핑하면, 데이터프레임 반환

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()

# 사용자 함수 정의
def missiing_value(series):         # 시리즈를 인자로 전달
    return series.isnull()          # 불린 시리즈를 반환

# 데이터프레임의 각 열을 인자로 전달하면 데이터프레임을 반환
result = df.apply(missiing_value, axis=0)
print(result.head())
print()
print(type(result))
# %%
