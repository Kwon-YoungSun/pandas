#%%
### 이변수 데이터의 분포
# pairplot() 함수는 인자로 전달되는 데이터프레임의 열(변수)을 두 개씩 짝을 지을 수 있는 모든 조합에 대해 표현


# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('whitegrid')

# -------------------------------------------------------------------
# titanic 데이터셋 중에서 분석 데이터 선택하기
# 3개의 열을 사용하기 때문에 3행 x 3열 크기로 모두 9개의 그리드를 만듦
# 각 그리드에 두 변수 간의 관계를 나타내는 그래프를 하나씩 그림
titanic_pair = titanic[['age', 'pclass', 'fare']]

# 조건에 따라 그리드 나누기
g = sns.pairplot(titanic_pair)
# %%
