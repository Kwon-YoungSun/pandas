#%%
### 파이차트
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('../../datasets/part4/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# 데이터 개수 카운트를 위해 값 1을 가진 열 추가
df['count'] = 1
df_origin = df.groupby('origin').sum()      # origin 열을 기준으로 그룹화, 합계 연산
print(df_origin.head())                     # 그룹 결과 연산 출력

# 제조국가(origin) 값을 실제 지역명으로 변경
df_origin.index = ['USA', 'EU', 'JPN']

# 제조국가(origin) 열에 대한 파이 차트 그리기 - count 열 데이터 사용
df_origin['count'].plot(kind='pie',
                        figsize=(7,5),
                        autopct='%1.1f%%',                                  # 퍼센트 % 표시
                        startangle=10,                                      # 파이 조각을 나누는 시작점(각도 표시)
                        colors=['chocolate', 'bisque', 'cadetblue']         # 색상 리스트
                        )

plt.title('Model Origin', size=20)
plt.axis('equal')       # 파이 차트의 비율을 같게(원에 가깝게) 조정
plt.legend(labels=df_origin.index, loc='upper right')       # 범례 표시
plt.show()
# %%
