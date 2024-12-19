import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: 한국의 행정 경계 데이터 불러오기
# GeoJSON 파일은 https://github.com/southkorea/southkorea-maps 에서 다운로드 가능
# korea_admin_boundaries = "skorea-municipalities-2018-geo.json"
hzfiles = [
    'KR_HZ_5a.geojson',
    'KR_HZ_5b.geojson',
    'KR_HZ_6a.geojson',
    'KR_HZ_6b.geojson',
    'KR_HZ_7a.geojson',
    'KR_HZ_7b.geojson',
    'KR_HZ_8a.geojson',
    'KR_HZ_8b.geojson',
    'KR_HZ_9a.geojson',
    'KR_HZ_9b.geojson',
]

gdfs = []
for f in hzfiles:
    gd = gpd.read_file('./geo/'+f)
#    title = f.split('.')[0]
    gdfs.append(gd)


full = gpd.GeoDataFrame(pd.concat(gdfs,ignore_index=True))

# Step 65: 내한성 지도 시각화
# 각 data를 따로 표현



fig, ax = plt.subplots(1, len(gdfs), figsize=(10, 14))

i=0
for gdf in gdfs:
    full.plot(
            column='pm_icon',
            #cmap='Grey',
            color='gray',
            #legend=True,
            edgecolor="black",
            linewidth=0.1,
            #alpha=0.3,
            ax=ax[i])
   
    gdf.plot(
            color='gold',  # 특정 구간 강조 색상
            edgecolor="black",
            legend=True,
            linewidth=1.0,
            alpha=1.0,
            ax=ax[i])
    
    i+=1


# highlight = gdf[gdf['pm_icon'] == 'KR_7a']

# highlight.plot( 
#     color='gold',  # 특정 구간 강조 색상
#     edgecolor="black",
#     linewidth=1.2,
#     ax=ax)

# 지도 타이틀 추가
#plt.title("Korean Plant Hardiness Zones", fontsize=11)
#plt.axis("off")
plt.show()

#plt.waitforbuttonpress()