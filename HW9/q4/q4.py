#! /usr/bin/python 

import clusters
blognames,words,data=clusters.readfile('blogdata.txt')
coords=clusters.scaledown(data)
clusters.draw2d(coords,blognames,jpeg='blogs2d.jpg')
