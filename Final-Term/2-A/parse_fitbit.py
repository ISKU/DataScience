import csv
import json
from pathlib import Path

# step, heart, sleep
result = [[0 for x in range(4)] for y in range(98)]

for i in range(1, 99, 1) :
    userName = 'A0' + str(i)
    result[i - 1][0] = userName
    stepPath = './sokulee/' + userName + '/' + userName + '_' + '20160401' + '_steps.json'
    heartPath = './sokulee/' + userName + '/' + userName + '_' + '20160401' + '_heart.json'
    sleepPath = './sokulee/' + userName + '/' + userName + '_' + '20160401' + '_sleep.json'

    if not Path(stepPath).is_file() :
        result[i - 1][1] = 0
    else :
        stepFile = open(stepPath, 'r')
        json_step = json.loads(stepFile.read())
        stepFile.close()
        print(stepPath)
        result[i - 1][1] = json_step['activities-steps'][0]['value'] if ('activities-steps' in json_step) else 0

    if not Path(heartPath).is_file() :
        result[i - 1][2] = 0
    else :
        heartFile = open(heartPath, 'r')
        json_heart = json.loads(heartFile.read())
        heartFile.close()
        print(heartPath)
        result[i - 1][2] = len(json_heart['activities-heart-intraday']['dataset']) if ('activities-heart-intraday' in json_heart) else 0

    if not Path(sleepPath).is_file() :
        result[i - 1][3] = 0
    else :
        sleepFile = open(sleepPath, 'r')
        json_sleep = json.loads(sleepFile.read())
        sleepFile.close()
        print(sleepPath)
        result[i - 1][3] = json_sleep['summary']['totalTimeInBed'] if ('summary' in json_sleep) else 0


write_file = open('kmeans_fitbit.txt', 'w')

#for i in range(0, 98, 1) :
#    for j in range(0, 4, 1) :
#        write_file.write(str(result[i][j]) + ',')
#    write_file.write(str(int(result[i][1]) + int(result[i][2]) + int(result[i][3])))
#    write_file.write('\n')
#write_file.close()

for i in range(0, 98, 1) :
    write_file.write(str(i) + ' ')
    write_file.write('1:' + str(result[i][1]) + ' ')
    write_file.write('2:' + str(result[i][2]) + ' ')
    write_file.write('3:' + str(result[i][3]) + ' ')
    write_file.write('\n')
write_file.close()
