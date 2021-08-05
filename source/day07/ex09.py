#%%
### 자료형 변환

# 라이브러리 불러오기
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part5/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# ---------------------------------------------------------------------------
# 각 열의 자료형 확인: dtypes 속성 활용
# dtypes 속성 대신 info() 메소드를 사용해도 각 열의 자료형 확인 가능
print(df.dtypes)
print()

# horespower 열의 고유값 확인
# 고유값 중 문자 '?'가 섞여 있는 것을 알 수 있음
print(df['horespower'].unique())
print()

# 누락 데이터('?') 삭제(NaN값으로 변환 후 삭제)
import numpy as np
df['horespower'].replace('?', np.nan, inplace=True)     # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)  # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')     # astype('float')를 이용하여 문자열을 실수형으로 변환

# horespower 열의 자료형 확인
print(df['horespower'].dtypes)


# %%
# origin 열의 고유값 확인
print(df['origin'].unique())

# 정수형 데이터를 문자형 데이터로 변환
df['origin'].replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)

# origin 열의 고유값과 자료형 확인
print(df['origin'].unique())
print(df['origin'].dtypes)

# %%
# 'origin'열 값은 3개의 국가이름이 반복된다. 이처럼 유한 개의 고유값이 반복적으로 나타나는 경우에는
# 범주형 데이터로 표현하는 것이 효율적이다.

# 문자열을 범주형으로 변환
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

# 범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

# %%
# 연도는 시간적인 순서의 의미는 있으나 숫자의 상대적인 크기는 별 의미가 없으므로 범주형으로 표현하는 것이 적절하다.

# model year 열의 정수형을 범주형으로 변환
print(df['model year'].sample(3))                           # sample() 메소드로 'model year'열에서 무작위로 3개의 행을 선택해서 출력
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))
# %%
