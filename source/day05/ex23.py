#%%

### 제조국가별 연비 분포를 보여주는 박스 플롯
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/H2GTRE.TTF"   # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('seaborn-poster')             # 스타일 서식 지정
plt.rcParams['axes.unicode_minus']=False    # 마이너스 부호 출력 설정

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part4/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메소드로 그래프 출력
# 각 axe 객체에 박스 플롯을 그리는 boxplot() 메소드 적용
# origin 값이 1인 mpg열, origin 값이 2인 mpg열, origin 값이 3인 mpg 열의 데이터 분포를 출력
ax1.boxplot(x=[df[df['origin'] == 1]['mpg'],
              df[df['origin'] == 2]['mpg'],
              df[df['origin'] == 3]['mpg']],
            labels=['USA', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin'] == 1]['mpg'],
              df[df['origin'] == 2]['mpg'],
              df[df['origin'] == 3]['mpg']],
            labels=['USA', 'EU', 'JAPAN'],
            vert=False)     # vert=False 옵션을 사용하여 수평 박스 플롯을 그림

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()
# %%
