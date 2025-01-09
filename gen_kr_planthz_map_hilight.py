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

hzones = {
    "KR_HZ_5a": {'color':"#77A7F0", 'desc':'-28.9°C to -26.1°C'},
    "KR_HZ_5b": {'color':"#77DCFD", 'desc':'-26.1°C to -23.3°C'},
    "KR_HZ_6a": {'color':"#779FB7", 'desc':'-23.3°C to -20.6°C'},
    "KR_HZ_6b": {'color':"#DCF1CB", 'desc':'-20.6°C to -17.8°C'},
    "KR_HZ_7a": {'color':"#A2F97D", 'desc':'-17.8°C to -15°C'},
    "KR_HZ_7b": {'color':"#8AB37D", 'desc':'-15°C to -12.2°C'},
    "KR_HZ_8a": {'color':"#F7F97D", 'desc':'-12.2°C to -9.4°C'},
    "KR_HZ_8b": {'color':"#F7CE7D", 'desc':'-9.4°C to -6.7°C'},
    "KR_HZ_9a": {'color':"#B19F7D", 'desc':'-6.7°C to -3.9°C'},
    "KR_HZ_9b": {'color':"#CB797D", 'desc':'-3.9°C to -1.1°C'},
}

highlightStyle = {
    "fillColor": "green",
    "fillOpacity": 0.5,
    "weight": 2,
    "opacity": 1.0,
    "color": "green",
}

# 지도 생성
m = folium.Map(location=[36.2635727, 128.0286009], zoom_start=7, no_touch=True)

# GeoJSON 레이어 추가
geojson_layers_js = []
for f in hzfiles:
    gd = gpd.read_file('./geo/' + f)
    key = f.split('.')[0]  # 파일 이름에서 키 추출 (예: KR_HZ_5a)
    layer = folium.GeoJson(
        gd,
        name=key,
        style_function=lambda x, col=hzones[key]['color']: {
            "fillColor": col,
            "fillOpacity": 0.7,
            "weight": 0.7,
            "opacity": 0.9,
            "color": col,
        },
     #   highlight_function=lambda x: highlightStyle,
    )
    layer.add_to(m)

    # JavaScript에 사용할 레이어 정보 저장
    geojson_layers_js.append(f'"{key}": {layer.get_name()}')

# 범례(legend) 추가 - JavaScript 사용
legend_html = """
<div id="legend" style="
    position: fixed; 
    bottom: 50px; left: 50px; width: fit-content; height: 350px; 
    background-color: white; z-index:9999; font-size:14px; 
    border:2px solid grey; padding: 10px;">
    <b>범례 (Legend)</b><br>
"""

for key, val in hzones.items():
    legend_html += f"""
    <div id="legend-item-{key}" onclick="highlightFeature('{key}')" style="cursor: pointer; padding: 5px;">
        <i style="background: {val['color']}; width: 10px; height: 10px; display: inline-block;"></i> {key} ({val['desc']})<br>
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

    // 선택된 Legend의 배경색 변경
    let previouslySelectedLegend = null;

    function highlightLegend(key) {

        if (previouslySelectedLegend) {
            // 이전 선택된 Legend 항목 초기화
            previouslySelectedLegend.style.backgroundColor = "";
        }

        const selectedLegend = document.getElementById(`legend-item-${key}`);
        if(selectedLegend == previouslySelectedLegend){
            previouslySelectedLegend.style.backgroundColor = "";
            previouslySelectedLegend = null;
            return;
        }
        if (selectedLegend) {
            selectedLegend.style.backgroundColor = "lightgreen";
            previouslySelectedLegend = selectedLegend;
        }

    }

    // 특정 레이어 강조
    function highlightFeature(key) {
        // Legend 배경색 변경
        highlightLegend(key);

        // 기본 스타일로 복원
        Object.keys(window.geojsonLayers).forEach(function(layerKey) {
            
            window.geojsonLayers[layerKey].resetStyle();
        });
        
        if(previouslySelectedLegend === null) return;

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
            highlightFeature(highlightKey);
        }}
    }}
    );
"""

# 범례와 JavaScript 추가
m.get_root().html.add_child(folium.Element(legend_html))
m.get_root().script.add_child(folium.Element(geojson_layers_script))

# 결과 저장
folium.TileLayer().add_to(m)
folium.LayerControl().add_to(m)
m.save("map.html")
