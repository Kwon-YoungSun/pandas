#%%
### 단순회귀분석

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv('../../datasets/part7/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 데이터 살펴보기
print(df.head())
print()

# IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 10)
print(df.head())
# %%

'''
[Step2] 데이터 탐색
'''

# 2-1. 데이터 자료형 확인
print(df.info())
print()

# 2-2. 데이터 통계 요약 정보 확인
print(df.describe())

# 2-3. horespower 열의 자료형 변경(문자열 -> 숫자)
print(df['horespower'].unique())                        # horespower 열의 고유값 확인
print()

df['horespower'].replace('?', np.nan, inplace=True)     # '?'을 np.nan으로 변경
df.dropna(subset=['horespower'], axis=0, inplace=True)  # 누락 데이터 행 삭제
df['horespower'] = df['horespower'].astype('float')     # 문자열을 실수형으로 변환

print(df.describe())
# %%

'''
[Step 3] 속성(feature 또는 variable) 선택
'''

# 3-1. 분석에 활용할 열(속성) 선택(연비, 실린더, 출력, 중량)
# 종속변수(Y)가 될 'mpg' 열과 독립변수(X)로 사용할 후보로 3개의 열('cylinders', 'horespower', 'weight')을 포함
ndf = df[['mpg', 'cylinders', 'horespower', 'weight']]
print(ndf.head())


# %%
### 3-2. 종속 변수 Y인 "연비(mpg)"와 다른 변수 간의 선형관계를 그래프(산점도)로 확인
# 3-2-1. Matplotlib으로 산점도 그리기
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
plt.show()
plt.close()
# %%

# 3-2-2. seaborn으로 산점도 그리기
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax1)                  # 회귀선 표시
sns.regplot(x='weight', y='mpg', data=ndf, ax=ax2, fit_reg=False)   # 회귀선 미표시
plt.show()
plt.close()
# %%
# 3-2-3. seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x='weight', y='mpg', data=ndf)                        # 회귀선 없음
sns.jointplot(x='weight', y='mpg', kind='reg', data=ndf)            # 회귀선 표시
plt.show()
plt.close()
# %%

# 3-2-4. seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()
# %%

'''
[Step 4] 데이터셋 구분 - 훈련용(train data)/검증용(test data)
         두 변수 간의 회귀방정식을 찾기 위해 훈련 데이터와 검증 데이터로 나눠서 모형을 구축한다.
         예제는 'weight' 열을 독립 변수 X로 선택하여 데이터를 7:3의 비율로 분할한다.
'''

# 4-1. 속성(변수) 선택
X=ndf[['weight']]           # 독립 변수 X
Y=ndf[['mpg']]              # 종속 변수 Y

# 4-2. train data와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,                  # 독립 변수 
                                                Y,                      # 종속 변수
                                                test_size=0.3,          # 검증 30%
                                                random_state=10)        # 랜덤 추출 값

print('train data 개수: ', len(X_train)) 
print('test data 개수: ', len(X_test))
# %%
'''
[Step 5] 단순회귀분석 모형 만들기 - sklearn 사용
'''

# 5-1. sklearn 라이브러리에서 선형회귀분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 5-2. 단순회귀분석 모형 객체 생성
lr = LinearRegression()

# 5-3. train data를 가지고 모형 학습
# **** 훈련 데이터를 전달하면 모형이 학습을 통해 회귀 방정식의 계수 a,b를 찾는다.
lr.fit(X_train, y_train)

# 5-4. 학습을 마친 모형에 test data를 적용하여 결정계수(R-제곱) 계산
# * 결정계수: 추정한 선형 모형이 주어진 자료에 적합한 정도를 재는 척도로, 종속변인과 독립변인 사이에 상관관계가 높을수록 1에 가까워진다. 
#             즉, 결정계수가 0에 가까운 값을 가지는 회귀모형은 유용성이 낮은 반면, 결정계수의 값이 클수록 회귀모형의 유용성이 높다고 할 수 있다.
r_square = lr.score(X_test, y_test)
print(r_square)
# %%
# 5-5. 회귀식의 기울기
# 계수 a는 회귀식의 기울기를 나타내고, 모형 객체 lr의 coef_ 속성값
print('기울기 a: ', lr.coef_)
print()

# 5-6. 회귀식의 y절편
# 계수 b는 y절편이고, 모형 객체 lr의 intercept_ 속성값
print('y절편 b', lr.intercept_)
# %%

# 5-7. 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교
# 독립 변수 전체 데이터(X)를 predict() 메소드에 입력하여 모형이 반환하는 예측값을 y_hat에 저장
y_hat = lr.predict(X)

# 5-8. 실제 값 y와 모형의 예측값 y_hat을 같은 화면에 분포도를 그려서 비교
plt.figure(figsize=(10, 5))
ax1 = sns.distplot(Y, hist=False, label="Y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.legend()
plt.xlabel('mpg')
plt.show()
plt.close()

# 출력된 결과를 보면 실제 값은 왼쪽으로 편향되어 있고 예측값은 반대로 오른쪽으로 편중되는 경향을 보인다.
# 따라서 독립 변수(weight)와 종속 변수(mpg) 사이에 선형관계가 있지만, 모형의 오차를 더 줄일 필요가 있어 보인다.
# 앞에서 그린 산점도를 보면 직선보다는 곡선의 형태가 더 적합해 보인다.
# 이럴 경우 비선형 회귀분석을 통해 모형의 정확도를 높일 수 있다.
# %%
