import pandas as pd


# read_csv() 함수로 df 생성
df = pd.read_csv('datasets/part3/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count())
print()

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
unique_values = df['origin'].value_counts()
print(unique_values)
print()

# value_counts 메소드가 반환하는 객체 타입 출력
print(type(unique_values))
