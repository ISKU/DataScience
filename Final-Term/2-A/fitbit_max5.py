import csv
import json
import operator
from pathlib import Path

fitbit_file = open('fitbit.csv', 'r')
fitbit = csv.DictReader(fitbit_file)

fitbitmax = []

for info in fitbit :
    fitbitmax.append(info)

for i, line in fitbitmax:
    fitbitmax[i]['step'] = int(fitbitmax[i]['step'])

print('step')
fitbitmax.sort(key = operator.itemgetter('step'), reverse = False)

for i in range(0, 5, 1):
    print(fitbitmax[i]['name'] + ", " + fitbitmax[i]['step'] + "\n")

#print('heart')
#result.sort(key = operator.itemgetter('heart'), reverse = True)
#for i in range(0, 5, 1):
#    print(result[i]['name'] + ", " + result[i]['heart'] + "\n")

#print('sleep')
#result.sort(key = operator.itemgetter('sleep'), reverse = True)
#for i in range(0, 5, 1):
#    print(result[i]['name'] + ", " + result[i]['sleep'] + "\n")

