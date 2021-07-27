import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
# 인덱스를 별도로 정의하지 않았으므로, 정수형 위치 인덱스가 자동 지정됨
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 인덱스 배열은 변수 idx에 저장, 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)