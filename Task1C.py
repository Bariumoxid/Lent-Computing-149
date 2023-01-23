from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    filtered_stations= sorted(stations_within_radius(stations,centre,10), key = lambda x: x.name)

    output = [station.name for station in filtered_stations]
    print(output)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()