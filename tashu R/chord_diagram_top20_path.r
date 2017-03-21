
library(chorddiag)
library(RColorBrewer)
tashu <- na.omit(read.csv('tashu.csv', header = TRUE))

top_path <- data.frame(table(tashu $ RENT_STATION, tashu $ RETURN_STATION))
top_path <- top_path[order(top_path $ Freq, decreasing = T),]
top_path <- head(top_path, n = 20)
top_path

matrix_path <- matrix(0, nrow = 144, ncol = 144)
dimnames(matrix_path) <- list(have = 1:144, prefer = 1:144)
matrix_path

for (i in 1 : nrow(top_path))
    matrix_path[top_path[i, 1], top_path[i, 2]] <- top_path[i, 3]

matrix_path

qual_col_pals = brewer.pal.info[brewer.pal.info $ category == 'qual',]
color_vector = unlist(mapply(brewer.pal, qual_col_pals $ maxcolors, rownames(qual_col_pals)))

chorddiag(matrix_path, groupColors = color_vector, groupnamePadding = 50)
