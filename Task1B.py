from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    stations = build_station_list()
    distance=[]
    print(stations_by_distance(stations,distance))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()