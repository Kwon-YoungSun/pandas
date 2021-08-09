#%%
### Decision Tree 모형

### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np

'''
[Step 1] 데이터 준비/기본 설정
'''

# Breast Cancer 데이터셋 가져오기(출처: UCI ML Repository)
# 샘플 ID, 암세포 조직의 크기와 모양 등 종양 특성을 나타내는 열 9개, 악성 종양 여부(2: 양성, 4: 악성)를 나타내는 열로 구성
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data'
df = pd.read_csv(uci_path, header=None)

# 열 이름 지정
df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']

# IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 15)

'''
[Step 2] 데이터 탐색
'''

# 데이터 살펴보기
print(df.head())
print()

# 데이터 자료형 확인
print(df.info())
print()

# 데이터 통계 요약 정보 확인
print(df.describe())
# %%
# bare_nuclei 열의 자료형 변경(문자열 -> 숫자)
print(df['bare_nuclei'].unique())                           # bare_nuclei 열의 고유값 확인
print()

df['bare_nuclei'].replace('?', np.nan, inplace=True)        # '?'을 np.nan으로 변경
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)     # 누락 데이터 행 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int')         # 문자열을 정수형으로 변환

print(df.describe())                                        # 데이터 통계 요약 정보 확인
# %%
'''
[Step 3] 데이터셋 구분 - 훈련용(train data)/검증용(test data)
'''

# 속성(변수) 선택
X=df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial', 'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]     # 설명 변수 X
y=df['class']                                                                                                       # 예측 변수 Y

# 설명 변수 데이터 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# train data와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

print('train data 개수: ', X_train.shape)
print('test data 개수: ', X_test.shape)
# %%
'''
[Step 4] Decision Tree 분류 모형 - sklearn 사용
'''
# sklearn 라이브러리에서 Decision Tree 분류 모형 가져오기
from sklearn import tree

# 모형 객체 생성(분류 정도를 평가하는 기준으로 criterion='entropy' 적용)
# * 레벨이 많아질수록 모형 학습에 사용하는 훈련 데이터에 대한 예측은 정확해지지만, 모형이 훈련 데이터에 대해서만 지나치게 최적화되어 실제 데이터 예측 능력은 떨어지는 문제 발생
# * 따라서 적정한 레벨값을 찾는 것이 중요함
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)      # max_depth=5: 5단계까지 가지를 확장할 수 있다.

# train data를 가지고 모형 학습
tree_model.fit(X_train, y_train)

# test data를 가지고 y_hat 예측(분류)
y_hat = tree_model.predict(X_test)          # 2: begin(양성), 4: malignant(악성)

print(y_hat[0:10])
print(y_test.values[0:10])
# %%

# 모형 성능 평가 - Confusion Matrix 계산
from sklearn import metrics
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix)
print()

# 모형 성능 평가 - 평가 지표 계산
tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)
# %%
