import pandas as pd

# 딕셔너리 정의
dict_data = {'c0':[1, 2, 3], 'c1':[4, 5, 6], 'c2':[7, 8, 9], 'c3':[10, 11, 12], 'c4':[13, 14, 15]}

# 딕셔너리를 데이터프레임으로 변환, 인덱스를 [r0, 01, 02]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print()

# 인덱스를 [r0, r1, r2, r3, r4]로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
print()

# 기존 데이터프레임에 존재하지 않는 행 인덱스가 새롭게 추가되는 경우 그 행의 데이터 값은 NaN 값이 입력된다.
# 이럴 경우 데이터가 존재하지 않는다는 뜻의 NaN 대신 유효한 값으로 채우려면 fill_value 옵션에 원하는 값(0)을 입력 
# reindex로 발생한 NaN값을 숫자 0으로 채우기
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)