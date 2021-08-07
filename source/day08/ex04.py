#%%

### 데이터프레임에 apply(axis=0) 적용
### 시리즈를 입력받아서 하나의 값을 반환하는 함수를 매핑하면 시리즈를 반환한다.

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print()

# 사용자 함수 정의
def min_max(x):                 # 최대값 - 최소값
    return x.max() - x.min()

# 데이터프레임의 각 열을 인자로 전달하면 시리즈를 반환
# axis=0 옵션은 따로 설정하지 않아도 기본 적용됨
result = df.apply(min_max)      # 기본값 axis=0
print(result.head())
print()
print(type(result))
# %%
