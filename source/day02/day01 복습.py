import pandas as pd

# 딕셔너리를 선언합니다.
member = [
    [23, 'sun@naver.com'],
    [21, 'joon@naver.com'],
    [26, 'chan@naver.com'],
    [24, 'hyuck@naver.com'],
]

df = pd.DataFrame(member, index=['영선', '준수', '강찬', '오혁'], columns=['나이', '메일'])
print(df)

df_index = df.index
print(df_index)

df_columns = df.columns
print(df_columns)

# 행 선택
print()
print("# '영선' 행만 선택")
df2 = df.loc['영선']
print(df2)

print("# '영선', '준수' 두 행 모두 선택")
df3 = df.loc[['영선','준수']]
print(df3)

# 열 선택
print("# 나이, 메일 열 모두 선택")
df4 = df[['나이', '메일']]
print(df4)