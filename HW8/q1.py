#! /usr/bin/python

from scipy.stats.stats import pearsonr
import math

class movie:
	def __init__(self, data):
		data = data.strip('\n').split('|')
		
		self.id 	= int(data[0])
		self.title 	= data[1].replace(',', '')
		self.data 	= data[2]
		self.vid 	= data[3]
		self.url 	= data[4]
		self.genre 	= data[5:len(data)]
		self.scores	= []
		self.cnt	= 0
		self.avg 	= 0
		self.rvwrs	= []

	def avgr(self):
		if self.cnt > 0:
			self.avg = sum(self.scores)/self.cnt
		else:
			self.avg = 0


class user:
	def __init__(self,data):
		data = data.strip('\n').split('|')

		self.id 	= int(data[0])
		self.age	= int(data[1])
		self.sex	= data[2]
		self.job	= data[3]
		self.zip 	= data[4]
		self.film   = {}
		self.cnt	= 0

class review:
	def __init__(self, data):
		data = data.strip('\n').split('\t')

		self.user 	= int(data[0])
		self.item	= int(data[1])
		self.score	= int(data[2])
		self.time	= int(data[3])

def clearScore(movies):
	for i in movies:
		i.scores = []
		i.cnt = 0
		i.avg = 0




movies 	= []
users 	= []
reviews = []
f = open("./ml-100k/u.item")
for i in f:
	movies.append(movie(i))

f = open("./ml-100k/u.user")
for i in f:
	users.append(user(i))

f = open("./ml-100k/u.data")	
for i in f:
	reviews.append(review(i))


# HIGHEST RATING
def q1(movies):
	clearScore(movies)
	for i in reviews:
		movies[i.item-1].scores.append(float(i.score))
		movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	hRate = sorted(movies, key=lambda x:(x.avg, x.title), reverse=True)
	f = open("q1.txt", "w")
	
	print "\n\tQ1: Highest Average Rating"
	for i in range(0,20):
		print  '%.4f'%hRate[i].avg, hRate[i].title
		f.write("%.4f ,  \"%s\"\n" % (hRate[i].avg, hRate[i].title))

	f.close()
def q2(movies):
	clearScore(movies)
	for i in reviews:
		movies[i.item-1].scores.append(float(i.score))
		movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr();

	# MOST RATING
	mRate = sorted(movies, key=lambda x:x.cnt, reverse=True)
	f = open("q2.txt", "w")
	print "\n\tQ2: Most Ratings"
	for i in range(0,5):
		print  mRate[i].cnt, mRate[i].title
		f.write("% d,  \"%s\"\n" % (mRate[i].cnt, mRate[i].title))
	f.close()

