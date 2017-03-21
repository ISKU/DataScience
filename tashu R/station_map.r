
library(ggplot2)
library(ggmap)

tashu <- read.csv('tashu.csv', header = TRUE)
station <- read.csv('station.csv', header = TRUE)
rent_count <- data.frame(table(tashu $ RENT_STATION))
return_count <- data.frame(table(tashu $ RETURN_STATION))

merged <- merge(rent_count, return_count, by = 'Var1')
station_count <- data.frame(station = c(merged $ Var1), count = c(merged $ Freq.x + merged $ Freq.y))
station_count

station_info <- merge(station_count, station, by.x = 'station', by.y = '번호')
station_info

station_info $ lat <- as.numeric(sapply(strsplit(as.character(station_info $ 좌표), split = ','), '[', 1))
station_info $ lon <- as.numeric(sapply(strsplit(as.character(station_info $ 좌표), split = ','), '[', 2))
station_info

station_info $ size <- with(station_info, as.numeric(count) / 20000)
station_info $ size

map <- ggmap(get_googlemap(center = as.numeric(geocode('Daejeon')), maptype = 'roadmap', zoom = 13))
map + geom_point(data = top_station, aes(x = lon, y = lat), colour = 'red', size = top_station $ size, alpha = 0.5)
