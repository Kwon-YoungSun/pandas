#%%
### 그룹 연산 - 분할

# 라이브러리 불러오기
import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

print('승객 수:', len(df))
print(df.head())
print()

# class 열을 기준으로 분할
grouped = df.groupby(['class'])
print(grouped)
# %%

# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print()
# %%

# 연산 메소드 적용
# 이때 연산이 가능한 열에 대해서만 선택적으로 연산을 수행한다.
average = grouped.mean()
print(average)

#%%

# 개별 그룹 선택하기
# get_group() 메소드를 적용하면 특정 그룹만을 선택할 수 있다.
group3 = grouped.get_group('Third')
print(group3.head())
# %%

# class 열, sex 열을 기준으로 분할
# 두 열이 갖는 원소 값들로 만들 수 있는 모든 조합으로 키를 생성한다.
# 그리고 조합된 키를 기준으로 그룹 객체를 만든다.
grouped_two = df.groupby(['class', 'sex'])

# grouped_two 그룹 객체를 iteration으로 출력
# 모두 6개의 키가 조합으로 만들어진다.
for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print()
# %%

# grouped_two 그룹 객체에 연산 메소드 적용
# 키가 되는 2개의 열('class', 'sex')의 값으로부터 2중 멀티 인덱스가 지정됨
average_two = grouped_two.mean()
print(average_two)
print()
print(type(average_two))
# %%

# 멀티 인덱스를 이용하여 특정 그룹만을 골라서 추출하는 방법
# grouped_two 그룹 객체에서 개별 그룹 선택하기
# 인자로 전달하는 키는 투플로 입력
group3f = grouped_two.get_group(('Third', 'female'))
print(group3f.head())
# %%
