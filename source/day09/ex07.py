#%%

### K-Means

### 기본 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse.coo import coo_matrix

'''
[Step 1] 데이터 준비
'''

# Wholesale customers 데이터셋 가져오기(출처: UCI ML Repository)
# 각 고객의 연간 구매금액을 상품 카테고리별로 구분하여 정리한 데이터
# 첫 2개 열은 고객의 일반 정보를 담고 있음
uci_path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/\
00292/Wholesale%20customers%20data.csv'
df = pd.read_csv(uci_path, header=0)

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
'''
[Step 3] 데이터 전처리
'''

# 분석에 사용할 속성 선택
# 비지도 학습이므로 예측 변수를 지정할 필요가 없고 필요한 속성을 모두 설명 변수로 활용함
X = df.iloc[:, :]
print(X[:5])
print('\n')

# 설명 변수 데이터 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

print(X[:5])
# %%
'''
[Step 4] k-means 군집 모형 - sklearn 사용
'''

# sklearn 라이브러리에서 cluster 군집 모형 가져오기
from sklearn import cluster

# 모형 객체 생성
# 클러스터 개수는 5
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

# 모형 학습
# 모형은 스스로 학습하여 설정한 클러스터 개수만큼 데이터를 구분
kmeans.fit(X)

# 예측(군집)
cluster_label = kmeans.labels_      # 모형의 labels_ 속성에 구분한 클러스터 값 입력
print(cluster_label)
print()

# 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())
# %%

# 그래프로 표현 - 시각화
# 매번 실행할 때마다 예측값의 분포가 달라지는 점에 유의하자.
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', colorbar=True, figsize=(10, 10))
plt.show()
plt.close()
# %%

# 큰 값으로 구성된 클러스터(0, 4) 제외 - 값이 몰려 있는 구간을 자세하게 분석
# 다른 값들에 비해 지나치게 큰 값으로 구성되는 클러스터에 속하는 값들을 제외하고 다시 그리기
# 데이터들이 몰려 있는 구간을 확대해서 자세하게 파악할 수 있음
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]

ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1', colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1', colorbar=True, figsize=(10, 10))
plt.show()
plt.close()
# %%
