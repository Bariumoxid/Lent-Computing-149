# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

a = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='e',
                coord=(52.141965, 0.148004),
                typical_range=None,
                river='cc',
                town='aaa')

b = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='e',
                coord=(52.141965, 0.148004),
                typical_range=(0,1),
                river='cc',
                town='aaa')

c = MonitoringStation(
                station_id=1,
                measure_id=1,
                label='e',
                coord=(52.141965, 0.148004),
                typical_range=(1,0),
                river='cc',
                town='aaa')


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():
    assert inconsistent_typical_range_stations([a,b,c]) == [a,c]

