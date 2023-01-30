def stations_level_over_threshold(stations, tol):
    return sorted([(station,station.relative_water_level()) for station in stations if (station.relative_water_level()!= None) and (station.relative_water_level()>tol)], key = lambda x: x[1], reverse = True)

def stations_highest_rel_level(stations, N):
    level_to_station_dict={}
    water_level=[]
    for i in stations_level_over_threshold(stations,0):
        level_to_station_dict[(i[1])]=i[0].name
        water_level.append(i[1])
    
    water_level.sort(reverse=True)
    i=0
    output=[]
    while i< (N):
        output.append([level_to_station_dict[water_level[i]],water_level[i]])
        i+=1
    return output