reader = open('ml-10M100K/ratings.csv', 'r')
output = open('test.csv', 'w')

lines = reader.readlines()
output.write(lines[0])

extract = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
for index in extract :
    output.write(lines[index])

reader.close()
output.close()
