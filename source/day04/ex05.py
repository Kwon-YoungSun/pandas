#%%
# Jupytor Notebook을 사용하기 위해서는 #%%를 입력
from numpy import kaiser
import pandas as pd

# df = pd.read_excel('datasets/part3/남북한발전전력량.xlsx')  # 데이터프레임 변환
df = pd.read_excel('../../datasets/part3/남북한발전전력량.xlsx')  # 데이터프레임 변환

df_ns = df.iloc[[0, 5], 3:]         # 남한, 북한 발전량 합계 데이터만 추출
df_ns.index = ['South', 'North']    # 행 인덱스 변경
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())
print()

# 행, 열 전치하여 다시 그리기
tdf_na = df_ns.T
print(tdf_na.head())
print()
tdf_na.plot(kind='bar')
# %%
