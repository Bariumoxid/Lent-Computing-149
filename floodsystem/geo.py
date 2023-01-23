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
    centre=(52.2053, 0.1218) #the coordinate of cambridge city center
    i=0
    station_distance_dict={}
    for i in range (len(stations)):
        station_distance_dict[str(p[i])]=str(stations[i]) #create a dict in form coordinate:station_name 
    j=0
    station_county_distance=[]
    while j<len(stations):
        distance=haversine(centre,p[j]) 
        station_county_distance.append((station_distance_dict[str(p[j])],distance))
        j+=1

    station_county_distance=sorted_by_key(station_county_distance, 1) #sort by distance
    return station_county_distance
