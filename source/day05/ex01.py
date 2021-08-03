#%%
# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# Excel 데이터를 데이터프레임으로 변환
# df = pd.read_excel('datasets/part4/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)
df = pd.read_excel('../../datasets/part4/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# df = pd.read_excel('../../datasets/part4/시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

# 1. 누락값(NaN)을 앞 데이터로 채움(엑셀 양식 병합 부분)
# fillna() 메소드의 method='ffill' 옵션을 사용하면 누락 데이터가 들어 있는 행의 바로 앞에 위치한 행의 데이터 값으로 채운다.
df = df.fillna(method='ffill')

# 2. '전출지별' 열에서 '서울특별시'라는 값을 갖는 데이터만 추출하여 변수 df_seoul에 저장한다.
# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]

# 3. '전출지별' 열을 삭제
df_seoul = df_seoul.drop(['전출지별'], axis=1)

# 4. '전입지별' 열의 이름을 '전입지'로 바꾼다.
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)

# 5. '전입지' 열을 df_seoul의 행 인덱스로 지정한다.
df_seoul.set_index('전입지', inplace=True)

# 6. df_seoul에서 '전입지'가 '경기도'인 행 데이터를 선택하여 sr_one에 저장한다.
# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# 7. 선 그래프를 그리는 plot() 함수에 입력할 x, y축 데이터 선택
plt.plot(sr_one.index, sr_one.values)
# %%

# 판다스 객체를 plot 함수에 입력(앞의 실행 결과와 같은 결과)
plt.plot(sr_one)
# %%
