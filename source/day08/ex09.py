#%%
### 불린 인덱싱

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 로딩
titanic = sns.load_dataset('titanic')

# 나이가 10대(10~19세)인 승객만 따로 선택
mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())
# %%
# 나이가 10세 미만(0~9세)이고 여성인 승객만 따로 선택
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())
# %%

# 나이가 10세 미만(0~9세) 또는 60세 이상인 승객의 age, sex, alone 열만 선택
mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morethan60 = titanic.loc[mask3, ['age', 'sex', 'alone']]
print(df_under10_morethan60.head())
# %%
