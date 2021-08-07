#%%

### 데이터프레임 연결(concatenate)

# 라이브러리 불러오기
import pandas as pd

# 데이터프레임 만들기
df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3]
                    )

df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5]
                    )
print(df1, '\n')
print(df2, '\n')

# 1. 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기
# 축방향을 지정하지 않으면 기본 옵션(axis=0)이 적용되어 위 아래 행 방향으로 연결된다.
# 이때 각 데이터프레임의 행 인덱스는 본래 형태를 유지한다.

# 열 이름에 대해서는 join='outer' 옵션이 기본 적용되어, df1의 열 이름(A, B, C)와 df2의 열 이름 (B, C, D, E)의 합집합으로 
# 연결 데이터프레임의 열 이름 배열 (A, B, C, D, E)를 구성한다.

# 한편 join='inner' 옵션의 경우 교집합 (B, C)가 기준이 된다.

result1 = pd.concat([df1, df2])
print(result1, '\n')
# %%

# 2. ignore_index=True 옵션 설정하기
# 기존 행 인덱스를 무시하고 새로운 행 인덱스를 설정한다.
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2, '\n')
# %%

# 3. 2개의 데이터프레임을 좌우 열 방향으로 이어 붙이듯 연결하기
# axis=1 옵션을 사용하면 데이터프레임을 좌우 열 방향으로 연결한다.
# 따라서 기존 열 이름 배열이 그대로 유지되고, 연결되는 데이터프레임의 행 인덱스는 join='outer' 옵션이 기본값으로 적용되어
# 각 데이터프레임의 행 인덱스들의 합집합으로 구성된다.
result3 = pd.concat([df1, df2], axis=1)
print(result3, '\n')
# %%

# 4. join = 'inner' 옵션 적용하기(교집합)
# 연결할 데이터프레임들의 행 인덱스의 교집합을 기준으로 사용
result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in, '\n')
# %%

# 5. 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

# df1과 sr1을 좌우 열 방향으로 연결하기
result4 = pd.concat([df1, sr1], axis=1)
print(result4, '\n')

# df2와 sr2를 좌우 열 방향으로 연결하기
result5 = pd.concat([df2, sr2], axis=1, sort=True)
print(result5, '\n')
# %%
# sr1과 sr3을 좌우 열 방향으로 연결하기
result6 = pd.concat([sr1, sr3], axis=1)
print(result6, '\n')

# sr1과 sr3를 아래 위 방향으로 연결하기
result7 = pd.concat([sr1, sr3], axis=0)
print(result7, '\n')
# %%
