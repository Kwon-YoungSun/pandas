#%%
### 원핫인코딩
# * 원핫인코딩이란 해당되는 하나의 데이터만 1로 변경해 주고 나머지는 0으로 채워주는 것을 뜻한다.
# * 이렇게 표현된 벡터를 원-핫 벡터(One-Hot vector)라고 한다.

# 라이브러리 불러오기
from operator import le
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

# %%
# ----------------------------------------------------------------------------
# sklern 라이브러리 불러오기
from sklearn import preprocessing

# 전처리를 위한 encoder 객체 만들기
label_encoder = preprocessing.LabelEncoder()            # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()          # one hot encoder 생성

# label encoder로 문자열 범주를 숫자형 범주로 변환
# hp_bin 열에 들어 있는 범주형 데이터를 0, 1을 원소로 갖는 원핫벡터로 변환한다.
onehot_labeled = label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))

# 1차원 벡터를 2차원 행렬로 변환하고 다시 희소행렬로 변환한다.
# 2차원 행렬로 형태 변경
onehot_reshaped = onehot_labeled.reshape(len(onehot_labeled), 1)
print(onehot_reshaped)
print(type(onehot_reshaped))

# 희소행렬(희소행렬(sparse matrix)은 행렬의 값이 대부분 0인 경우를 가리키는 표현이다.)로 변환
onehot_fitted = onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)
print(type(onehot_fitted))

# %%
