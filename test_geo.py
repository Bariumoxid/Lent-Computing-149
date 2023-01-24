from floodsystem.geo import stations_within_radius, stations_by_distance
from floodsystem.station import MonitoringStation
from floodsystem.geo import river_with_station
from floodsystem.geo import stations_by_river

c = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='c',
                coord=(52.141965, 0.148004),
                typical_range=(1, 1),
                river='aa',
                town='aaa')
b = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='b',
                coord=(51.874767, -1.740083),
                typical_range=(1, 1),
                river='aa',
                town='aaa')
a = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='a',
                coord=(52.197227, 0.087527),
                typical_range=(1, 1),
                river='aa',
                town='aaa')

def test_sort_station_by_distance(): #the pytest for Task1B
    station_list_test=[a,b,c]
    p = (52.2053, 0.1218)
    print(stations_by_distance(station_list_test,p))
    assert stations_by_distance(station_list_test,p)[0]==('a', 2.502277543239629)
    assert stations_by_distance(station_list_test,p)[1]==('c', 7.265704342799649)
    assert stations_by_distance(station_list_test,p)[2]==('b', 132.5410306597496)
test_sort_station_by_distance()

def test_stations_within_radius(): #the pytest for Task1C
    centre = (52.2053, 0.1218)
    print(set(stations_within_radius([c,b,a],centre,10)) == {a,c})
test_stations_within_radius()


d = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='d',
                coord=(52.141965, 0.148004),
                typical_range=(1, 1),
                river='aa',
                town='aaa')

e = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='e',
                coord=(52.141965, 0.148004),
                typical_range=(1, 1),
                river='cc',
                town='aaa')

def test_river_with_station():
    assert (river_with_station([a,b,c,d,e]))==['aa','cc']
test_river_with_station()

def test_stations_by_river():
    assert stations_by_river([a,b,c,d,e])['cc']==['e']
    assert stations_by_river([a,b,c,d,e])['aa']==['a','b','c','d']
test_stations_by_river()
    
