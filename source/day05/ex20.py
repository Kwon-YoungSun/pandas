#%%
### 버블 차트
# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part4/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# cylinders 개수의 상대적 비율을 계산하여 시리즈 생성(해당 열의 최댓값 대비 상대적 크기를 나타내는 비율 계산)
cylinders_size = df.cylinders/df.cylinders.max() * 300

# 3개의 변수로 산점도 그리기
# c = color, s = size
df.plot(kind='scatter', x='weight', y='mpg', c='coral', s=cylinders_size, figsize=(10, 5), alpha=0.3)
plt.title('Scatter Plot - mpg-weight-cylinders')
plt.show()
# %%
