#%%
### 단위 환산
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('../../datasets/part5/auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horespower', 'weight', 'acceleration', 'model year', 'origin', 'name']
print(df.head(3))
print()

# mpg(mile per gallon)를 kpl(kilometer per liter)로 변환(mpg_to_kpl = 0.425)
# 1마일은 1.60934km이고, 1갤런은 3.78541리터. 따라서 1mpg는 0.425km/L임
mpg_to_kpl = 1.60934/3.78541

# mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
df['kpl'] = df['mpg'] * mpg_to_kpl
print("1--------------------------------------------------------------------------------------")
print(df.head(3))
print("--------------------------------------------------------------------------------------")
print()

# kpl 열을 소수점 아래 둘째자리에서 반올림
df['kpl'] = df['kpl'].round(2)
print("2--------------------------------------------------------------------------------------")
print(df.head(3))
print("---------------------------------------------------------------------------------------")
print()

# kpl 열을 소수점 아래 둘째자리에서 반올림
df['kpl'] = df['kpl'].round(2)
print(df.head(3))
# %%
