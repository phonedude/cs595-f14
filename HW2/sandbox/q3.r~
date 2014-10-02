a = read.csv("stripped.csv")

pdf("plot1.pdf")
plot(a[,1], a[,2], xlab="Days", ylab="Mementos")
dev.off()

pdf("plot2.pdf")
plot(log(a[,1]), (a[,2]), xlim=range(0:10), ylim=range(0:500), xlab="Log(Days)", ylab="Mementos")
dev.off()

pdf("plot3.pdf")
plot(log(a[,1]), log(a[,2]), xlim=range(0:10), ylim=range(0:10), xlab="Log(Days)", ylab="Log(Mementos)")
dev.off()
