#! /usr/bin/python 

import clusters

no = 20 
blognames,words,data=clusters.readfile('blogdata.txt')
kclust=clusters.kcluster(data,k=no) 
for i in range(no):
	print "\tCluster #"+str(i+1)+str([blognames[r] for r in kclust[i]])
