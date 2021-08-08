#%%

### 데이터프레임 합치기(merge)

# 라이브러리 불러오기
import pandas as pd


# IPython 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)        # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)       # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)     # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('../../datasets/part6/stock price.xlsx')
df2 = pd.read_excel('../../datasets/part6/stock valuation.xlsx')

print(df1)
print()
print(df2)
# %%
# 1. 데이터프레임 합치기 - 교집합
# on=None 옵션 : 두 데이터프레임에 공통으로 속하는 모든 열을 기준(키)으로 병합한다는 뜻
# how='inner' 옵션 : 기준이 되는 열의 데이터가 양쪽 데이터프레임에 공통으로 존재하는 교집합일 경우에만 추출한다는 뜻
merge_inner = pd.merge(df1, df2)    # 'id' 열을 기준으로 병합되어 출력
print(merge_inner)
# %%

# 2. 데이터프레임 합치기 - 합집합
# on='id' 옵션 : 두 데이터프레임의 공통 열 중 'id'열을 키로 병합한다는 뜻
# how='outer' 옵션 : 기준이 되는 'id'열의 데이터가 데이터프레임 어느 한쪽에만 속하더라도 포함한다는 뜻
# 없는 데이터는 NaN값이 지정됨
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer)
# %%

# 3. 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리
# how='left' 옵션 : 왼쪽 데이터프레임의 키 열에 속하는 데이터 값을 기준으로 병합
# left_on과 right_on 옵션을 사용하여 좌우 데이터프레임에 각각 다르게 키를 지정할 수 있다.

merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')
print(merge_left)
# %%

# 4. 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리
# how='right' 옵션 : 오른쪽 데이터프레임의 키 열을 기준으로 추출
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right)
# %%

# 5. 불린 인덱싱과 결합하여 원하는 데이터 찾기
# 주가가 50,000원 미만인 종목 찾기
price = df1[df1['price'] < 50000]
print(price.head())
print()

value = pd.merge(price, df2)
print(value)
# %%
