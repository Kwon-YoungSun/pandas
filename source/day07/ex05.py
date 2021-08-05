#%%
### 이웃하고 있는 값으로 바꾸기
# * 데이터의 특성상 서로 이웃하고 있는 데이터끼리 유사성을 가질 가능성이 높다. 이럴 때는 앞이나 뒤에서 이웃하고 있는 값으로 치환해 주는 것이 좋다.
# * fillna() 메소드에 'ffill' 옵션을 추가하면 NaN이 있는 행의 직전 행에 있는 값으로 바꿔준다.
# * method='bfill' 옵션을 사용하면 NaN이 있는 행의 바로 다음 행에 있는 값을 가지고 치환한다.

import seaborn as sns


df = sns.load_dataset('titanic')

# embark_town 열의 829행의 NaN 데이터 출력
print(df['embark_town'][825:830])
print()

# embark_town 열의 NaN 값을 바로 앞에 있는 828행의 값으로 변경하기
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])
# %%
