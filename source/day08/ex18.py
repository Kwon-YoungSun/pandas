#%%

### 그룹 객체에 함수 매핑

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 정렬
grouped = df.groupby(['class'])

# --------------------------------------------------------------
# 집계: 각 그룹별 요약 통계 정보 집계
agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)
# %%

# z-score를 계산하는 사용자 함수 정의
# transform과의 차이가 무엇인가?
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.apply(z_score)     # 기본값 axis=0
print(age_zscore.head())
# %%

# 필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
print()
for x in age_filter.index:
    if age_filter[x] == True:
        age_filter_df = grouped.get_group(x)
        print(age_filter_df.head())
        print()

# %%
