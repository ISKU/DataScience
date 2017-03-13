reader = open('2015_2.csv', 'r')
writer = open('test2015_2.csv', 'w')

lines = reader.readlines()

for line in lines:
	cur = line.split(',')
	cur[1] = cur[1].replace("'", '')
	cur[3] = cur[3].replace("'", '')
	writer.write(cur[0] + ',' + cur[1] + ',' + cur[2] + ',' + cur[3])

reader.close()
writer.close()