# MEN
def q4(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if users[i.user-1].sex == "M":
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	men = sorted(movies, key=lambda x:x.avg, reverse=True)

	f = open("q4.txt", "w")
	print "\n\tQ4: Highest Average by men"
	for i in range(0,30):
		print  '%.4f'%men[i].avg, men[i].title
		f.write("%.4f,  \"%s\"\n" % (men[i].avg, men[i].title))
	f.close()
# WOMEN
def q3(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if users[i.user-1].sex == "F":
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	wmn = sorted(movies,key=lambda x:(x.avg, x.title), reverse=True)

	f = open("q3.txt", "w")
	print "\n\tQ3: Highest Average by women"
	for i in range(0,20):
		print  '%.4f'%wmn[i].avg, wmn[i].title
		f.write("%.4f,  \"%s\"\n" % (wmn[i].avg, wmn[i].title))
	f.close()
# MEN OVER 40
def q9a(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if (users[i.user-1].sex == "M") and (users[i.user-1].age > 40):
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	m40 = sorted(movies,key=lambda x:(x.avg, x.title), reverse=True)

	# 
	f = open("q9a.txt", "w")
	print "\n\tQ9a: Highest Average by men over 40"
	for i in range(0,30):
		print  '%.4f'%m40[i].avg, m40[i].title
		f.write("%.4f,  \"%s\"\n" % (m40[i].avg, m40[i].title))
	f.close()
# MEN UNDER 40
def q9b(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if (users[i.user-1].sex == "M") and (users[i.user-1].age < 40):
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	m30 = sorted(movies,key=lambda x:(x.avg, x.title), reverse=True)

	# 
	f = open("q9b.txt", "w")
	print "\n\tQ9b: Highest Average by men under 40"
	for i in range(0,40):
		print  '%.4f'%m30[i].avg, m30[i].title 	
		f.write("%.4f,  \"%s\"\n" % (m30[i].avg, m30[i].title ))
	f.close()

	# WOMEN OVER 40
def q10a(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if (users[i.user-1].sex == "F") and (users[i.user-1].age > 40):
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	w40 = sorted(movies,key=lambda x:(x.avg, x.title), reverse=True)

	# 
	f = open("q10a.txt", "w")
	print "\n\tQ10a: Highest Average by women over 40"
	for i in range(0,40):
		print  '%.4f'%w40[i].avg, w40[i].title
		f.write("%.4f,  \"%s\"\n" % (w40[i].avg, w40[i].title))
	f.close()


# MEN UNDER 40
def q10b(rmovies, reviews, users):
	clearScore(movies)

	for i in reviews:
		if (users[i.user-1].sex == "F") and (users[i.user-1].age < 40):
			movies[i.item-1].scores.append(float(i.score))
			movies[i.item-1].cnt +=1

	for i in movies:
		i.avgr(); 
	w30 = sorted(movies,key=lambda x:(x.avg, x.title), reverse=True)

	# 
	f = open("q10b.txt", "w")
	print "\n\tQ10b: Highest Average by women under 40"
	for i in range(0,40):
		print  '%.4f'%w30[i].avg, w30[i].title	
		f.write("%.4f,  \"%s\"\n" % (w30[i].avg, w30[i].title))
	f.close()	

# RATES
def q6(users):
	for i in reviews:
		users[i.user-1].cnt += 1

	usr = sorted(users,key=lambda x:x.cnt, reverse=True)

	# 
	f = open("q6.txt", "w")
	print "\n\tQ6: Rated most pics"
	print  "cnt, id"
	for i in range(0,5):
		print  usr[i].cnt, usr[i].id
		f.write("%d,  %d\n" % (usr[i].cnt, usr[i].id))
	f.close()


# CORR TOP GUN
def q5(movies, reviews, users):
	clearScore(movies)

	for i in reviews:
		movies[i.item-1].scores.append(i.score)
		movies[i.item-1].cnt +=1
		if "Top Gun" in movies[i.item-1].title:
			id = movies[i.item-1].id
			temp = movies[i.item-1].scores


	for i in reviews:
		movies[i.item-1].rvwrs.append(i.user)
		users[i.user-1].film[str(i.item)] = float(i.score)

	guys = movies[id-1].rvwrs

	c1 = []
	for i in guys:
		c1.append(users[i-1].film[str(id)])

	corr = []

	for i in movies:
		c1 = []
		c2 = []	
		for j in guys:
			if(j in i.rvwrs):
				c1.append(users[j-1].film[str(i.id)])
				c2.append(users[j-1].film[str(id)]);
		if (len(c1) > 1):
			num = pearsonr(c1,c2)
			#print num
			#raw_input()
			if (not math.isnan(num[0])):
				corr.append([num,i.id])
	mt = sorted(corr, key=lambda x:x[:][0], reverse=True)	

	f = open("q5a.txt", "w")
	print "\n\tQ5a: MOST LIKE TOP GUN"
	for i in range(0,25):
		print '%.4f'%mt[i][0][0], movies[mt[i][1]-1].title	
		f.write("%.9f,  %s\n" % (mt[i][0][0], movies[mt[i][1]-1].title	))
	f.close()

	lt = sorted(corr, key=lambda x:x[:][0], reverse=False)	

	f = open("q5b.txt", "w")
	print "\n\tQ5b: LEAST LIKE TOP GUN"
	for i in range(0,25):
		print '%.4f'%lt[i][0][0], movies[lt[i][1]-1].title	
		f.write("%.4f,  %s\n" % (lt[i][0][0], movies[lt[i][1]-1].title))
	f.close()	


# CORR RATES
def corrR(users):
	corrR = []

	for i in users:
		a = i.film.keys();
		for j in users:
			c1 = []
			c2 = []
			if(i != j):			
				for k in a:
					if( k in j.film):
						c1.append(i.film.get(k,None))
						c2.append(j.film.get(k,None))
				if (len(c1) > 1):
					num = pearsonr(c1,c2)
					#print num
					#raw_input()
					if (not math.isnan(num[0])):
						corrR.append([num,i.id, j.id])

	raters  = sorted(corrR, key=lambda x:x[:][0], reverse=True)

	for i in range(0,20):
		print raters[i]

# DOING STUFF
#q1(movies)
#q2(movies)
#q3(movies, reviews, users)
#q4(movies, reviews, users)
#q5(movies, reviews, users)
#q6(users)


#q9a(movies, reviews, users)
#q9b(movies, reviews, users)
#q10a(movies, reviews, users)
#q10b(movies, reviews, users)