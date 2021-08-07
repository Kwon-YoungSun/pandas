#%%

### 날짜 데이터 분리
# 연-월-일 날짜 데이터에서 일부 분리 추출

import pandas as pd

df = pd.read_csv('../../datasets/part5/stock-data.csv')

# 문자열인 날짜 데이터를 판다스 Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])         # df에 새로운 열로 추가
print(df.head())
print()

# dt 속성을 이용하여 new_Data 열의 연-월-일 정보를 년, 월, 일로 구분
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())
print('------------------')

# Timestamp를 Period로 변환하여 연-월-일 표기 변경하기
# to_period() 메소드를 적용하여, 연-월-일 중 연-월 또는 연도를 추출 
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')       # 연도를 나타내는 값 저장
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')        # 연-월을 나타내는 값 저장
print(df.head())
print('------------------')

# 원하는 열을 행 인덱스로 지정
df.set_index('Date_m', inplace=True)
print(df.head())
# %%
