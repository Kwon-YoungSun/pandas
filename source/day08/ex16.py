#%%

### 그룹 연산 데이터 변환

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# class 열을 기준으로 정렬
grouped = df.groupby(['class'])

# --------------------------------------------------------------
# 그룹별 age 열의 평균 집계 연산
age_mean = grouped.age.mean()
print(age_mean)
print()

# 그룹별 age 열의 표준편차 집계 연산
age_std = grouped.age.std()
print(age_std)
print()

# 1. 첫번째 방법: 그룹 객체의 age 열을 iteration으로 z-score(표준점수)을 계산하여 출력
for key, group in grouped.age:
    group_zscore = (group - age_mean.loc[key]) / age_std.loc[key]
    print('* origin : ', key)
    print(group_zscore.head(3))         # 각 그룹의 첫 3개의 행 출력
    print()
# %%

# 2. 두번째 방법: transform() 메소드를 사용

# 2-1. z-score를 계산하는 사용자 함수 정의
def z_score(x):
    return (x - x.mean()) / x.std()

# 2-2. transform 메소드를 이용하여 age 열의 데이터를 z-score로 변환
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1, 9, 0]])                # 1, 2, 3 그룹의 첫 데이터 확인(변환 결과)
print()
print(len(age_zscore))                          # transform 메소드 반환 값의 길이
print()
print(age_zscore.loc[0:9])                      # transform 메소드 반환 값 출력(첫 10개)
print()
print(type(age_zscore))                         # transform 메소드 반환 객체의 자료형
# %%