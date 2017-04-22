reader = open('ml-10M100K/ratings.dat', 'r')
writer = open('ratings.csv', 'w')

lines = reader.readlines()
writer.write('userId,movieId,rating,timestamp\n')

for line in lines :
    part = line.split('::')
    writer.write(part[0] + ',' + part[1] + ',' + part[2] + ',' + part[3])

reader.close()
writer.close()
