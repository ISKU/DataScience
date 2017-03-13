import csv
import operator

tashu_file = open('tashu.csv', 'r')
station_file = open('station.csv', 'r')

tashu = csv.DictReader(tashu_file)
station = csv.DictReader(station_file)

station_list = [{}]
rent_list = []

for info in station :
	station_list.append(info)

for i in range(0, 227, 1) :
	rent_list.append({'station': i, 'count': 0})

for rent in tashu :
	if rent['RENT_STATION'] != '' :
		rent_list[int(rent['RENT_STATION'])]['count'] += 1
	if rent['RETURN_STATION'] != '' :
		rent_list[int(rent['RETURN_STATION'])]['count'] += 1

rent_list.sort(key = operator.itemgetter('count'), reverse = True)

for i in range(0, 10, 1) :
	print(station_list[rent_list[i]['station']]['NAME'] + " " + str(rent_list[i]['station']) + " " + str(rent_list[i]['count']))
