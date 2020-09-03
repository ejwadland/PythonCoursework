import pytest
from cities import *


def test_compute_total_distance():

    road_map1 = [('Kentucky', 'Frankfort', 38.197274, -84.86311),
                ('Delaware', 'Dover', 39.161921, -75.526755),
                ('Minnesota', 'Saint Paul', 44.95, -93.094)]

    assert compute_total_distance(road_map1) == 38.528719926809416
    assert compute_total_distance(road_map1) != 0

    road_map2 = [('Iowa', 'Des Moines',	41.590939, -93.620866),
                 ('New York', 'Albany',	42.659829,	-73.781339),
                 ('Kansas',	'Topeka', 39.04, -95.69)]

    assert compute_total_distance(road_map2) == 45.35858976132347
    assert compute_total_distance(road_map2) != 0

    road_map3 = [('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                     ('New York', 'Albany', 42.659829, -73.781339),
                     ('North Carolina', 'Raleigh', 35.771, -78.638),
                     ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                     ('Ohio', 'Columbus', 39.962245, -83.000647)]

    assert compute_total_distance(road_map3) == 110.28160192715517
    assert compute_total_distance(road_map3) != 0

    road_map4 = [('Virginia', 'Richmond', 37.54, -77.46),
                ('Washington', 'Olympia', 47.042418 , -122.893077),
                ('West Virginia', 'Charleston', 38.349497, -81.633294),
                ('Wisconsin', 'Madison', 43.074722 , -89.384444),
                ('Wyoming', 'Cheyenne', 41.145548 , -104.802042),
                ('Ohio', 'Columbus', 39.962245 , -83.000647)]

    assert compute_total_distance(road_map4) == 141.07793655218606
    assert compute_total_distance(road_map4) != 0

    road_map5 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                 ('Wyoming', 'Cheyenne', 41.145548, -104.802042)]

    assert compute_total_distance(road_map5) == 41.00036805639071
    assert compute_total_distance(road_map5) != 0





