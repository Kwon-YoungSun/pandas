#%%
### 다항회귀분석

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

'''
[Step 1~4] 데이터 준비
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('../../datasets/part7/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# horespower 열의 자료형 변경(문자열 -> 숫자)
df['horespower'].replace('?', np.nan, inplace=True)             # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)          # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')             # 문자열을 실수형으로 변환

# 분석에 활용할 열(속성) 선택(연비, 실린더, 출력, 중량)
ndf = df[['mpg', 'cylinders', 'horespower', 'weight']]

# ndf 데이터를 train data와 test data로 구분(7:3 비율)
X=ndf[['weight']]           # 독립 변수 X
y=ndf['mpg']                # 종속 변수 Y

# train data와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print("훈련 데이터: ", X_train.shape)
print("검증 데이터: ", X_test.shape)
# %%
'''
[Step 5] 비선형회귀분석 모형 - sklearn 사용
'''

# 1. sklearn 라이브러리에서 필요한 모듈 가져오기
# sklearn 라이브러리에서 선형회귀분석을 위한 LinearRegression() 함수와
# 다항식 변환을 위한 PolynomialFeatures() 함수를 불러온다.
from sklearn.linear_model import LinearRegression       # 선형회귀분석
from sklearn.preprocessing import PolynomialFeatures    # 다향식 변환

# 2. 다항식 변환
# 2-1. 2차항 객체인 poly를 생성하고,
poly = PolynomialFeatures(degree=2)         # 2차항 적용
# **** 2-2. 독립변수로 사용할 X_train 데이터를 fit_transform() 메소드에 전달하면 2차항 회귀분석에 맞게 변환된다.
X_train_poly = poly.fit_transform(X_train)  # X_train 데이터를 2차항으로 변형

print('원 데이터: ', X_train.shape)
print('2차항 변환 데이터: ', X_train_poly.shape)
# %%

# **** 2-3. train data를 가지고 모형 학습
pr = LinearRegression()
pr.fit(X_train_poly, y_train)

# 2-4. 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
X_test_poly = poly.fit_transform(X_test)            # X_test 데이터를 2차항으로 변형
r_square = pr.score(X_test_poly, y_test)
print(r_square)
# %%

# 2-5. train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat_test = pr.predict(X_test_poly)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(X_train, y_train, 'o', label='Train data')              # 데이터 분포
ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value')      # 모형이 학습한 회귀선
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()
# %%

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
X_ploy = poly.fit_transform(X)
y_hat = pr.predict(X_ploy)

plt.figure(figsize=(10, 5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)

plt.legend()
plt.xlabel('mpg')
plt.show()
plt.close
# %%
