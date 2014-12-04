#! /usr/bin/Rscript

a = read.csv("feedstats.txt", sep=",", head=TRUE)
b = a[,2];
pdf("freqHist.pdf")
hist(b, breaks=length(b), main="Blog Histogram", xlab="# of pages", ylab="# of blogs")
axis(side=1, at=seq(0,110,10), labels=seq(0,110,10))
axis(side=2, at=seq(0,15,2), labels=seq(0,15,2)); dev.off()

pdf("densHist.pdf")
mean.b = mean(b)
var.b = var(b)
hist(b, breaks=length(b), main="Blog Histogram", xlab="# of pages", ylab="Density", freq=F)
axis(side=1, at=seq(0,110,10), labels=seq(0,110,10))
axis(side=2, at=seq(0,15,2), labels=seq(0,15,2))
curve(dgamma(x, shape = mean.b^2/var.b, scale = var.b/mean.b), add = T); dev.off()
pdf("densHist1.pdf")
hist(b, main="Blog Histogram", xlab="# of pages", ylab="Density", freq=F)
axis(side=1, at=seq(0,110,10), labels=seq(0,110,10))
axis(side=2, at=seq(0,15,2), labels=seq(0,15,2))
curve(dgamma(x, shape = mean.b^2/var.b, scale = var.b/mean.b), add = T); dev.off()
