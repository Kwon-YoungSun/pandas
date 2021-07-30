# 위키피디아에서 미국 ETF 리스트 데이터를 가져와 데이터프레임으로 변환하는 예제 코드
from typing import Text
from bs4 import BeautifulSoup       # 웹 크롤링 모듈
import requests                     # 파이썬에서 HTTP 요청을 보내는 모듈
import re                           # 정규표현식 모듈
import pandas as pd

# 위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
reap = requests.get(url)
soup = BeautifulSoup(reap.text, 'lxml')
rows = soup.select('div > ul > li')

etfs = {}
for row in rows:

    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)

        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]      ### 리스트를 원소로 갖는 딕셔너리를 정의하는 방법
                    # 열                # 행            # 행
    except AttributeError as err:
        pass

# etfs 딕셔너리 출력
print(etfs)
print('\n')

# etfs 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)
print(df)