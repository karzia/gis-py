import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Step 1: 한국의 행정 경계 데이터 불러오기
# GeoJSON or SHP 파일을 불러옵니다 (GeoJSON은 한국 경계 데이터를 쉽게 구할 수 있음)
# https://github.com/southkorea/southkorea-maps 에서 행정구역 GeoJSON을 다운로드할 수 있습니다.
# korea_admin_boundaries = "korea_admin_boundaries.json"  # 파일 경로를 맞게 설정하세요.
# korea_admin_boundaries = "./geo_kr/skorea-municipalities-2018-geo.json"
korea_admin_boundaries = "./geo_kr/skorea-submunicipalities-2018-topo.json"

gdf = gpd.read_file(korea_admin_boundaries)

# Step 2: 임의의 내한성 데이터 추가
# 한국의 행정 구역별 내한성 (Hardiness Zone) 값을 가정
np.random.seed(42)  # 재현 가능한 결과를 위해 설정
gdf['Hardiness_Zone'] = np.random.randint(6, 9, len(gdf))  # 예: 내한성 값 6~9 범위

# Step 3: 지도 그리기
fig, ax = plt.subplots(1, 1, figsize=(10, 14))
gdf.plot(column='Hardiness_Zone',
         cmap='coolwarm',  # 색상 지도 설정
         legend=True,
         edgecolor="black",
         linewidth=0.1,
         ax=ax)

# 지도에 타이틀 추가
plt.title("Korean Plant Hardiness Zones", fontsize=15)
plt.axis("off")  # 축 제거
plt.show()