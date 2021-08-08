#%%
### 피벗 테이블

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# IPython 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)        # 출력할 최대 열 개수
pd.set_option('display.max_colwidth', 20)       # 출력할 열의 너비

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
print(df.head())
print()

# 행, 열, 값, 집계에 사용할 열을 1개씩 지정 - 평균 집계
pdf1 = pd.pivot_table(df,                   # 피벗할 데이터프레임
                       index='class',       # 행 위치에 들어갈 열
                       columns='sex',       # 열 위치에 들어갈 열
                       values='age',        # 데이터로 사용할 열
                       aggfunc='mean')      # 데이터 집계 함수

print(pdf1.head())
# %%

# 값에 적용하는 집계 함수, 2개 이상 지정 가능 - 생존율, 생존자 수 집계
pdf2 = pd.pivot_table(df,                           # 피벗할 데이터프레임
                       index='class',               # 행 위치에 들어갈 열
                       columns='sex',               # 열 위치에 들어갈 열
                       values='age',                # 데이터로 사용할 열
                       aggfunc=['mean', 'sum'])     # 데이터 집계 함수
print(pdf2.head())
# %%
# 행, 열, 값에 사용할 열을 2개 이상 지정 가능 - 평균 나이, 최대 요금 집계
pdf3 = pd.pivot_table(df,                           # 피벗할 데이터프레임
                       index=['class', 'sex'],      # 행 위치에 들어갈 열
                       columns='survived',          # 열 위치에 들어갈 열
                       values=['age', 'fare'],      # 데이터로 사용할 열
                       aggfunc=['mean', 'max'])     # 데이터 집계 함수

# IPython Console 디스플레이 옵션 설정
pd.set_option('display.max_columns', 10)            # 출력할 열의 개수 한도
print(pdf3.head())
print()

# 행, 열 구조 살펴보기
# levels, labels, names라는 3가지 속성이 있다.
# levels : 행은 2개의 열이 사용되어 2중 구조이고, 열은 3중 구조로 이루어짐
print(pdf3.index)
print(pdf3.columns)
# %%

# xs 인덱서 사용 - 행 선택(default: axis=0)
print(pdf3.xs('First'))         # 행 인덱스가 First인 행을 선택

# %%
# 1등석 승객 중 여성의 데이터만을 선택
print(pdf3.xs(('First', 'female')))         # 행 인덱스가 ('First', 'female')인 행을 선택

# %%
# 레벨 이름은 [0, 'sex'] 대신 숫자형 레벨 1을 사용해도 결과는 동일
print(pdf3.xs('male', level='sex'))         # 행 인덱스의 sex 레벨이 male인 행을 선택
print(pdf3.xs('male', level=1))             # 행 인덱스의 sex 레벨이 male인 행을 선택
# %%

print(pdf3.xs(('Second', 'male'), level=[0, 'sex']))      # Second, male인 행을 선택

# %%

# xs 인덱서 사용 - 열 선택(axis=1 설정)
# xs 인덱서를 이용하여 열 인덱스에 접근하기 위해서는 축 값을 axis=1로 설정해야 한다.
print(pdf3.xs('mean', axis=1))              # 열 인덱스가 mean인 데이터를 선택

# %%
print(pdf3.xs(('mean', 'age'), axis=1))     # 열 인덱스가 ('mean', 'age')인 데이터 선택

# %%
print(pdf3.xs(1, level='survived', axis=1)) # survived 레벨이 1인 데이터 선택
# %%
print(pdf3.xs(('max', 'fare', 0), level=[0, 1, 2], axis=1))     # max, fare, survived=0인 데이터 선택
# %%
