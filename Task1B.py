from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()

    station_name_to_town_dict={}
    for items in stations: #extract station names and coordinates
        station_name_to_town_dict[str(items.name)]=str(items.town)


    coordinate=tuple((52.2053, 0.1218)) #the given coordinates
    value=stations_by_distance(stations,coordinate) #in the form (station, distance)
    output=[] #in form (station, town, distance)
    print(value[1][0])
    k=0
    for k in range (len(value)):
        output.append((value[k][0],station_name_to_town_dict[str(value[k][0])],value[k][1]))
        
    print(output[:10]) #10 closest
    print("--------")
    print(output[-10:]) #10 furthest

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()