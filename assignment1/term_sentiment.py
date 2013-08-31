import sys
import string
import unicodedata
import json

def getSentScoreDic(sentFile):
    scores = {}  
    for eachLine in sentFile:
        term, score = eachLine.split("\t")
        scores[term.lower()] = int(score)
    return scores

"""only analyze tweet containing 'text' field"""
def getTweets(tweetFile):
    tweets = []
    for eachLine in tweetFile:
        tweet = json.loads(eachLine)
        if "text" in tweet:
            tweets.append(json.loads(eachLine))
    return tweets

def getCleanTerm(term, delTable):
    s = unicode(term.lower())
    #convert unicode to string
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore')
    #remove punctuation
    cleanTerm = s.translate(None, delTable) 
    return cleanTerm

def calculateSentScore(tweet, scoreDic):
    score = 0.0
    delTable = string.maketrans(string.ascii_letters, ' ' * \
                                        len(string.ascii_letters))    
    for term in tweet.split():
        cleanTerm = getCleanTerm(term, delTable)
        if cleanTerm in scoreDic:
            score = score + scoreDic[cleanTerm]
    return score

def findNewScore(scoreDic, tweets):
    delTable = string.maketrans(string.ascii_letters, ' ' * \
                                len(string.ascii_letters))
    termScores = {}                            
    for tweet in tweets:
        tweetScore = calculateSentScore(tweet["text"], scoreDic) 
        if tweetScore != 0:
            for term in tweet["text"].split():
                cleanTerm = getCleanTerm(term, delTable)
                if cleanTerm and cleanTerm not in scoreDic:
                    termScores[cleanTerm] = termScores.get(cleanTerm, 0.0) +\
                        tweetScore                    
    
    scoreDic.update(termScores)
    return scoreDic

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scoreDic = getSentScoreDic(sent_file)
    tweets = getTweets(tweet_file)
    for term, value in findNewScore(scoreDic, tweets).iteritems():
        if ' ' in term:
            for subTerm in term.split():
                print subTerm, value
        else:
            print term, value

if __name__ == '__main__':
    main()
