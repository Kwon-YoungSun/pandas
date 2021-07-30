# JSON 파일 읽기
import pandas as pd
import os

currentPath = os.getcwd()

os.chdir(currentPath + '\source\day03')


# read_json() 함수로 데이터프레임 변환
df = pd.read_json('./read_json_sample.json')
print(df)
print('\n')
print(df.index)