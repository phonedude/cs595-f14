#! /usr/bin/Rscript

library(Kendall)

a <- read.csv("tfidf");
b <- read.csv("PR.txt");

a <- a[,1];
b <- b[,1];


cor(a,b,method="kendall")
Kendall(a,b)
