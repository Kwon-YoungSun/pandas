#%%

### 지도에 마커 표시하기
import pandas as pd
import folium

# 대학교 리스트를 데이터프레임으로 변환
df = pd.read_excel('../../datasets/part4/서울지역 대학교 위치.xlsx', index_col=0)
print(df.head())

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)

# 대학교 위치 정보를 Marker로 표시
# Marker 위치를 표시하려면 Marker() 함수에 위도, 경도 정보를 전달한다.
# popup 옵션을 추가하면 마커를 클릭했을 때 팝업창에 표시해주는 텍스트를 넣을 수 있음
for name, lat, lng in zip(df.index, df.위도, df.경도):          # zip 함수: 매개변수들의 데이터를 zip 형태로 엮어줌(https://www.daleseo.com/python-zip/)
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('./seoul_colleges.html')
# %%
