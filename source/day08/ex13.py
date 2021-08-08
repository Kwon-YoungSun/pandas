#%%

### 데이터프레임 합치기(join)

# 라이브러리 불러오기
import pandas as pd

# IPython 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)        # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)       # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)     # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('../../datasets/part6/stock price.xlsx', index_col='id')
df2 = pd.read_excel('../../datasets/part6/stock valuation.xlsx', index_col='id')

# 데이터프레임 결합(join)
# 왼쪽에 위치한 df1의 행 인덱스를 기준으로 결합하는 how='left' 옵션 기본 적용
df3 = df1.join(df2)
print(df3)

# %%
# 데이터프레임 결합(join) - 교집합
# how='inner' 옵션을 이용해서 두 데이터프레임에 공통으로 존재하는 행 인덱스를 기준으로 추출
df4 = df1.join(df2, how='inner')
print(df4)
# %%
