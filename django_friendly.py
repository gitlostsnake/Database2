import folium
import pandas as pd
import webbrowser


data = pd.read_csv('roadlocationdata.csv')
df = pd.DataFrame(data)

fg = folium.FeatureGroup(name="Django_Map")
marker_post = "12/1"
road_name = "A1"
area = "Area 14"

def findmp(marker_post, road_name, area):
    north = "A"
    south = "B"

    north_markerpost = str("P" + marker_post + north)
    south_markerpost = str("P" + marker_post + south)

    found_north = data[data.BD == north_markerpost]
    found_north_road = found_north[found_north.DD == road_name]
    found_north_road_area = found_north_road[found_north_road.Area == area]

    found_south = data[data.BD == south_markerpost]
    found_south_road = found_south[found_south.DD == road_name]
    found_south_road_area = found_south_road[found_south_road.Area == area]

    north_lat = list(found_north_road_area['lat'])
    north_lon = list(found_north_road_area['lng'])
    north_markerpost = list(found_north_road_area['BD'])

    for lt, ln, mp in zip( north_lat, north_lon, north_markerpost):
        fg.add_child(folium.Marker(location=[lt, ln], popup=(str(lt) + ',' + str(ln)), icon=folium.Icon(color='red')))
        map.save(f"{north_markerpost}.html")
        webbrowser.open_new_tab(f"{north_markerpost}.html")

        return f'{north_markerpost}.html'


map = folium.Map(location=[54.880268, -1.560417], zoom_start=8)
map.add_child(fg)


    # south_lat = list(found_south_road_area['lat'])
    # south_lon = list(found_south_road_area['lat'])
