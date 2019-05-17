import folium
import pandas as pd

data = pd.read_csv("roadlocationdata.csv")
df = pd.DataFrame(data)
lat = list(data["lat"])
lon = list(data["lng"])
markerpostlist = list(data["BD"])
area = list(data["Area"])
fg = folium.FeatureGroup(name="My Map")

def findmp(markernumber, bound, area):
    """
       First take markerpost and search for it in the dataframe.
       Then, search the markerpost True list for the right area.
    """
    last = []
    if bound == "North bound":
        last.append("A")

    else:
        last.append("B")

    print(last)
    markerpost = str("P" + markernumber + last[0])
    markerpostfound = data[data.BD == markerpost]
    print(markerpostfound)
    print(f"Found {len(markerpostfound)} results that match the markerpost")
    bingo = markerpostfound[markerpostfound.Area == area]
    print(f"Found {len(bingo)} results that match the markerpost and area")
    print(bingo)

    """Take the bingo list which is a pandas df and get the right info to plot on folium map."""

    lat = list(bingo['lat'])
    lon = list(bingo['lng'])
    markerp = list(bingo['BD'])
    for lt, ln, mp in zip(lat,lon, markerp):
        fg.add_child(folium.Marker(location=[lt,ln], popup=(str(lt) +' '+ str(ln)), icon=folium.Icon(color='red')))
        map.save("Map1.html")
        view = map.open("Map1.html")
        print(view.read())







def findmp21(markerpost, bound, area):
    if bound == "North Bound":
        Last = "A"
        search = df.loc[df['BD'] == str("P"+ markerpost + Last) & df['Area'] == area]
    else:
        Last = "B"
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

map = folium.Map(location=[54.880268, -1.560417], zoom_start=8)

# for lt, ln, mp in zip(lat, lon, markerpost):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(mp), icon=folium.Icon(color='green')))

map.add_child(fg)

print("Map updated go have a look.")
