#%%

### Period 배열
# 라이브러리 불러오기
import pandas as pd

# Period 배열 만들기 - 1개월 길이
pr_m = pd.period_range(start='2019-01-01',          # 날짜 범위 시작
                       end=None,                    # 날짜 범위 끝
                       periods=3,                   # 생성할 Period 개수
                       freq='M')                    # 기간의 길이(M: 월)
print(pr_m)
# %%
# Period 배열 만들기 - 1시간 길이
pr_h = pd.period_range(start='2019-01-01',          # 날짜 범위 시작
                       end=None,                    # 날짜 범위 끝
                       periods=3,                   # 생성할 Period 개수
                       freq='H')                    # 기간의 길이(H: 시간)
print(pr_h)
print()

# Period 배열 만들기 - 2시간 길이
pr_h = pd.period_range(start='2019-01-01',          # 날짜 범위 시작
                       end=None,                    # 날짜 범위 끝
                       periods=3,                   # 생성할 Period 개수
                       freq='2H')                   # 기간의 길이(H: 시간)
print(pr_h)
print()



# %%
