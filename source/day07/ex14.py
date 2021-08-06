#%%
### 정규화
# 각 열(변수)의 데이터 중에서 최대값(max)와 최소값(min)을 뺀 값으로 나누는 방법
# (해당 열의 최소값을 뺀 값) / (해당 열의 최대값과 최소값의 차)

# 라이브러리 불러오기
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part5/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horespower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horespower'].replace('?', np.nan, inplace=True)             # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)          # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')             # 문자열을 실수형으로 변환

# ---------------------------------------------------------
# horespower 열의 통계 요약 정보로 최대값(max)과 최소값(min)확인
print(df.horespower.describe())
print()

# horespower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
min_x = df.horespower - df.horespower.min()
min_max = df.horespower.max() - df.horespower.min()
df.horespower = min_x/min_max

print(df.horespower.head())
print()
print(df.horespower.describe())
# %%
