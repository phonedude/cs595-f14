#! /usr/bin/python 

import clusters
blognames,words,data=clusters.readfile('blogdata.txt')
clust=clusters.hcluster(data)
clusters.printclust(clust,labels=blognames)

clusters.drawdendrogram(clust,blognames,jpeg='blogdendro.jpg')
