#%%
### 중복 데이터 제거

# 라이브러리 불러오기
import pandas as pd

# 중복 데이터를 갖는 데이터프레임 만들기
df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'],
                   'c2' : [1, 1, 1, 2, 2],
                   'c3' : [1, 1, 2, 2, 2]})
print(df)
print()

# 데이터프레임에서 중복 행 제거
# drop_duplicates() 메소드를 이용하여 중복되는 행을 제거하고 고유한 관측값을 가진 행들만 남김
df2 = df.drop_duplicates()
print(df2)
print()

# c2, c3열을 기준으로 중복 행 제거
df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)

# %%
