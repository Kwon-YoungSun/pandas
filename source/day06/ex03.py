#%%
### 히스토그램/커널 밀도 그래프

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# titanic 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정(5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

#----------------------------------------------------------------------------------------------------------------------------
# 그래프 객체 생성(figure에 3개의 서브 플롯 생성)
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

# 단변수(하나의 변수) 데이터의 분포를 확인할 때 distplot() 함수를 이용한다.
# 기본값으로 히스토그램과 커널 밀도 함수(그래프와 x축 사이의 면적이 1이 되도록 그리는 밀도 분포 함수)를 그래프로 출력한다.
# 기본값
sns.distplot(titanic['fare'], ax=ax1)

# hist=False: 히스토그램이 표시되지 않음
sns.distplot(titanic['fare'], hist=False, ax=ax2)

# kde=False: 커널 밀도 그래프를 표시하지 않음
sns.distplot(titanic['fare'], kde=False, ax=ax3)

# 차트 제목 표시
ax1.set_title('titanic fare - hist/ked')
ax2.set_title('titanic fare - ked')
ax3.set_title('titanic fare - hist')

# %%
