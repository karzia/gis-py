import folium
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geodatasets


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

# Step 2: data frame 합치기
gdf = gpd.GeoDataFrame(pd.concat(gdfs,ignore_index=True))





fig, ax = plt.subplots(1, 1, figsize=(10, 14))

# Step 3: 내한성 지도 시각화

# tile 종류 : https://leaflet-extras.github.io/leaflet-providers/preview/
m = gdf.explore(
    #tiles=None,
    tiles= "OpenTopoMap",
    #tiles= "Stadia.StamenWatercolor",

    column="pm_icon",  # make choropleth based on "POP2010" column
    scheme="naturalbreaks",  # use mapclassify's natural breaks scheme
    cmap='coolwarm',
    legend=True,  # show legend
    k=20,  # use 10 bins
    tooltip=False,  # hide tooltip
    #popup=["POP2010", "POP2000"],  # show popup (on-click)
    legend_kwds=dict(colorbar=False),  # do not use colorbar
    name="Hardness Zone",  # name of the layer in the map
    )

# m = gdf.explore(
#         column='pm_icon',
#         cmap='coolwarm',
#         legend=True,
#         edgecolor="black",
#         linewidth=0.9,
#         alpha=0.3,
#         ax=ax)
# highlight = gdf[gdf['pm_icon'] == 'KR_7a']

# highlight.plot( 
#     color='gold',  # 특정 구간 강조 색상
#     edgecolor="black",
#     linewidth=1.2,
#     ax=ax)


folium.TileLayer().add_to(m)
folium.LayerControl().add_to(m)

m.save("map.html")
