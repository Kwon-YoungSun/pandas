#%%
### 누락 데이터 치환

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# age 열의 첫 10개 데이터 출력(5행에 NaN값)
print(df['age'].head(10))
print()

# age 열의 NaN값을 다른 나이 데이터의 평균으로 변경하기
# 누락 데이터를 바꾸기 위해서 fillna() 메소드 사용
mean_age = df['age'].mean(axis=0)       # age 열의 평균 계산(NaN값 제외)
df['age'].fillna(mean_age, inplace=True)

# age 열의 첫 10개 데이터 출력(5행에 NaN값이 평균으로 대체)
print(df['age'].head(10))
# %%
