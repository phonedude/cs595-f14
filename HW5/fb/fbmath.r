#! /usr/bin/Rscript

args <- commandArgs(trailingOnly=TRUE)
input <- args[1]
fn <- unlist(strsplit(input, "/"))
name <- paste(fn[3], ".pdf", sep="")
name <- paste("./figs/", name, sep="")

print(name)

d <- read.table(input, header=TRUE, sep=",", as.is=TRUE, strip.white=TRUE)

names <-d[,1]
num <- sort(d[,2]);
names <- names[order(d[,2])];

mean(num)
sd(num)

cols <- c("grey", "black")[(names=="George C Micros")*1+1];

nF = paste("# of Friends: ", length(num));

pdf(name)
barplot(num, col=cols, main=nF, xlab="friends", ylab="# of friends", border=NA);
dev.off()
