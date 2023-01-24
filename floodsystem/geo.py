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

    coordinate_to_name={}
    for items in stations: 
        coordinate_to_name[str(items.coord)]=items.name #dict mapping coordinates to station name

    coord_list=[] #list of coordinates for input cities
    #for i in range (len(stations)):
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

def stations_within_radius(stations, centre, r):
    print(stations)
    return [station for station in stations if haversine(station.coord,centre) < r]
