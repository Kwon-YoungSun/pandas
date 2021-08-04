#%%
### 지도 만들기

# 라이브러리 불러오기
import folium

# 서울 지도 만들기
# Map() 함수를 이용하면 간단하게 지도 객체를 만들 수 있음
# 단, 오직 웹 환경에서만 지도를 확인할 수 있음
seoul_map = folium.Map(location=[37.55,126.98], zoom_start=12)  # zoom_start: 화면 확대 비율

# 지도를 HTML 파일로 저장하기
seoul_map.save('./seoul.html')
# %%
