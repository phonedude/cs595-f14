#! /usr/bin/python 

import clusters
blognames,words,data=clusters.readfile('blogdata2.txt')
clust=clusters.hcluster(data)
clusters.printclust(clust,labels=blognames)

clusters.drawdendrogram(clust,blognames,jpeg='blogdendro.jpg')
