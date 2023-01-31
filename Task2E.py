import datetime
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
def run():
    N=5
    dt=10
    stations = build_station_list()
    update_water_levels(stations)
    dict={}
    for station in stations:
        dict[station.name]=station


    for items in stations_highest_rel_level(stations,N+1):
        station_name=items[0]
        
        if station_name=="Whaddon":
            continue
        
        station=dict[station_name]
        dates,outcome2=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)) 
        plot_water_levels(station,dates,outcome2)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()