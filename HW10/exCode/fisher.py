import docclass
cl=docclass.fisherclassifier(docclass.getwords) 
cl.setdb('mln.db')
docclass.sampletrain(cl)
cl.fisherprob('quick','good') 
