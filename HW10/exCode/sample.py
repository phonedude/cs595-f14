import feedfilter
import docclass
c=docclass.fisherclassifier(docclass.getwords) 
c.setdb('mln-f-measure.db')
feed = 'http://f-measure.blogspot.com/feeds/posts/default?max-results=100'

feedfilter.read(feed,c)
