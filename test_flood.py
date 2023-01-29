from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

c = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='c',
                coord=(52.141965, 0.148004),
                typical_range=(1, 2),
                river='aa',
                town='aaa')

b = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='b',
                coord=(51.874767, -1.740083),
                typical_range=(1, 2),
                river='aa',
                town='aaa')

a = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='a',
                coord=(52.197227, 0.087527),
                typical_range=(1, 2),
                river='aa',
                town='aaa')


def test_stations_level_over_threshold():
    a.latest_level = 2
    b.latest_level = 3
    assert stations_level_over_threshold([a,b,c],0.8) == [(b,2.0),(a,1.0)]


