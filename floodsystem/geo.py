# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit #Package that can calculate dist by two geographic coordinates (latitude/longitude)
from .stationdata import build_station_list


def stations_by_distance(stations, p):
    """Returns a list of (station, distance) tuples"""

    station = build_station_list()
    station_name_to_coordinate={}
    for items in station: 
        station_name_to_coordinate[str(items.name)]=items.coord


    i=0
    station_distance_dict={}
    coord_list=[]
    for i in range (len(stations)):
        coord_list.append(station_name_to_coordinate[stations[i]])
        station_distance_dict[str(station_name_to_coordinate[stations[i]])]=str(stations[i]) #create a dict in form coordinate:station_name 

    j=0
    station_county_distance=[]
    while j<len(stations):
        distance=haversine(p,coord_list[j])
        station_county_distance.append((station_distance_dict[str(coord_list[j])],distance)) #in the form [(name, distance)]
        j+=1

    station_county_distance=sorted_by_key(station_county_distance, 1) #sort by distance
    return station_county_distance
