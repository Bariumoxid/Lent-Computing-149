import floodsystem.geo as g
from floodsystem.station import MonitoringStation

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

f = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='e',
                coord=(52.141965, 0.148004),
                typical_range=(1, 1),
                river='dd',
                town='aaa')

def test_sort_station_by_distance(): #the pytest for Task1B
    station_list_test=[a,b,c]
    p = (52.2053, 0.1218)
    print(g.stations_by_distance(station_list_test,p))
    assert g.stations_by_distance(station_list_test,p)[0]==('a', 2.502277543239629)
    assert g.stations_by_distance(station_list_test,p)[1]==('c', 7.265704342799649)
    assert g.stations_by_distance(station_list_test,p)[2]==('b', 132.5410306597496)


def test_stations_within_radius(): #the pytest for Task1C
    centre = (52.2053, 0.1218)
    print(set(g.stations_within_radius([c,b,a],centre,10)) == {a,c})


def test_river_with_station():
    assert (g.river_with_station([a,b,c,d,e]))==['aa','cc']


def test_stations_by_river():
    assert g.stations_by_river([a,b,c,d,e])['cc']==['e']
    assert g.stations_by_river([a,b,c,d,e])['aa']==['a','b','c','d']


def test_rivers_by_station_number():
    assert g.rivers_by_station_number([a,b,c,d,e,f],2)==[('aa',4),('cc',1),('dd',1)]
