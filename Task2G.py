import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.predict import predict_water_level

def run():
    N, dt, dic = 5, 10, {}
    stations = build_station_list()
    update_water_levels(stations)
    prediction_results = {}
    for i in stations_level_over_threshold(stations,0.9):
        station = i[0]

        try:    
            dates,levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)) 
        except:
            continue
        if station.relative_water_level() != None:
            prediction = predict_water_level(dates,levels,5)
            rel = station.relative_water_level()

            if rel > 1:
                if prediction > 1:
                    status = 'severe'
                else:
                    status = 'high'
            else:
                if prediction > 1:
                    status = 'moderate'
                else:
                    status = 'low'

            plot_water_level_with_fit(station,dates,levels,4)
            prediction_results[status] = prediction_results.get(status,[]) + [[station.name, station.relative_water_level(),prediction]]
    
    for i in prediction_results:
        print('\n')
        print(f'Risk of flooding : {i}')
        print(prediction_results[i])
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()