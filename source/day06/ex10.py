#%%
### 조건을 적용하여 화면을 그리드로 분할하기
# * FacetGrid() 함수는 행, 열 방향으로 서로 다른 조건을 적용하여 여러 개의 서브 플롯을 만듦.
# * 그리고 각 서브 플롯에 적용할 그래프 종류를 map() 메소드를 이용하여 그리드 객체에 전달

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# 조건에 따라 그리드 나누기
# 열 방향으로는 'who' 열의 탑승객 구분(man, woman, child) 값으로 구분하고, 
# 행 방향으로는 'survived' 열의 구조 여부(구조 성공=1, 실패=0) 값으로 구분하여 2행 x 3열 모양의 그리드를 만듦
g = sns.FacetGrid(data=titanic, col='who', row='survived')

# 그래프 적용하기
g = g.map(plt.hist, 'age')
# %%
