#%%
### 범주형 데이터의 산점도
# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')

# 스타일 테마 설정
sns.set_style('whitegrid')

# 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
fig = plt.figure(figsize=(15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# 이산형 변수의 분포 - 데이터 분산 미고려
# stripplot() 함수는 데이터 분산을 고려하지 않음
sns.stripplot(x="class",            # x축 변수
              y="age",              # y축 변수
              data=titanic,         # 데이터셋 - 데이터프레임
              ax=ax1,               # axe 객체 - 1번째 그래프
              #hue='sex'#           # 남녀 성별을 색상으로 구분하여 출력
              )               

# 이산형 변수의 분포 - 데이터 분산 고려(중복 X)
# swarmplot은 데이터 분산까지 고려하여, 데이터 포인트가 서로 중복되지 않도록 그림
# 즉, 데이터가 퍼져 있는 정도를 입체적으로 볼 수 있음
sns.swarmplot(x="class",            # x축 변수
              y="age",              # y축 변수
              data=titanic,         # 데이터셋 - 데이터프레임
              ax=ax2)               # axe 객체 - 2번째 그래프

# 차트 제목 표시
ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()
# %%
