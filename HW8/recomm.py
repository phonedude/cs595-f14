#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
# A dictionary of movie critics and their ratings of a small set of movies
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}


def sim_distance(prefs, p1, p2):
    '''
    Returns a distance-based similarity score for person1 and person2.
    '''

    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in
                         prefs[p1] if item in prefs[p2]])
    #return 1 / (1 + sum_of_squares)
    return sum_of_squares


def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
    # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
        # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


def calculateSimilarItems(prefs, n=5):
    '''
    Create a dictionary of items showing which other items they are
    most similar to.
    '''

    result = {}
    # Invert the preference matrix to be item-centric
    #itemPrefs = transformPrefs(prefs)
    itemPrefs = prefs
    c = 0
    for item in itemPrefs:
        # Status updates for large datasetsa
        c += 1
        if c % 100 == 0:
            print '%d / %d' % (c, len(itemPrefs))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_pearson)
        result[item] = scores
    return result


def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():
        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings:
                continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    # Divide each total score by total weighting to get an average
    rankings = [(score / totalSim[item], item) for (item, score) in
                scores.items()]
    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings


def loadMovieLens(path='./ml-100k'):
  # Get movie titles
    movies = {}
    for line in open(path + '/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
  # Load data
    prefs = {}
    for line in open(path + '/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs


def greedy(prefs, best):
    c = [[]]*(len(prefs))
    for i in prefs:
        e = []
        for j in prefs:
            d = []
            num = sim_pearson(prefs,i,j);
            d.append(num)
            d.append(i)
            d.append(j)
            if (i != j):
                e.append(d)
        e.sort(key=lambda x:x[:][0], reverse=best)
        #print int(e[0][1])
        c[int(e[0][1])-1] = e[0]
        
    return c     

def dist(prefs):
    c = []

    for i in prefs:
        c.append(topMatches(prefs, i, 1, sim_pearson))
    
    # for i in c:
    #     i.append(sum(pair[0] for pair in i))

    c.sort(key=lambda x:x[5], reverse=True)

    return c
def maths(c, prefs):
    d = []
    for i in c:
        e = []
        e.append(i[1])
        e.append(i[2])
        for j in range(2,5):
            e.append(c[int(e[j-1])-1][2])
        

        tSum = 0
        for j in range (0,5):
            for k in range (0,5):
                tSum +=  sim_pearson(prefs, e[j], e[k])
        e.append(tSum)
        d.append(e)
    return d


def q7():
    prefs =  loadMovieLens(path='./ml-100k')   
    c = greedy(prefs, True)
    x = maths(c, prefs)

    x.sort(key=lambda x:x[5], reverse=True)
    y = []
    for i in x:
        if len(i) == len(set(i)):
            y.append(i)

    print "Most Agreed Reviewers"
    for i in range(0,5):
        print y[i]


def q8():
    prefs =  loadMovieLens(path='./ml-100k')
    c = greedy(prefs, False)
    x = maths(c, prefs)

    x.sort(key=lambda x:x[5], reverse=False)
    y = []
    for i in x:
        if len(i) == len(set(i)):
            y.append(i)
    print "Least Agreed Reviewers"
    for i in range(0,5):
        print y[i]

prefs =  loadMovieLens(path='./ml-100k')
# a =  calculateSimilarItems(prefs, 4)
# d = []
# for pps in a:
#     temp = 0
#     e = []
#     ps = a[str(pps)]
#     for i in ps:
#         for j in ps:
#             temp += sim_pearson(prefs, i[1], j[1]) 
#     e.append(pps)
#     for i in ps:
#         e.append(i[1])        
#     e.append(temp)
#     d.append(e)
# greedy(prefs)
# #print c
# d = maths(c, prefs)
# d.sort(key=lambda x:x[5])
# for i in d: 
#     if len(i) == len(set(i)):   
#         print i


