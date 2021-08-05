#%%
### 중복 데이터 확인

import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'],
                   'c2' : [1, 1, 1, 2, 2],
                   'c3' : [1, 1, 2, 2, 2]})
print(df)
print()

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기 : duplicated() 메소드 이용
# 전에 나온 행들과 비교하여 중복되는 행이면 True를 반환하고, 처음 나오는 행에 대해서는 False 반환
df_dup = df.duplicated()
print(df_dup)
print()

# 데이터프레임의 특정 열 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)

# %%
