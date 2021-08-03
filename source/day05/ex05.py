#%%
#-*- encoding: utf8 -*-
# ** Matplotlib 한글 폰트 오류 해결
from matplotlib import font_manager, rc, rcParams, style
from numpy import place, sign

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================================================================================
# seaborn 서식을 사용할 경우 한글폰트 깨짐 해결 방법?
# =====================================================================================================================


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

# ** 차트 제목, 축 이름 추가
# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# -------------------------------------------------------------------------------------
# ** 그래프 꾸미기 추가 - 스타일 서식 지정 등
# 스타일 서식 지정
# plt.style.use('ggplot')
# plt.style.use('classic')
# plt.style.use('bmh')
# plt.style.use('dark_background')
# plt.style.use('fast')
# plt.style.use('grayscale')
plt.style.use('seaborn')

# 그림 사이즈 지정
plt.figure(figsize=(14, 5))

# x축 눈금 라벨 회전하기
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)    # 마커 표시 추가

plt.title('서울 -> 경기 인구 이동') # 차트 제목
plt.xlabel('기간')                  # x축 이름
plt.ylabel('이동 인구수')           # y축 이름

plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=15)         # 범례 표시

plt.show()

# %%
