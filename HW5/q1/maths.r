#! /usr/bin/Rscript

d <- read.table("temp", header=TRUE, sep=",", as.is=TRUE, strip.white=TRUE)

mean(d[,2])
sd(d[,2])


names <-d[,1]
num <- sort(d[,2]);
names <- names[order(d[,2])];

cols <- c("grey", "black")[(names=="Michael L. Nelson")*1+1];

pdf("twitter.pdf")
barplot(num, col=cols, main="Twitter Friend Pradox", xlab="friends", ylab="# of friends", border=NA);
dev.off()
