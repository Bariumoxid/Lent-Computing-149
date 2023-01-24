from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list
def run():
    stations = build_station_list()
    print(river_with_station(stations)[:10]) #the first ten rivers
    print(f"{len(river_with_station(stations))} rivers have at least one monitoring station")
    print("---------------")
    print(stations_by_river(stations)["River Aire"])
    print("---------------")
    print(stations_by_river(stations)["River Cam"])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()