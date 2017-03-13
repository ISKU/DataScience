import csv
from operator import itemgetter

rent_file = open('tashu.csv', 'r')
station_file = open('station.csv', 'r')
tashu_dict = csv.DictReader(rent_file)
station_dict = csv.DictReader(station_file)

w, h = 227, 277
rent_list = [[0 for x in range(w)] for y in range(h)]
station_list = [{}]

for info in station_dict :
    station_list.append(info)

for i in range(1, 227, 1) :
    for j in range(1, 227, 1) :
        rent_list[i][j] = {'rent': i, 'return': j, 'count': 0}

for rent in tashu_dict :
    if rent['RENT_STATION'] == '' :
        continue
    if rent['RETURN_STATION'] == '' :
        continue

    rent_list[int(rent['RENT_STATION'])][int(rent['RETURN_STATION'])]['count'] += 1
 
linearlist = []
for i in range(1, 227, 1) :
    for j in range(1, 227, 1) :
        linearlist.append(rent_list[i][j])

linearlist.sort(key = itemgetter('count'), reverse = True)
    
result = []
for i in range(0, 10, 1) :
    print(station_list[linearlist[i]['rent']]['NAME'] + " " + str(linearlist[i]['rent']) + " " +  station_list[linearlist[i]['return']]['NAME'] + " " + str(linearlist[i]['return']) + " " + str(linearlist[i]['count']))

