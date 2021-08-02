#%%
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part3/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 2개의 열을 선택하여 산점도 그리기
# 차량 무게에 따른 연비의 분포
df.plot(x='weight', y='mpg', kind='scatter')
# %%