def test_swap_cities():
    road_map1 = [('Colorado', 'Denver', '39.7391667', '-104.984167'),
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),
                 ('Delaware', 'Dover', '39.161921', '-75.526755'),
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277')]

    new_road_map1 = [('Colorado', 'Denver', '39.7391667', '-104.984167'),
                     ('Florida', 'Tallahassee', '30.4518', '-84.27277'),
                     ('Delaware', 'Dover', '39.161921', '-75.526755'),
                     ('Connecticut', 'Hartford', '41.767', '-72.677')]

    new_total_distance1 = compute_total_distance(new_road_map1)
    assert swap_cities(road_map1, 1, 3), \
                     (new_road_map1, new_total_distance1)

    road_map2 = [('Virginia', 'Richmond', 37.54, -77.46),
                ('Washington', 'Olympia', 47.042418 , -122.893077),
                ('West Virginia', 'Charleston', 38.349497, -81.633294),
                ('Wisconsin', 'Madison', 43.074722 , -89.384444),
                ('Wyoming', 'Cheyenne', 41.145548 , -104.802042),
                ('Ohio', 'Columbus', 39.962245 , -83.000647)]

    new_road_map2 = [('Ohio', 'Columbus', 39.962245 , -83.000647),
                ('Washington', 'Olympia', 47.042418 , -122.893077),
                ('West Virginia', 'Charleston', 38.349497, -81.633294),
                ('Wisconsin', 'Madison', 43.074722 , -89.384444),
                ('Wyoming', 'Cheyenne', 41.145548 , -104.802042),
                ('Virginia', 'Richmond', 37.54, -77.46)]

    new_total_distance2 = compute_total_distance(new_road_map2)
    assert swap_cities(road_map2, 0, 5), (new_road_map2, new_total_distance2)

    road_map3 = [('Alabama', 'Montgomery', 32.361538, -86.279118),
                 ('Wyoming', 'Cheyenne', 41.145548, -104.802042)]

    new_road_map3 = [('Wyoming', 'Cheyenne', 41.145548, -104.802042),
                    ('Alabama', 'Montgomery', 32.361538, -86.279118)]

    new_total_distance3 = compute_total_distance(new_road_map3)
    assert swap_cities(road_map3, 0, 1), (new_road_map3, new_total_distance3)

    road_map4 = [('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                     ('New York', 'Albany', 42.659829, -73.781339),
                     ('North Carolina', 'Raleigh', 35.771, -78.638),
                     ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                     ('Ohio', 'Columbus', 39.962245, -83.000647)]

    new_road_map4 = [('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                     ('North Dakota', 'Bismarck', 48.813343, -100.779004),
                     ('North Carolina', 'Raleigh', 35.771, -78.638),
                     ('New York', 'Albany', 42.659829, -73.781339),
                     ('Ohio', 'Columbus', 39.962245, -83.000647)]

    new_total_distance4 = compute_total_distance(road_map4)
    assert swap_cities(road_map4, 1, 4), (new_road_map4, new_total_distance4)

    road_map5 = [('Colorado', 'Denver', '39.7391667', '-104.984167'),
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),
                 ('Delaware', 'Dover', '39.161921', '-75.526755'),
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277')]

    new_road_map5 = [('Delaware', 'Dover', '39.161921', '-75.526755'),
                 ('Connecticut', 'Hartford', '41.767', '-72.677'),
                 ('Colorado', 'Denver', '39.7391667', '-104.984167'),
                 ('Florida', 'Tallahassee', '30.4518', '-84.27277')]

    new_total_distance5 = compute_total_distance(road_map5)
    assert swap_cities(road_map4, 0, 4), (new_road_map5, new_total_distance5)



def test_shift_cities():

    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755),\
                ("Minnesota", "Saint Paul", 44.95, -93.094)]
    assert shift_cities(road_map1) ==\
                [("Minnesota", "Saint Paul", 44.95, -93.094),\
                ("Kentucky", "Frankfort", 38.197274, -84.86311),\
                ("Delaware", "Dover", 39.161921, -75.526755)]

    road_map2 = [('Virginia', 'Richmond', 37.54, -77.46),
                ('Washington', 'Olympia', 47.042418 , -122.893077),
                ('West Virginia', 'Charleston', 38.349497, -81.633294),
                ('Wisconsin', 'Madison', 43.074722 , -89.384444),
                ('Wyoming', 'Cheyenne', 41.145548 , -104.802042),
                ('Ohio', 'Columbus', 39.962245 , -83.000647)]

    assert shift_cities(road_map2) ==\
        [('Ohio', 'Columbus', 39.962245 , -83.000647),
         ('Virginia', 'Richmond', 37.54, -77.46),
         ('Washington', 'Olympia', 47.042418 , -122.893077),
         ('West Virginia', 'Charleston', 38.349497, -81.633294),
         ('Wisconsin', 'Madison', 43.074722, -89.384444),
         ('Wyoming', 'Cheyenne', 41.145548, -104.802042)]

    road_map3 = [('Colorado', 'Denver', 39.7391667, -104.984167),
                 ('Connecticut', 'Hartford', 41.767, -72.677)]

    assert shift_cities(road_map3) ==\
        [('Connecticut', 'Hartford', 41.767, -72.677),
         ('Colorado', 'Denver', 39.7391667, -104.984167)]

    road_map4 =  [('Delaware', 'Dover', 39.161921, -75.526755),
                 ('Connecticut', 'Hartford', 41.767, -72.677),
                 ('Colorado', 'Denver', 39.7391667, -104.984167),
                 ('Florida', 'Tallahassee', 30.4518, -84.27277)]

    assert shift_cities(road_map4) ==\
        [('Florida', 'Tallahassee', 30.4518, -84.27277),
         ('Delaware', 'Dover', 39.161921, -75.526755),
         ('Connecticut', 'Hartford', 41.767, -72.677),
         ('Colorado', 'Denver', 39.7391667, -104.984167)]

    road_map5 = [('Georgia', 'Atlanta',	33.76,	-84.39),
                 ('Hawaii',	'Honolulu',	21.30895, -157.826182),
                 ('Idaho', 'Boise',	43.613739,	-116.237651),
                 ('Illinois', 'Springfield', 39.78325,	-89.650373)]

    assert shift_cities(road_map5) ==\
        [('Illinois', 'Springfield', 39.78325,	-89.650373),
         ('Georgia', 'Atlanta', 33.76, -84.39),
         ('Hawaii', 'Honolulu', 21.30895, -157.826182),
         ('Idaho', 'Boise', 43.613739, -116.237651)]
















