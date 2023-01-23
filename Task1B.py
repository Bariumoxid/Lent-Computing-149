from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()
    stations_list=[]

    station_name_to_town_dict={}
    for items in stations: #extract station names and coordinates
        stations_list.append(items.name)
        station_name_to_town_dict[str(items.name)]=str(items.town)


    coordinate=tuple((52.2053, 0.1218))
    value=stations_by_distance(stations_list,coordinate)
    output=[]
    k=0
    print(value[1][1])
    for k in range (len(value)):
        output.append((value[k][0],station_name_to_town_dict[str(value[k][0])],value[k][1]))
        
    print(output[:10])
    print("--------")
    print(output[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()