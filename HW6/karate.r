#! /usr/bin/Rscript

library("igraph")
library("igraphdata")

graphics.off()

data(karate)
g <- karate
h <- karate
f <- karate
g<-set.vertex.attribute(g,"name",index=(2:33), (2:33))
colrs <- c("red", "blue")[get.vertex.attribute(g,"Faction")]
plot(g,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Original")
repeat
{
  a <- edge.betweenness(g)
	g <- delete.edges(g,which.max(a))

	if(clusters(g)$no == 2)
	{
		#colrs <- c("red","blue")[get.vertex.attribute(g,"Faction")]
		colrs <- c("red", "blue")[clusters(g)$membership]
		h<-set.vertex.attribute(h,"name",index=(2:33), (2:33))
		dev.new()
		plot(h,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Girvan-Newman")
		break;
	}
}

j <- leading.eigenvector.community(h, steps=1, weights=get.edge.attribute(h,"weight"))
f <- set.vertex.attribute(f,"Faction", index=(1:34), j$membership);
colrs <- c("red", "blue")[get.vertex.attribute(f, "Faction")]
dev.new()
plot(h,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Leading Eigenvector - 2 class")

# 3 class

j <- leading.eigenvector.community(h, steps=3, weights=get.edge.attribute(h,"weight"))
f <- set.vertex.attribute(f,"Faction", index=(1:34), j$membership);
colrs <- c("red", "blue", "green")[get.vertex.attribute(f, "Faction")]
dev.new()
plot(h,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Leading Eigenvector - 3 Class")
# 4 class

j <- leading.eigenvector.community(h, steps=4, weights=get.edge.attribute(h,"weight"))
f <- set.vertex.attribute(f,"Faction", index=(1:34), j$membership);
colrs <- c("red", "blue", "green", "yellow")[get.vertex.attribute(f, "Faction")]
dev.new()
plot(h,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Leading Eigenvector - 4 Class")

# 5 class

j <- leading.eigenvector.community(h,  weights=get.edge.attribute(h,"weight"))
f <- set.vertex.attribute(f,"Faction", index=(1:34), j$membership);
colrs <- c("red", "blue", "green", "yellow", "pink")[get.vertex.attribute(f, "Faction")]
dev.new()
plot(h,vertex.color=colrs, vertex.size=25,layout=layout.fruchterman.reingold(g,niter=500,area=vcount(g)^2.3,repulserad=vcount(g)^2),  main="Leading Eigenvector - 5 Class")

