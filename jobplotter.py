import folium
import pandas as pd
import webbrowser


data = pd.read_csv("roadlocationdata.csv")
fg = folium.FeatureGroup(name="My Map")
"""Get a marker post for taper and length of a job and calculate
   stock items then plot it onto a folium map."""
latdata = list(data['lat'])
londata = list(data['lng'])
"Chapter list to plot"
signlist = ['Taper front arrow','200', '400', '600', '800']
signcolor = ['blue', 'red', 'red', 'red', 'red']
markerlist = []
last_two = ['1mile', 'Workforce']
last_two_c = ['green', 'green']
last_two_m = []
"Work area to plot"
worksmarkerlist = []
access_signs_l = ['Access 100', 'Works access']
access_color_l = ['purple', 'purple']
access_markerposts_l = []
"Dead zone is inside the lat safety from front arrow"
deadzone_markerpost_l =[]

# lat and lon have to be floats to work so far..
# take taper location and work backwards to get sign locations
def advanced_warning_signs(lat, lon, len):
    found = data[data.lat == lat]
    bingo = found[found.lng == lon]
    taper_marker = list(bingo['BD'])
    taper_area = list(bingo['Area'])
    taper_road = list(bingo['DD'])
    startingp = taper_marker[0][0]
    bound = taper_marker[0][-1]
    middlepoint = taper_marker[0][1:-1]

    x, y = [int(num) for num in taper_marker[0][1:-1].split('/')]
    if taper_marker[0][-1] == 'A':
        print("/////////////////////////////////////////////////////////////////////")
        print("We are going Northbound")
        # Taper is on a northbound or away from london road..
        # So warning signs will be on on a markerpost with lower numbers
        # And the end of works will be on a higher number because it is further
        # from London..
        for num in range(5):

            if y <= 0:
                x -= 1
                y += 10
                print("/////////////////////////////////////////////////////////////////////")
                print("y is too big ...")
                print(f"Now this block is ran so x ={x} and y ={y}")

            elif num == 3:
                print("/////////////////////////////////////////////////////////////////////")
                print("At the 600s now")
                one_mile = x - 1
                print("/////////////////////////////////////////////////////////////////////")
                print(f"One mile goes at {one_mile}/{y}")
                plot = str(taper_marker[0][0]),str(one_mile),'/',str(y),str(taper_marker[0][-1])
                last_two_m.append(''.join(plot))

            elif num == 4:
                print("/////////////////////////////////////////////////////////////////////")
                print("At the 800s now")
                work_force = x - 1
                # Last in the range is 800s so add 1 km to get work force
                print("/////////////////////////////////////////////////////////////////////")
                print(f"Work force goes at {work_force}/{y}")
                plot = str(taper_marker[0][0]),str(work_force),'/',str(y),str(taper_marker[0][-1])
                last_two_m.append(''.join(plot))

            plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
            markerlist.append(''.join(plot))
            print("/////////////////////////////////////////////////////////////////////")
            print(markerlist)
            y -= 2


            """Heres where we will take the length of a job in km and plot it at the end of the job"""
            """
            I can also add in the longatude safety zone 150 mt taper + 50 = 200 lat safety then 100 from
            the end of lat safety is the works access so from start of taper +200 end of safety (access 100)
            + 100 works access
            Then take the direction of the traffic into account and plus or minus from taper location..
            """

        print(f"Job end is {len} away from {taper_marker}")
        jobmarkerps = len * 10
        print(f"Thats {int(jobmarkerps)} points on the map away from taper after plotting access and 100")
        x, y = [int(num) for num in taper_marker[0][1:-1].split('/')]

        for num in range(int(jobmarkerps)):

            if y >= 10:
                x += 1
                y -= 10

            if num == 1:
                print("Markerpost is inside the safety zone so it wont be plotted to map..")
                print(x, '/', y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                deadzone_markerpost_l.append(''.join(plot))

            if num == 2:
                print(f"Works access 100 is here")
                print(x, "/", y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                access_markerposts_l.append(''.join(plot))
            elif num == 3:
                print("Works access is here")
                print(x, "/", y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                access_markerposts_l.append(''.join(plot))

            plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
            worksmarkerlist.append(''.join(plot))
            y += 1


        # a, b = [int(num) for num in len[0].split('.')]
        # print(a)
        # print(b)

    else:
        # Taper is on a southbound or towards london road
        # everything in reverse to the if statement
        print("/////////////////////////////////////////////////////////////////////")
        print("We are going Southbound")
        for num in range(5):

            if y >= 10:
                x += 1
                y -= 10
                print("/////////////////////////////////////////////////////////////////////")
                print("y is too small ...")
                print(f"Now this block is ran so x ={x} and y ={y}")
                print("/////////////////////////////////////////////////////////////////////")
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                markerlist.append(''.join(plot))

            elif num == 3:
                print("/////////////////////////////////////////////////////////////////////")
                print("At the 600s now")
                one_mile = x + 1
                print("/////////////////////////////////////////////////////////////////////")
                print(f"One mile goes at {one_mile}/{y}")
                plot = str(taper_marker[0][0]),str(one_mile),'/',str(y),str(taper_marker[0][-1])
                last_two_m.append(''.join(plot))

            elif num == 4:
                print("/////////////////////////////////////////////////////////////////////")
                print("At the 800s now")
                work_force = x + 1
                # Last in the range is 800s so add 1 km to get work force
                print("/////////////////////////////////////////////////////////////////////")
                print(f"Work force goes at {work_force}/{y}")
                plot = str(taper_marker[0][0]),str(work_force),'/',str(y),str(taper_marker[0][-1])
                last_two_m.append(''.join(plot))

            plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
            markerlist.append(''.join(plot))
            print("/////////////////////////////////////////////////////////////////////")
            print(markerlist)
            y += 2

        jobmarkerps = len * 10
        print(f"Thats {int(jobmarkerps)} points on the map away from taper after plotting access and 100")
        x, y = [int(num) for num in taper_marker[0][1:-1].split('/')]

        for num in range(int(jobmarkerps)):

            if y <= 0:
                x -= 1
                y += 10

            if num == 1:
                print("Markerpost is inside the safety zone so it wont be plotted to map..")
                print(x, '/', y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                deadzone_markerpost_l.append(''.join(plot))

            if num == 2:
                print(f"Works access 100 is here")
                print(x, "/", y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                access_markerposts_l.append(''.join(plot))
            elif num == 3:
                print("Works access is here")
                print(x, "/", y)
                plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
                access_markerposts_l.append(''.join(plot))

            y -= 1
            plot = str(taper_marker[0][0]),str(x),'/',str(y),str(taper_marker[0][-1])
            worksmarkerlist.append(''.join(plot))

    """Add works markerpost to map and remove duplicates"""
    for marker in worksmarkerlist:

        newdata = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                       & (data['DD'] == taper_road[0])]
        lat = list(newdata['lat'])
        lon = list(newdata['lng'])

        for lt, ln in zip(lat, lon):
            fg.add_child(folium.Marker(location=[lt, ln], popup=(str(f"{marker}")), icon=folium.Icon(color='orange')))
            map.save("Map1.html")

    """Now to add them to a folium map...."""
    for sign, marker, color in zip(signlist, markerlist, signcolor):

        newdata = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                       & (data['DD'] == taper_road[0])]
        lat = list(newdata['lat'])
        lon = list(newdata['lng'])
        for lt, ln in zip(lat, lon):
            print("////////////////////////////////////////////////////////////////////")
            print(f"{sign} at {marker} lat/lon {lat}{lon} will be {color} on the map..")
            fg.add_child(folium.Marker(location=[lt, ln], popup=(str(f"{sign}\n{marker}")), icon=folium.Icon(color=color)))
            map.save("Map1.html")

    """Add the last two signs to the map"""
    for sign, marker, color in zip(last_two, last_two_m, last_two_c):
        newdata = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                       & (data['DD'] == taper_road[0])]
        lat = list(newdata['lat'])
        lon = list(newdata['lng'])
        for lt,ln in zip(lat, lon):
            print("////////////////////////////////////////////////////////////////////")
            print(f"{sign} at {marker} lat/lon {lat}{lon} will be {color} on the map..")
            fg.add_child(folium.Marker(location=[lt, ln], popup=(str(f"{sign}\n{marker}")), icon=folium.Icon(color=color)))
            map.save("Map1.html")

    """Add works access&100 to map"""
    for sign, marker, color in zip(access_signs_l, access_markerposts_l, access_color_l):
        newdata = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                       & (data['DD'] == taper_road[0])]
        lat = list(newdata['lat'])
        lon = list(newdata['lng'])

        for lt, ln in zip(lat, lon):
            fg.add_child(folium.Marker(location=[lt, ln], popup=(str(f"{sign}\n{marker}")), icon=folium.Icon(color=color)))
            map.save("Map1.html")

    for marker in deadzone_markerpost_l:
        newdata = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                       & (data['DD'] == taper_road[0])]
        lat = list(newdata['lat'])
        lon = list(newdata['lng'])

        for lt, ln in zip(lat,lon):
            fg.add_child(folium.Marker(location=[lt, ln], popup=(str(f"Dead zone\n{marker}")), icon=folium.Icon(color='black')))
            map.save("Map1.html")

    print("////////////////////////////////////////////////////////////////////")
    print("Chapter has been plotted to map")

    webbrowser.open_new_tab("Map1.html")
# print("And finally lets see whats going on here")

#     print(lat)
#     print(lon)
#     print(type(lat))
#     print(type(lon))
#     print("Found")
#     print(found)
#     print(type(found))
#     print("Bingo")
#     print(bingo)
#     print(type(bingo))

#     print(f"Taper location is {taper_marker[0]}")
#     print(f"{taper_marker[0][-1]}")
#     print(f"Taper location in area {taper_area[0]}")
#     print(f"Taper is on the {taper_road[0]} road")
map = folium.Map(location=[54.880268, -1.560417], zoom_start=8)
map.add_child(fg)
advanced_warning_signs(54.56758000000001,-1.581401, 3.5)
