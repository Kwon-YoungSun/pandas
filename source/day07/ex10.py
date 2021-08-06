#%%
### 데이터 구간 분할

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# read_csv() 함수로 df 저장
df = pd.read_csv('../../datasets/part5/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horespower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horespower'].replace('?', np.nan, inplace=True)             # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)          # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')             # 문자열을 실수형으로 변환


# NumPy 라이브러리의 histogram() 함수를 활용하여 구간 분할하는 방법
# 나누려는 구간(bin) 개수를 bins 옵션에 입력하면 각 구간에 속하는 값의 개수(count)와 경계값 리스트를 반환함

# np.histogram 함수로 3개의 bin으로 나누는 경계값의 리스트 구하기
# 46~107.3 구간, 107.3~168.6 구간, 168.6~230 구간으로 나뉨
count, bin_dividers = np.histogram(df['horespower'], bins=3)
print(bin_dividers)
# %%
# 3개의 bin에 이름 지정
bin_name = ['저출력', '보통출력', '고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horespower'],               # 데이터 배열
                      bins=bin_dividers,                # 경계값 리스트
                      labels=bin_name,                  # bin 이름
                      include_lowest=True)              # 첫 경계값 포함(각 구간의 낮은 경계값 포함)

# horespower 열, hp_bin 열의 첫 15행 출력
print(df[['horespower', 'hp_bin']].head(15))
# %%
