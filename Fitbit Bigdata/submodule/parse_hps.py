import csv
import json
import pandas as pd
from pathlib import Path

hps_list = [[0 for x in range(99)] for y in range(1441)]
datetime_list = [str(date[1]).split(' ')[1] for date in enumerate(pd.DatetimeIndex(start = '00:00:00', end = '23:59:00', freq = '60000ms'))]
date_list = []
for date in range(20160401, 20160431, 1) :
    date_list.append(date)
for date in range(20160501, 20160521, 1) :
    date_list.append(date)

hps_list[0][0] = 'datetime'
for i in range(1, 99, 1) :
    hps_list[0][i] = 'A0' + str(i)

j = 1
for date in datetime_list :
    print(str(j) + ' ' + str(date))
    hps_list[j][0] = date
    j += 1


for date in date_list:
    for y in range(1, 1441, 1) :
        for x in range(1, 99, 1) :
            hps_list[y][x] = 0

    for i in range(1, 99, 1) :
        userName = 'A0' + str(i)
        path_heart = './sokulee/' + userName + '/' + userName + '_' + str(date) + '_heart.json'
        path_sleep = './sokulee/' + userName + '/' + userName + '_' + str(date) + '_sleep.json'

        if (not Path(path_heart).is_file()) or (not Path(path_sleep).is_file()) :
            continue

        file_heart = open(path_heart, 'r')
        file_sleep = open(path_sleep, 'r')
        json_heart = json.loads(file_heart.read())
        json_sleep = json.loads(file_sleep.read())
        file_heart.close()
        file_sleep.close()
        print(path_heart + ' ' + path_sleep)

        if (not 'activities-heart-intraday' in json_heart) or (len(json_sleep['sleep']) == 0) :
            continue

        maxDurationIndex = 0
        duration = 0
        for j in range(0, json_sleep['summary']['totalSleepRecords'], 1) :
            if duration < json_sleep['sleep'][j]['duration'] :
                maxDurationIndex = j
                duration = json_sleep['sleep'][j]['duration']

        for sleep in json_sleep['sleep'][maxDurationIndex]['minuteData'] :
            time = sleep['dateTime']
            try:
                index = (int(time[0:2]) * 60) + int(time[3:5]) + 1
                heart_index = next(j for (j, d) in enumerate(json_heart['activities-heart-intraday']['dataset']) if d['time'] == time)
            except StopIteration :
                continue

            print(time[0:2] + ':' + time[3:5] + ' ' + str(index) + ' ' + str(len(json_heart['activities-heart-intraday']['dataset'])))
            hps_list[index][i] = json_heart['activities-heart-intraday']['dataset'][heart_index]['value']

    file_hps = open(str(date) + '_hps.csv', 'w')
    csv_hps = csv.writer(file_hps, delimiter = ',')

    for line in hps_list :
        csv_hps.writerow(line)
    file_hps.close()
