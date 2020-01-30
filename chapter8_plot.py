import folium
import pandas as pd

data = pd.read_csv("roadlocationdata.csv")
fg = folium.FeatureGroup(name="Chapter 8")


sign_names = ['taper', '200', '400', '600', '800']
sign_marker = []

last_two = ["1 mile", 'Workforce']
last_two_marker = []


def plot_chapter_8(lat, lon, map_name):
    map = folium.Map(location=[lat, lon], zoom_start=8)
    found = data[data.lat == lat]
    bingo = found[found.lng == lon]
    taper_marker = list(bingo['BD'])
    taper_area = list(bingo['Area'])
    taper_road = list(bingo['DD'])
    pre_marker = str(taper_marker[0][0])

    x, y = [int(num) for num in taper_marker[0][1:-1].split('/')]

    if taper_marker[0][-1] == 'A':
        # a roads go away from london

        for num in range(5):

            if y < 0:

                x -= 1
                y += 10

            elif num == 3:

                # The mile sign is 1 km away from the 600 sign.
                one_mile_x = x - 1
                plot = pre_marker, str(one_mile_x), '/', str(y), str(taper_marker[0][-1])
                last_two_marker.append(''.join(plot))

            elif num == 4:

                # The work force sign is 1 km away from the 800 sign.
                work_force_x = x - 1
                plot = pre_marker, str(work_force_x), '/', str(y), str(taper_marker[0][-1])
                last_two_marker.append(''.join(plot))

            plot = pre_marker, str(x), "/", str(y), str(taper_marker[0][-1])
            sign_marker.append(''.join(plot))
            y -= 2

    else:
        # b roads are bound to london

        for num in range(5):

            if y >= 10:

                x += 1
                y -= 10

            elif num == 3:

                one_mile_x = x + 1
                plot = pre_marker, str(one_mile_x), '/', str(y), str(taper_marker[0][-1])
                last_two_marker.append(''.join(plot))

            elif num == 4:

                work_force_x = x + 1
                plot = pre_marker, str(work_force_x), '/', str(y), str(taper_marker[0][-1])
                last_two_marker.append(''.join(plot))

            plot = pre_marker, str(x), "/", str(y), str(taper_marker[0][-1])
            sign_marker.append(''.join(plot))

            y += 2

    # for each sign plot to map
    for sign, marker in zip(sign_names, sign_marker):

        # this line of code is rigid if it is empty we need more information or a detailed search to continue the plot
        new_data = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                        & (data['DD'] == taper_road[0])]
        lat = list(new_data['lat'])
        lon = list(new_data['lng'])

        for lt, ln in zip(lat, lon):
            fg.add_child(folium.Marker(location=[lt, ln],
                                       popup=(str(f"{sign}\n{marker}")),
                                       icon=folium.Icon(color='red')))

    for sign, marker in zip(last_two, last_two_marker):

        # this line of code is rigid if it is empty we need more information or a detailed search to continue the plot
        new_data = data[(data['BD'] == marker) & (data['Area'] == taper_area[0])
                        & (data['DD'] == taper_road[0])]
        lat = list(new_data['lat'])
        lon = list(new_data['lng'])

        for lt, ln in zip(lat, lon):
            fg.add_child(folium.Marker(location=[lt, ln],
                                       popup=(str(f"{sign}\n{marker}")),
                                       icon=folium.Icon(color='red')))
    map.save(f"{map_name}.html")

    map.add_child(fg)

    # pass info onto this function to plot the end of the job.
    # plot_length(lat, lon, len, map_name)

# plot_chapter_8(53.694582, -1.1713959999999999, "A1_JcWhatever")

