import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: 한국의 행정 경계 데이터 불러오기
# GeoJSON 파일은 https://github.com/southkorea/southkorea-maps 에서 다운로드 가능
korea_admin_boundaries = "./geo_kr/skorea-municipalities-2018-geo.json"

gdf = gpd.read_file(korea_admin_boundaries)

# Step 2: 지역별 평균 최저 기온 데이터 추가 (예시 데이터)
# 실제 기온 데이터를 기상청 또는 관련 기관에서 확보 후 사용
# temperature_data = {
#     'region': ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Jeju'],
#     'avg_min_temp': [-15.0, -6.0, -8.0, -12.0, -8.0, -10.0, -6.0, -2.0]  # 가상의 평균 최저 기온
# }

src = [
['안동시', 'Andong-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['안산시', 'Ansan-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['안성시', 'Anseong-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['안양시', 'Anyang-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['아산시', 'Asan-si',			"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['보령시', 'Boryeong-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['부천', 'Bucheon',			"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['부산', 'Busan',				"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['창원', 'Changwon',			"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['천안시', 'Cheonan-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['청주시', 'Cheongju-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['춘천시', 'Chuncheon-si',	"hz6b","Zone 6b: -20.6&deg;C to -17.8&deg;C",],
['충주시', 'Chungju-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['대구', 'Daegu',				"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['대전', 'Daejeon',			"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['당진시', 'Dangjin-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['동두천시', 'Dongducheon-si', "hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['동해시', 'Donghae-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['강진군', 'Gangjin-gun',		"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['강릉시', 'Gangneung-si',	"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['거제시', 'Geoje-si',		"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['김천시', 'Gimcheon-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['김해', 'Gimhae',			"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['김제', 'Gimje',				"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['김포시', 'Gimpo-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['공주시', 'Gongju-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['고양', 'Goyang',			"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['구미시', 'Gumi-si',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['군포시', 'Gunpo-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['군산시', 'Gunsan-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['구리시', 'Guri-si',			"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['과천시', 'Gwacheon-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['광주', 'Gwangju',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['광주시', 'Gwangju-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['광명시', 'Gwangmyeong-si',	"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['광양시', 'Gwangyang-si',	"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['경주시', 'Gyeongju-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['경산시', 'Gyeongsan-si',	"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['계룡시', 'Gyeryong-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['하남시', 'Hanam-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['화성시', 'Hwaseong-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['이천시', 'Icheon-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['익산시', 'Iksan-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['인천', 'Incheon',			"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['제천시', 'Jecheon-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['제주시', 'Jeju-si',			"hz9b","Zone 9b: -3.9&deg;C to -1.1&deg;C",],
['정읍시', 'Jeongeup-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['전주', 'Jeonju',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['진주시', 'Jinju-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['밀양', 'Miryang',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['목포시', 'Mokpo-si',		"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['문경시', 'Mungyeong-si',	"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['나주시', 'Naju-si',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['남원', 'Namwon',			"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['남양주시', 'Namyangju-si',	"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['논산시', 'Nonsan-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['오산', 'Osan',				"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['파주', 'Paju',				"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['포천시', 'Pocheon-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['포항시', 'Pohang-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['평택', 'Pyeongtaek',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['사천시', 'Sacheon-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['삼척시', 'Samcheok-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['상주시', 'Sangju-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['세종', 'Sejong',			"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['성남시', 'Seongnam-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['서산시', 'Seosan-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['서울', 'Seoul',				"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['시흥시', 'Siheung-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['속초시', 'Sokcho-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['순천시', 'Suncheon-si',		"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['수원시', 'Suwon-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['태백', 'Taebaek',			"hz6b","Zone 6b: -20.6&deg;C to -17.8&deg;C",],
['통영시', 'Tongyeong-si',	"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['울산', 'U;san',				"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['의정부시', 'Uijeongbu-si',	"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['의왕', 'Uiwang',			"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['원주시', 'Wonju-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['양주시', 'Yangju',			"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['양산', 'Yangsan',			"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['여주시', 'Yeoju-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C",],
['영천시', 'Yeongcheon-si',	"hz8a","Zone 8a: -12.2&deg;C to -9.4&deg;C",],
['영주시', 'Yeongju-si',		"hz7b","Zone 7b: -15&deg;C to -12.2&deg;C",],
['여수', 'Yeosu',				"hz8b","Zone 8b: -9.4&deg;C to -6.7&deg;C",],
['용인시', 'Yongin-si',		"hz7a","Zone 7a: -17.8&deg;C to -15&deg;C"],
]

dst = [
['종로구',],
['중구',],
['용산구',],
['성동구',],
['광진구',],
['동대문구',],
['중랑구',],
['성북구',],
['강북구',],
['도봉구',],
['노원구',],
['은평구',],
['서대문구',],
['마포구',],
['양천구',],
['강서구',],
['구로구',],
['금천구',],
['영등포구',],
['동작구',],
['관악구',],
['서초구',],
['강남구',],
['송파구',],
['강동구',],
['서구',],
['동구',],
['영도구',],
['부산진구',],
['동래구',],
['남구',],
['북구',],
['해운대구',],
['사하구',],
['금정구',],
['연제구',],
['수영구',],
['사상구',],
['기장군',],
['수성구',],
['달서구',],
['달성군',],
['연수구',],
['남동구',],
['부평구',],
['계양구',],
['강화군',],
['옹진군',],
['광산구',],
['유성구',],
['대덕구',],
['울주군',],
['세종시',],
['수원시장안구',],
['수원시권선구',],
['수원시팔달구',],
['수원시영통구',],
['성남시수정구',],
['성남시중원구',],
['성남시분당구',],
['의정부시',],
['안양시만안구',],
['안양시동안구',],
['부천시',],
['광명시',],
['평택시',],
['동두천시',],
['안산시상록구',],
['안산시단원구',],
['고양시덕양구',],
['고양시일산동구',],
['고양시일산서구',],
['과천시',],
['구리시',],
['남양주시',],
['오산시',],
['시흥시',],
['군포시',],
['의왕시',],
['하남시',],
['용인시처인구',],
['용인시기흥구',],
['용인시수지구',],
['파주시',],
['이천시',],
['안성시',],
['김포시',],
['화성시',],
['광주시',],
['양주시',],
['포천시',],
['여주시',],
['연천군',],
['가평군',],
['양평군',],
['춘천시',],
['원주시',],
['강릉시',],
['동해시',],
['태백시',],
['속초시',],
['삼척시',],
['홍천군',],
['횡성군',],
['영월군',],
['평창군',],
['정선군',],
['철원군',],
['화천군',],
['양구군',],
['인제군',],
['고성군',],
['양양군',],
['충주시',],
['제천시',],
['청주시상당구',],
['청주시서원구',],
['청주시흥덕구',],
['청주시청원구',],
['보은군',],
['옥천군',],
['영동군',],
['진천군',],
['괴산군',],
['음성군',],
['단양군',],
['증평군',],
['천안시동남구',],
['천안시서북구',],
['공주시',],
['보령시',],
['아산시',],
['서산시',],
['논산시',],
['계룡시',],
['당진시',],
['금산군',],
['부여군',],
['서천군',],
['청양군',],
['홍성군',],
['예산군',],
['태안군',],
['전주시완산구',],
['전주시덕진구',],
['군산시',],
['익산시',],
['정읍시',],
['남원시',],
['김제시',],
['완주군',],
['진안군',],
['무주군',],
['장수군',],
['임실군',],
['순창군',],
['고창군',],
['부안군',],
['목포시',],
['여수시',],
['순천시',],
['나주시',],
['광양시',],
['담양군',],
['곡성군',],
['구례군',],
['고흥군',],
['보성군',],
['화순군',],
['장흥군',],
['강진군',],
['해남군',],
['영암군',],
['무안군',],
['함평군',],
['영광군',],
['장성군',],
['완도군',],
['진도군',],
['신안군',],
['포항시남구',],
['포항시북구',],
['경주시',],
['김천시',],
['안동시',],
['구미시',],
['영주시',],
['영천시',],
['상주시',],
['문경시',],
['경산시',],
['군위군',],
['의성군',],
['청송군',],
['영양군',],
['영덕군',],
['청도군',],
['고령군',],
['성주군',],
['칠곡군',],
['예천군',],
['봉화군',],
['울진군',],
['울릉군',],
['진주시',],
['통영시',],
['사천시',],
['김해시',],
['밀양시',],
['거제시',],
['양산시',],
['창원시의창구',],
['창원시성산구',],
['창원시마산합포구',],
['창원시마산회원구',],
['창원시진해구',],
['의령군',],
['함안군',],
['창녕군',],
['남해군',],
['하동군',],
['산청군',],
['함양군',],
['거창군',],
['합천군',],
['제주시',],
['서귀포시',],
]

for d in dst :
    for s in src :
        if s[0] == d[0]:
            d.append(s[2])
    if len(d) == 1:
        d.append('hz7b')


hardzone = {
    'region':[],
    'hzone':[]
    }

for c in dst :
#    if len(c) < 2 : continue

    hardzone['region'].append(c[0].strip())
    hardzone['hzone'].append(c[1].strip())

df_temp = pd.DataFrame(hardzone)

# # Step 3: 내한성 존 할당 (USDA 기준 적용)
# def assign_hardiness_zone(temp):
#     if temp <= -23.3:
#         return "Zone 6"
#     elif temp <= -17.8:
#         return "Zone 7"
#     elif temp <= -12.2:
#         return "Zone 8"
#     elif temp <= -6.7:
#         return "Zone 9"
#     else:
#         return "Zone 10"

# df_temp['hzone'] = df_temp['avg_min_temp'].apply(assign_hardiness_zone)
# 한국의 행정 구역별 내한성 (Hardiness Zone) 값을 가정


# Step 4: 병합 전 이름 정리
# gdf['name'] = gdf['name'].str.strip()
# df_temp['region'] = df_temp['region'].str.strip()

# Step 5: 기온 데이터를 GeoDataFrame에 병합
# 지역 이름이 일치하는 컬럼 기준으로 병합
gdf = gdf.merge(df_temp, left_on='name', right_on='region', how='left')

for g in gdf['name'].unique() :
    print(g+',')  # GeoDataFrame의 지역 이름
# print(df_temp['region'].unique())  # 기온 데이터의 지역 이름


# Step 65: 내한성 지도 시각화
fig, ax = plt.subplots(1, 1, figsize=(10, 14))

gdf.plot(column='hzone',
        cmap='coolwarm',
        legend=True,
        edgecolor="black",
        linewidth=0.9,
        ax=ax)

# 지도 타이틀 추가
plt.title("Korean Plant Hardiness Zones", fontsize=15)
plt.axis("off")
plt.show()

plt.waitforbuttonpress()