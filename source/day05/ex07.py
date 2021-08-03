#%%

# -*- encoding: utf8 -*-
# ** Matplotlib 한글 폰트 오류 해결
from matplotlib import font_manager, rc, rcParams, style
from numpy import place, sign

font_path = "C:/Windows/Fonts/H2GTRE.TTF"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

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

# ** 차트 제목, 축 이름 추가
# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']

# ** 그래프 꾸미기 추가 - 스타일 서식 지정 등
# 스타일 서식 지정
plt.style.use('ggplot')
# plt.style.use('classic')
# plt.style.use('bmh')
# plt.style.use('dark_background')
# plt.style.use('fast')
# plt.style.use('grayscale')
# plt.style.use('seaborn')

# --------------------------------------------------------------------------------------
### 화면 분할하여 그래프 여러 개 그리기 - axe 객체 활용
# 여러 개의 axe 객체를 만들고, 분할된 화면마다 axe 객체를 하나씩 배정한다. axe 객체는 각각 서로 다른 그래프를 표현할 수 있다.

# 1. figure() 함수를 사용하여 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
# 1-1. figsize 옵션으로 (가로, 세로) 그림틀의 크기 설정
fig = plt.figure(figsize=(10, 10))
# 1-2. fig 객체에 add_subplot() 메소드를 적용하여 그림틀을 여러 개로 분할(행의 크기, 열의 크기, 서브플롯 순서를 순서대로 입력)
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# 2. axe 객체에 plot 함수로 그래프 출력
# 2-1. 첫 번째 그래프(ax1)에 'o' 옵션을 인자로 전달하여 선을 그리지 않고 점으로만 표시
ax1.plot(sr_one, 'o', markersize=10)
# 2-2. 두 번째 그래프(ax2)에 marker='o' 옵션을 사용하여 원 모양의 마커를 가진 선 그래프가 된다.
ax2.plot(sr_one, marker='o', markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울 -> 경기')
# 2-3. ax2 객체에 legend() 메소드를 적용하여 범례 표시
ax2.legend(loc='best')

# y축 범위 지정(최소값, 최대값)
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

# 축 눈금 라벨 지정 및 75도 회전
ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)

plt.show()
# %%
