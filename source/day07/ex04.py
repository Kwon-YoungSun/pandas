#%%
### 가장 많이 나타나는 값으로 바꾸기

import seaborn as sns

df = sns.load_dataset('titanic')

# embark_town 열의 829행의 NaN 데이터 출력
print(df['embark_town'][825:830])
print()

# embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
# value_counts 메소드를 사용해서 승선도시별 승객 수를 찾고, idxmax() 메소드로 가장 큰 값을 갖는 도시(Southampton)를 찾기
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
print()

df['embark_town'].fillna(most_freq, inplace=True)

# embark_town 열 829행의 NaN 데이터 출력(NaN값이 most_freq 값으로 대체)
print(df['embark_town'][825:830])
# %%
