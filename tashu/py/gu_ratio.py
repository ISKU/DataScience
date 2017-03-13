# -*- coding: utf-8 -*-

import csv
from operator import itemgetter

rent_file = open('tashu.csv', 'r')
station_file = open('station.csv', 'r')
tashu_dict = csv.DictReader(rent_file)
station_dict = csv.DictReader(station_file)

gu_dict = {'유성구': 0, '서구': 0, '대덕구': 0, '중구': 0, '동구': 0}
station_list = [{}]

for info in station_dict :
    station_list.append(info)

for rent in tashu_dict :
    if rent['RENT_STATION'] != '' :
        if int(rent['RENT_STATION']) <= 144 :
            gu_dict[station_list[int(rent['RENT_STATION'])]['GU']] += 1
    if rent['RETURN_STATION'] != '' :
        if int(rent['RETURN_STATION']) <= 144 :
            gu_dict[station_list[int(rent['RETURN_STATION'])]['GU']] += 1

print('유성구' + " " + str(gu_dict['유성구']) + "\n" +\
      '서구' + " " + str(gu_dict['서구']) + "\n" +\
      '대덕구' + " " + str(gu_dict['대덕구']) + "\n" +\
      '중구' + " " + str(gu_dict['중구']) + "\n" +\
      '동구' + " " + str(gu_dict['동구']))
    
