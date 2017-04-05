import csv
import json
import pandas as pd
from pathlib import Path

date_list = []
for date in range(20160401, 20160431, 1) :
    date_list.append(date)
for date in range(20160501, 20160521, 1) :
    date_list.append(date)

step_list = [[0 for x in range(99)] for y in range(51)]
step_list[0][0] = 'date'

for i in range(1, 99, 1) :
    step_list[0][i] = 'A0' + str(i)

j = 1
for date in pd.date_range('2016-04-01', '2016-05-20') :
    print(date)
    step_list[j][0] = date
    j += 1

for i in range(1, 99, 1) :
    userName = 'A0' + str(i)
    j = 1

    for date in date_list :
        filePath = './sokulee/' + userName + '/' + userName + '_' + str(date) + '_steps.json'
        
        if not Path(filePath).is_file() :
            step_list[j][i] = 0
            continue

        f = open(filePath, 'r')
        json_step = json.loads(f.read())
        f.close()

        print(filePath)
        step_list[j][i] = json_step['activities-steps'][0]['value'] if ('activities-steps' in json_step) else 0
        j += 1


write_file = open('steps.csv', 'w')
csv_step = csv.writer(write_file, delimiter = ',')

for line in step_list :
    csv_step.writerow(line)
write_file.close()
