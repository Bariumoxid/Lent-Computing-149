import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
def run():
    N, dt, dic = 5, 10, {}
    stations = build_station_list()
    update_water_levels(stations)
    
    for station in stations:
        dic[station.name]=station

    for items in stations_highest_rel_level(stations,N+1):
        station_name=items[0]

        station=dic[station_name]
        try:    
            dates,levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)) 
        except:
            continue

        plot_water_level_with_fit(station,dates,levels,4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
