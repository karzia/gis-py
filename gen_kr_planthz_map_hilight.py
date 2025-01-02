import folium
import geopandas as gpd

# Step 1: GeoJSON 파일과 색상 정의
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
colors = {
    "KR_HZ_5a": "#77A7F0",
    "KR_HZ_5b": "#77DCFD",
    "KR_HZ_6a": "#779FB7",
    "KR_HZ_6b": "#DCF1CB",
    "KR_HZ_7a": "#A2F97D",
    "KR_HZ_7b": "#8AB37D",
    "KR_HZ_8a": "#F7F97D",
    "KR_HZ_8b": "#F7CE7D",
    "KR_HZ_9a": "#B19F7D",
    "KR_HZ_9b": "#CB797D",
}

highlightStyle = {
    "fillColor": "green",
    "fillOpacity": 0.5,
    "weight": 2,
    "opacity": 1.0,
    "color": "green",
}

# 지도 생성
m = folium.Map(location=[36.2635727, 128.0286009], zoom_start=7,
               no_touch=True)

# GeoJSON 레이어 추가
geojson_layers_js = []
for f in hzfiles:
    gd = gpd.read_file('./geo/' + f)
    key = f.split('.')[0]  # 파일 이름에서 키 추출 (예: KR_HZ_5a)
    layer = folium.GeoJson(
        gd,
        name=key,
        style_function=lambda x, col=colors[key]: {
            "fillColor": col,
            "fillOpacity": 0.7,
            "weight": 0.7,
            "opacity": 0.9,
            "color": col,
        },
        highlight_function=lambda x: highlightStyle,
    )
    layer.add_to(m)

    # JavaScript에 사용할 레이어 정보 저장
    geojson_layers_js.append(f'"{key}": {layer.get_name()}')

# 범례(legend) 추가 - JavaScript 사용
legend_html = """
<div id="legend" style="
    position: fixed; 
    bottom: 50px; left: 50px; width: 200px; height: 350px; 
    background-color: white; z-index:9999; font-size:14px; 
    border:2px solid grey; padding: 10px;">
    <b>범례 (Legend)</b><br>
"""

for key, color in colors.items():
    legend_html += f"""
    <div onclick="highlightFeature('{key}')" style="cursor: pointer;">
        <i style="background: {color}; width: 10px; height: 10px; display: inline-block;"></i> {key}<br>
    </div>
    """

legend_html += """
</div>

<script>
    // URL에서 highlight 파라미터를 읽어 특정 레이어 강조
    function getHighlightParam() {
        const params = new URLSearchParams(window.location.search);
        return params.get('highlight');
    }

    // 특정 레이어 강조
    function highlightFeature(key) {
        Object.keys(window.geojsonLayers).forEach(function(layerKey) {
            // 기본 스타일로 복원
            window.geojsonLayers[layerKey].resetStyle();
        });

        // 선택된 피처 하이라이트
        if (window.geojsonLayers[key]) {
            window.geojsonLayers[key].setStyle({
                fillOpacity: 0.5,
                opacity: 1.0,
                weight: 3,
                fillColor: "green",
                color: "green",
            });
        }
    }

    // 페이지 로드 시 highlight 파라미터로 특정 레이어 강조
    document.addEventListener('DOMContentLoaded', function() {
        const highlightKey = getHighlightParam();
        if (highlightKey && window.geojsonLayers[highlightKey]) {
            highlightFeature(highlightKey);
        }
    });
</script>
"""

# JavaScript에서 사용할 GeoJSON 레이어 추가 (window.onload 사용)
geojson_layers_script = f"""
    document.addEventListener(
    'DOMContentLoaded',
    function() {{
        window.geojsonLayers = {{
            {', '.join(geojson_layers_js)}
        }};

        const highlightKey = getHighlightParam();
        if (highlightKey && window.geojsonLayers[highlightKey]) {{
            highlightFeature(highlightKey);}}
        }}
    )
"""

# 범례와 JavaScript 추가
m.get_root().html.add_child(folium.Element(legend_html))
m.get_root().script.add_child(folium.Element(geojson_layers_script))

# 결과 저장
folium.TileLayer().add_to(m)
folium.LayerControl().add_to(m)
m.save("map6.html")