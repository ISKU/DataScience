# -*- coding: utf-8 -*-

import csv
import datetime
import operator

rent_file = open('/home/kmh1/tashu.csv', 'r')
tashu_dict = csv.DictReader(rent_file)

day_dict = {'Mon': 0, 'Tues': 0, 'Wednes': 0, 'Thurs': 0, 'Fri': 0, 'Satur': 0, 'Sun': 0}
getDay = ['Mon', 'Tues', 'Wednes', 'Thurs', 'Fri', 'Satur', 'Sun']

station = []
for i in range(0, 227, 1):
    station.append({'station': i, 'count': 0})

output = []

for rent in tashu_dict :
    if rent['RENT_STATION'] is '':
        continue

    rentdate = rent['RENT_DATE']
    if getDay[datetime.date(int(rentdate[0:4]), int(rentdate[4:6]), int(rentdate[6:8])).weekday()] is 'Satur':
        output.append(rent['RENT_STATION'])
        station[int(rent['RENT_STATION'])]['count'] += 1
    elif getDay[datetime.date(int(rentdate[0:4]), int(rentdate[4:6]), int(rentdate[6:8])).weekday()] is 'Sun':
        output.append(rent['RENT_STATION'])
        station[int(rent['RENT_STATION'])]['count'] += 1

station.sort(key=operator.itemgetter('count'), reverse = True)
for i in range(0, 5, 1):
    print(str(station[i]['station']) + " " + str(station[i]['count']))


write_file = open('tashu_week.csv', 'w')
write_file.write('mon-fri\n')

for value in output :
    write_file.write(value + '\n')

write_file.close()
