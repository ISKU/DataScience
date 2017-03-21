
library(ggplot2)
tashu <- na.omit(read.csv('tashu.csv', header = TRUE))

top_path <- data.frame(table(tashu $ RENT_STATION, tashu $ RETURN_STATION))
top_path <- top_path[order(top_path $ Freq, decreasing = T),]
top_path <- head(top_path, n = 20)
top_path

top_path $ Var1 <- as.factor(top_path $ Var1)
top_path $ Var2 <- as.factor(top_path $ Var2)
top_path $ size <- with(top_path, as.numeric(Freq) / 3000)
top_path

ggplot(top_path, aes(Var1, Var2)) + geom_point(shape = 19, size = top_path $ size)
