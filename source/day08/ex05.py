#%%
### 데이터프레임에 apply() 적용

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print()

# 사용자 함수 정의
def add_two_obj(a, b):          # 두 객체의 합
    return a + b

# 데이터프레임의 2개 열을 선택하여 적용
# x=df, a=df['age'], b=df['ten']
# 모든 행의 연산 결과를 한데 모아서 시리즈 객체를 만든다.
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)         # 반환된 시리즈를 df의 새로운 열 'add'로 추가한다.
print(df.head())

# %%
