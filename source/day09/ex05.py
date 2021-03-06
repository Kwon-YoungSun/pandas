#%%

### SVM 모형
#%%

### KNN 분류 알고리즘

'''
[Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터셋 가져오기
'''

### 기본 라이브러리 불러오기
from matplotlib.pyplot import legend
import pandas as pd
import seaborn as sns

# load_dataset 함수를 사용하여 데이터프레임으로 변환
df = sns.load_dataset('titanic')

# 데이터 살펴보기
print(df.head())

# IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 15)
print(df.head())

# %%
'''
[Step 2] 데이터 탐색/전처리
'''

# 데이터 자료형 확인
print(df.info())

# %%
# NaN값이 많은 deck 열 삭제, embarked와 내용이 겹치는 embark_town 열 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)
# %%
# age 열에 나이 데이터가 없는 모든 행 삭제 - age 열(891개 중 177개의 NaN값)
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))
# %%

# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(most_freq)
print()

print(rdf.describe(include='all'))      # 'embarked' 열의 최빈값(top)을 확인해도 같은 결과를 얻는다.
print()

rdf['embarked'].fillna(most_freq, inplace=True)
# %%
'''
[Step 3] 분석에 사용할 속성 선택
'''

# 분석에 활용할 열(속성) 선택
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())

# %%

# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환(day07의 ex11.py, ex12.py를 살펴보기)
# KNN 모형에 적용하기 위해 'sex' 열과 'embarked' 열의 범주형 데이터를 숫자형으로 변환
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

# 기존 'sex'열과 'embarked' 열 삭제
ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head())
# %%
'''
[Step 4] 데이터셋 구분 - 훈련용(train data) / 검증용(test data)
'''

# 속성(변수) 선택
X=ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]  # 설명 변수 X
y=ndf['survived']   # 예측 변수 Y

# 설명 변수 데이터를 정규화(normalization)
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
# %%
# --------------------------------------------------------
'''
[Step 5] SVM 분류 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 SVM 분류 모형 가져오기
from sklearn import svm

# 모형 객체 생성(kernel='rbf') 적용
# 이때 데이터를 벡터 공간으로 매핑하는 함수를 커널(kernel)이라고 하는데, kernel='rbf' 옵션으로 RBF(Radial Basis Function) 함수를 적용한다.
# 이외에 Linear, Polynimial, Sigmoid 등의 커널이 있다.
svm_model = svm.SVC(kernel='rbf')

# ***** train data를 가지고 모형 학습
svm_model.fit(X_train, y_train)

# test data를 가지고 y_hat 예측(분류)
y_hat = svm_model.predict(X_test)

print(y_hat[0:10])
print(y_test.values[0:10])

# %%

# 모형 성능 평가 - Confusion Matrix 계산
from sklearn import metrics
svm_metrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_metrix)
print()

# 모형 성능 평가 - 평가 지표 계산
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
# %%
