reader = open('ml-10M100K/movies.dat', 'r')
writer = open('movies.csv', 'w')

lines = reader.readlines()
writer.write('movieId,title,genres\n')

for line in lines :
    part = line.split('::')
    writer.write(part[0] + ',' + '"' + part[1] + '"' + ',' + part[2])

reader.close()
writer.close()
