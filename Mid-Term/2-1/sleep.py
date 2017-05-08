import csv
import json
import pandas as pd
from pathlib import Path

date_list = []
for date in range(20160401, 20160431, 1) :
    date_list.append(date)
for date in range(20160501, 20160521, 1) :
    date_list.append(date)

sleep_list = [[0 for x in range(51)] for y in range(99)]
sleep_list[0][0] = 'date'

for i in range(1, 99, 1) :
    sleep_list[i][0] = 'A0' + str(i)

j = 1
for date in pd.date_range('2016-04-01', '2016-05-20') :
    print(date)
    sleep_list[0][j] = date
    j += 1

for i in range(1, 99, 1) :
    userName = 'A0' + str(i)
    j = 1

    for date in date_list :
        filePath = './sokulee/' + userName + '/' + userName + '_' + str(date) + '_sleep.json'
        
        if not Path(filePath).is_file() :
            sleep_list[i][j] = 0
            continue

        f = open(filePath, 'r')
        json_sleep = json.loads(f.read())
        f.close()

        print(filePath)
        if (len(json_sleep['sleep']) ==0) :
            continue

        duration = 0
        for k in range(0, json_sleep['summary']['totalSleepRecords'], 1) :
            if duration < json_sleep['sleep'][k]['duration'] :
                duration += json_sleep['sleep'][k]['duration']

        sleep_list[i][j] = duration
        j += 1

write_file = open('avgsleep.csv', 'w')
csv_step = csv.writer(write_file, delimiter = ',')

for line in sleep_list :
    csv_step.writerow(line)
write_file.close()
