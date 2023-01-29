# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, date_open = None):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        self.date_open = date_open

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   date opened: {}".format(self.date_open)
        return d
    
    def typical_range_consistent(self):
        return (self.typical_range != None) and (self.typical_range[0] <= self.typical_range[1])


    def relative_water_level(self):
        if self.latest_level != None and self.typical_range_consistent():
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1]- self.typical_range[0])
        return None


    
    #==========================================Properties=======================================

    #------------------------------------------Station ID---------------------------------------
    
    @property
    def station_id(self):
        return self._station_id
    
    @station_id.setter
    def station_id(self,value):
        try:
            self._station_id
            print("NO CHANGES ALLOWED!")
        except:
            self._station_id = value

    #------------------------------------------Name-----------------------------------------------
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        try:
            self._name
            print("NO CHANGES ALLOWED!")
        except:
            self._name = value

    #------------------------------------------Measure_ID-------------------------------------------
    @property
    def measure_id(self):
        return self._measure_id
    
    @measure_id.setter
    def measure_id(self,value):
        try:
            self._measure_id
            print("NO CHANGES ALLOWED!")
        except:
            self._measure_id = value

    #------------------------------------------coord------------------------------------------------
    @property
    def coord(self):
        return self._coord
    
    @coord.setter
    def coord(self,value):
        try:
            self._coord
            print("NO CHANGES ALLOWED!")
        except:
            self._coord= value

    #------------------------------------------typical_range-----------------------------------------
    @property
    def typical_range(self):
        return self._typical_range
    
    @typical_range.setter
    def typical_range(self,value):
        try:
            self._typical_range
            print("NO CHANGES ALLOWED!")
        except:
            self._typical_range = value

    #------------------------------------------river--------------------------------------------------
    @property
    def river(self):
        return self._river
    
    @river.setter
    def river(self,value):
        try:
            self._river
            print("NO CHANGES ALLOWED!")
        except:
            self._river = value
            
    #------------------------------------------town----------------------------------------------------
    @property
    def town(self):
        return self._town
    
    @town.setter
    def town(self,value):
        try:
            self._town
            print("NO CHANGES ALLOWED!")
        except:
            self._town = value

    

def inconsistent_typical_range_stations(stations):
    return [station for station in stations if not station.typical_range_consistent()]