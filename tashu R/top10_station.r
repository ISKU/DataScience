
library(ggplot2)
tashu <- read.csv('tashu.csv', header = TRUE)

top_rent <- data.frame(table(tashu $ RENT_STATION))
top_return <- data.frame(table(tashu $ RETURN_STATION))

merged <- merge(top_rent, top_return, by = 'Var1')
merged

top_station <- data.frame(station = c(merged $ Var1), count = c(merged $ Freq.x + merged $ Freq.y))
top_station <- top_station[order(top_station $ count, decreasing = T),]
top_station[1:10,]

top_station $ station <- as.factor(top_station $ station)
top_station $ count <- as.factor(top_station $ count)
ggplot(top_station[1:10,], aes(station, count, variable)) + geom_bar(stat = 'identity') + scale_colour_manual(values=c(colours(), 10))


