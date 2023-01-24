# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit #Package that can calculate dist by two geographic coordinates (latitude/longitude)


def stations_by_distance(stations, p):
    """Returns a list of (station, distance) tuples"""

    coordinate_to_name={}
    for items in stations: 
        coordinate_to_name[str(items.coord)]=items.name #dict mapping coordinates to station name

    coord_list=[] #list of coordinates for input cities
    for items in stations:
        coord_list.append(items.coord)
          
    j=0
    station_county_distance=[] #list of tuple in form (station, distance)
    while j<len(stations):
        distance=haversine(p,coord_list[j]) #calculate the distance from coordinates
        station_county_distance.append((coordinate_to_name[str(coord_list[j])],distance)) #in the form [(name, distance)]
        j+=1

    station_county_distance=sorted_by_key(station_county_distance, 1) #sort by distance
    return station_county_distance


#---------------------------------------------------------------------------------------------------------------


def stations_within_radius(stations, centre, r):
    return [station for station in stations if haversine(station.coord,centre) < r]


#---------------------------------------------------------------------------------------------------------------


def river_with_station(stations):
    rivers=[]
    for station in stations:
        rivers.append(str(station.river))
    list_river=list(set(rivers))
    list_river.sort()
    return list_river


#---------------------------------------------------------------------------------------------------------------


def stations_by_river(stations): #return a dic in form {river:[stationsA, stationB...]}
    dic_river_stations={}
    for station in stations:
        if dic_river_stations.get(station.river)==None: #if the river is not yet in the dic
            dic_river_stations[station.river]=[station.name]
        else:
            dic_river_stations[station.river].append(station.name)
            dic_river_stations[station.river].sort() #sort by alphabetical order
    return dic_river_stations


#---------------------------------------------------------------------------------------------------------------


def rivers_by_station_number(stations, N):
    dic_rivers = {}
    for station in stations:
        dic_rivers[station.river] = dic_rivers.get(station.river,0)+1
    
    list_rivers = sorted([(river,dic_rivers[river]) for river in dic_rivers],key = lambda x: x[1], reverse = True)

    output = list_rivers[:N]
    for i in list_rivers[N:]:
        if i[1] == output[-1][1]:
            output.append(i)
    
    return output