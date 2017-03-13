# -*- coding: utf-8 -*-

import csv
import datetime
from operator import itemgetter

rent_file = open('tashu.csv', 'r')
station_file = open('station.csv', 'r')
tashu_dict = csv.DictReader(rent_file)
station_dict = csv.DictReader(station_file)

day_dict = {'Mon': 0, 'Tues': 0, 'Wednes': 0, 'Thurs': 0, 'Fri': 0, 'Satur': 0, 'Sun': 0}
getDay = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur', 'Sun']

for rent in tashu_dict :
    rentdate = rent['RENT_DATE']
    date = getDay[datetime.date(int(rentdate[0:4]), int(rentdate[4:6]), int(rentdate[6:8])).weekday()]
    day_dict[date] += 1

print('Mon ' + str(day_dict['Mon']) + "\n" +\
      'Tues ' + str(day_dict['Tues']) + "\n" +\
      'Wednes ' + str(day_dict['Wednes']) + "\n" +\
      'Thurs ' + str(day_dict['Thurs']) + "\n" +\
      'Fri ' + str(day_dict['Fri']) + "\n" +\
      'Satur ' + str(day_dict['Satur']) + "\n" +\
      'Sun ' + str(day_dict['Sun']))

    
