# 라이브러리 불러오기
import pandas as pd
import os

currentPath = os.getcwd()
print(currentPath)
os.chdir(currentPath+"\source\day03")       # vscode 상에서는 디렉토리 경로를 수동으로 지정해주어야 함

# 파일 경로(파이썬 파일과 같은 폴더)를 찾고, 변수 file_path에 저장
file_path = './read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환, 변수 df1에 저장
# 기본값으로 0행을 행 지정
df1 = pd.read_csv(file_path)
print(df1)
print('\n')

# read_csv() 함수로 데이터프레임 변환, 변수 df2에 저장. header_None 옵션
# 행을 열 지정하지 않음
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

# read_csv() 함수로 데이터프레임 변환, 변수 df3에 저장, index_col=None 옵션
# 인덱스가 되는 열을 지정하지 않음
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
# 'c0' 열이 인덱스로 지정됨
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
