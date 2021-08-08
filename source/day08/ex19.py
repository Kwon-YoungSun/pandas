#%%

### 멀티 인덱스

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열, sex 열을 기준으로 정렬
grouped = df.groupby(['class', 'sex'])

# 그룹 객체에 연산 메소드 적용
gdf = grouped.mean()
print(gdf)
print()
print(type(gdf))
# %%
# class 값이 First인 행을 선택하여 출력
print(gdf.loc['First'])
# %%
# class 값이 First이고, sex 값이 female인 행을 선택하여 출력
# loc 인덱서를 이용하여 인자로는 투플 형태로 각 인덱스에서 찾는 값을 전달한다.
print(gdf.loc[('First', 'female')])
# %%

# sex 값이 male인 행을 선택하여 출력
# 남성 승객에 한정하여 객실별로 그룹을 만들어서 분석할 수 있다.
print(gdf.xs('male', level='sex'))
# %%
