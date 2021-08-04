#%%
### 히트맵

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# heatmap() 메서드: 2개의 범주형 변수를 각각 x, y축에 놓고 데이터를 매트리스 형태로 분류
# 이 때 한 변수(sex)를 행 인덱스로, 나머지 변수(class)를 열 이름으로 설정한다.

# 피벗테이블(커다란 표(예: 데이터베이스, 스프레드시트, 비즈니스 인텔리전스 프로그램 등)의 데이터를 요약하는 통계표)로 범주형 변수를 각각 행, 열로 재구분하여 정리
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')       # aggfunc='size' 옵션은 데이터 값의 크기를 기준으로 집계한다는 뜻

print(table.head())
# 히트맵 그리기
sns.heatmap(table,                  # 데이터프레임
            annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu',          # 컬러 맵
            linewidths=5,           # 구분 선
            cbar=False)             # 컬러 바 표시 여부

plt.show()

# %%
