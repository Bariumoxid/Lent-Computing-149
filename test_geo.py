from floodsystem.geo import stations_within_radius, stations_by_distance
from floodsystem.station import MonitoringStation


def test_stations_within_radius():
    centre = (52.2053, 0.1218)
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
    print(set(stations_within_radius([c,b,a],centre,10)) == {a,c})

test_stations_within_radius()
    
