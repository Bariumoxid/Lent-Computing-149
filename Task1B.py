from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()
    coordinates_list=[]
    stations_list=[]
    for items in stations: #extract station names and coordinates
        coordinates_list.append(items.coord)
        stations_list.append(items.name)
    output=stations_by_distance(stations_list,coordinates_list)
    print(output[:10])
    print("--------")
    print(output[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()