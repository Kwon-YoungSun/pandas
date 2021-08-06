#%%
### Timestamp를 Period로 변환

# 라이브러리 불러오기
import pandas as pd

# 날짜 형식의 문자열로 구성되는 리스트 정의
dates = ['2019-01-01', '2020-01-01', '2021-06-01']

# 문자열의 배열(시리즈 객체)을 판다스 Timestamp로 변환
ts_dates = pd.to_datetime(dates)
print(ts_dates)
print()

# Timestamp를 Period로 변환
# to_period() 함수를 이용하면 일정한 기간을 나타내는 Period 객체로 Timestamp 객체를 변환할 수 있다.
# freq 옵션 목록
# 'D' : 1일의 기간
# 'M' : 1개월의 기간
# 'A' : 1년의 기간(12월을 기준으로)

pr_day = ts_dates.to_period(freq='D')
print(pr_day)
pr_month = ts_dates.to_period(freq='M')
print(pr_month)
pr_year = ts_dates.to_period(freq='A')
print(pr_year)
# %%
