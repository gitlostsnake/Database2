import folium
import pandas as pd
import webbrowser


data = pd.read_csv("roadlocationdata.csv")
fg = folium.FeatureGroup(name="My Map")
"""Get a marker post for taper and length of a job and calculate
   stock items then plot it onto a folium map."""
latdata = list(data['lat'])
londata = list(data['lng'])


# lat and lon have to be floats to work so far..
# take taper location and work backwards to get sign locations
def advanced_warning_signs(lat, lon):
    found = data[data.lat == lat]
    bingo = found[found.lng == lon]
    taper_marker = list(bingo['BD'])
    taper_area = list(bingo['Area'])
    taper_road = list(bingo['DD'])
    startingpoint = taper_marker[0][0]
    endingpoint = taper_marker[0][-1]
    middlepoint = taper_marker[0][1:-1]
    print(startingpoint)
    print(endingpoint)
    print(middlepoint)
    if taper_marker[0][-1] == 'A':
        # Taper is on a northbound or away from london road..
        # So warning signs will be on on a markerpost with higher numbers
        # And the end of works will be on a lower number because it is closer to
        # London..
        pass


    print("And finally lets see whats going on here")

    print(lat)
    print(lon)
    print(type(lat))
    print(type(lon))
    print("Found")
    print(found)
    print(type(found))
    print("Bingo")
    print(bingo)
    print(type(bingo))

    print(f"Taper location is {taper_marker[0]}")
    print(f"{taper_marker[0][-1]}")
    print(f"Taper location in area {taper_area[0]}")
    print(f"Taper is on the {taper_road[0]} road")


advanced_warning_signs(50.923557,-3.3475650000000003)
