#%%
### 누락 데이터 제거
# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# for 반복문으로 각 열의 NaN 개수 확인하기
missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()      # 각 열의 NaN 개수 파악
    try:
        print(col, ': ', missing_count[True])           # NaN값이 있으면 개수 출력(isnull == True)
    except:
        print(col, ': ', 0)                             # NaN값이 없으면 0개 출력

# NaN값이 500 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN값)
# dropna() 메소드에 thresh=500 옵션 적용
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

# age 열에 나이 데이터가 없는 모든 행 삭제 - age 열(891개 중 177개의 NaN값)
# dropna() 메소드에 subset을 'age'로 한정하면, 'age' 열의 행 중에서 NaN값이 있는 모든 행(axis=0)을 삭제
# 이 때 기본값으로 how='any' 옵션이 적용되는데, NaN값이 하나라도 존재하면 삭제한다는 뜻
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

# %%
