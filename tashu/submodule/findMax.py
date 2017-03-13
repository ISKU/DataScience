import csv

tashu_file = open('tashu.csv', 'r')
tashu = csv.DictReader(tashu_file)

max = 0
for rent in tashu:
	if rent['RETURN_STATION'] != '' :
		if max < int(rent['RETURN_STATION']) :
			max = int(rent['RETURN_STATION'])

	if rent['RENT_STATION'] != '' :
		if max < int(rent['RENT_STATION']) :
			max = int(rent['RENT_STATION'])

print(max)
