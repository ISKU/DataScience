# -*- coding: utf-8 -*-

import csv
import datetime
from operator import itemgetter

rent_file = open('tashu.csv', 'r')
station_file = open('station.csv', 'r')
tashu_dict = csv.DictReader(rent_file)
station_dict = csv.DictReader(station_file)

hour_dict = {'01': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0,\
            '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '00': 0}

for rent in tashu_dict :
    hour_dict[rent['RENT_DATE'][8:10]] += 1

print(hour_dict)
