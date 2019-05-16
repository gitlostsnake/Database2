import folium
import pandas as pd

data = pd.read_csv("roadlocationdata.csv")
df = pd.DataFrame(data)
lat = list(data["lat"])
lon = list(data["lng"])
markerpostlist = list(data["BD"])
area = list(data["Area"])
fg = folium.FeatureGroup(name="My Map")


def findmp2(markerpost, area):
    data[(data.BD == str("P"+markerpost)) & (data.Area == area)]
    print(data)


def findmp(markerpost, bound, area):

    if bound == "North Bound":
        Last = "B"
        search = df.loc[df['BD'] == str("P"+ markerpost + Last) & df['Area'] == area]
    else:
        Last = "A"
        search = df.loc[df['BD'] == str("P"+ markerpost + Last) & df['Area'] == area]


    if len(search) > 1:
        print("Marker posts found!!!")
        print(search)
        lat = list(search['lat'])
        lon = list(search['lng'])
        markerp = list(search['BD'])
        for lt, ln, mp in zip(lat,lon, markerp):
            fg.add_child(folium.Marker(location=[lt,ln], popup=(str(lt) +' '+ str(ln)), icon=folium.Icon(color='red')))

    elif len(search) == 0:
        print("No markerposts found... ")

    else:
        print("One of a kind")
        lat= list(search['lat'])
        lon= list(search['lng'])
        markerp = list(search['BD'])
        for lt, ln, mp in zip(lat,lon, markerp):
            fg.add_child(folium.Marker(location=[lt,ln], popup=str(mp)+ str(lt,ln),
                                        icon=folium.Icon(color='green')))

findmp2("1/9", "AREA14")

map = folium.Map(location=[54.880268, -1.560417], zoom_start=8)

# for lt, ln, mp in zip(lat, lon, markerpost):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(mp), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
print("Map updated go have a look.")
