#%%

### 다중회귀분석

### 라이브러리 불러오기
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

'''
[Step 1~3] 데이터 준비
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('../../datasets/part7/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horespower 열의 자료형 변경(문자 -> 숫자)
df['horespower'].replace('?', np.nan, inplace=True)             # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)          # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')             # 문자열을 상수형으로 변환

# 분석에 활용할 열(속성) 선택(연비, 실린더, 출력, 중량)
ndf = df[['mpg', 'cylinders', 'horespower', 'weight']]

'''
[Step 4] 데이터셋 구분 - 훈련용(train data)/검증용(test data)
'''

# 속성(변수) 선택
X=ndf[['cylinders', 'horespower', 'weight']]        # 독립 변수 X1, X2, X3
y=ndf['mpg']        # 종속 변수 Y

# train data와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)
# %%

'''
[Step 5] 단순회귀분석 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()

# train data를 가지고 모형 학습
lr.fit(X_train, y_train)

# 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
r_square = lr.score(X_test, y_test)
print(r_square)
print()

# 회귀식의 기울기
print('X 변수의 계수 a: ', lr.coef_)
print()

# 회귀식의 y절편
print('상수항 b', lr.intercept_)
# %%
# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat = lr.predict(X_test)

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y_test, hist=False, label="y_test")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.legend()
plt.show()
plt.close()
# %%
