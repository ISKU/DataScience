
library(ggplot2)
library(ggmap)

station <- read.csv('station.csv', header = TRUE)
top5_am <- read.csv('top5_am.csv', header=TRUE)
top5_fm <- read.csv('top5_fm.csv', header=TRUE)

top5_am

top5_fm

station

top_station_am <- merge(top5_am, station, by.x = 'rent_station', by.y = 'no')
top_station_am

map <- ggmap(get_googlemap(center = as.numeric(geocode('Daejeon')), maptype = 'roadmap', zoom = 13))
map + geom_point(data = top_station_am, aes(x = lat, y = lon), colour = 'red', size = top_station_am $ count * 0.01, alpha = 0.5)

top_station_fm <- merge(top5_fm, station, by.x = 'rent_station', by.y = 'no')
top_station_fm

map <- ggmap(get_googlemap(center = as.numeric(geocode('Daejeon')), maptype = 'roadmap', zoom = 13))
map + geom_point(data = top_station_fm, aes(x = lat, y = lon), colour = 'red', size = top_station_fm $ count * 0.006, alpha = 0.5)


