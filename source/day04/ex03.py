import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('datasets/part3/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 평균값

# 모든 열의 평균값
print(df.mean())
print()
# mpg 열의 평균값
print(df['mpg'].mean())
print(df.mpg.mean())
print()
# mpg, weight 열의 평균값
print(df[['mpg','weight']].mean())
print()

# 중간값
print('# 중간값')
print(df.median())
print()
print(df['mpg'].median())
print()

# 최대값
# 'horespower' 열은 '?' 문자가 포함되어 있기 때문에 다른 숫자 값까지 전부 문자열로 인식됨
print('# 최대값')
print(df.max())
print()
print(df['mpg'].max())
print()

# 최소값
print('# 최소값')
print(df.min())
print()
print(df['mpg'].min())
print()

# 표준 편차
print('# 표준 편차')
print(df.std())
print()
print(df['mpg'].std())
print()

# 상관계수
print('# 상관계수')
print(df.corr())
print()
print(df[['mpg', 'weight']].corr())