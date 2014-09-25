library(plotrix)

a = read.csv("cnt.csv", sep="," ,nrows=1000);
b = a[,1];
print(b);
#hist(b, breaks=1000);
c = table(a$num);
print(c)

pdf("hist.pdf")
barplot(c, xlab="Number of Mementos", ylab="Number of URLs")
#plot(log(c), log="x")
dev.off()
