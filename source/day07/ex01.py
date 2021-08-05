#%%
### 누락 데이터 확인

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# print(df.head())
# print()
# print(df.info())

# deck 열의 NaN 개수 계산하기
# value_counts() 메소드를 이용하여 'deck'열에 누락 데이터가 몇 개 포함되어 있는지 체크
# 이 때 누락 데이터의 개수를 확인하려면 반드시 dropna=False 옵션 사용해야 함
nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
print()

# isnull() 메소드로 누락 데이터 찾기
print(df.head().isnull())

print()
# notnull() 메소드로 누락 데이터 찾기
print(df.head().notnull())

print('------------------------------')

# isnull() 메소드로 누락 데이터 개수 구하기
print(df.head().isnull().sum(axis=0))   # sum(axis=0) 메소드를 적용하면 참(1)의 합, 즉 널값 개수의 합을 구한다.
# %%
