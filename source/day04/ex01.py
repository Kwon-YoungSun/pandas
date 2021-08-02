import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('datasets/part3/auto-mpg.csv', header=None)

# 열 이름 지정: columns 속성 이용
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 데이터프레임 df의 내용을 일부 확인
print(df.head())        # 처음 5개 행
print('\n')
print(df.tail())        # 마지막 5개 행

# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
print(df.shape)

# 데이터프레임 df의 내용 확인
print()
print(df.info())

# 데이터프레임 df의 자료형 확인
print()
print(df.dtypes)
print('\n')

# 시리즈(mpg 열)의 자료형 확인
print(df.mpg.dtypes)
print()

# 데이터프레임 df의 기술 통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))