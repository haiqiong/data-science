import sys
import string
import json
import unicodedata

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

def main():
    tweet_file = open(sys.argv[1])
    tweets = getTweets(tweet_file)
    freqDict = {}
    sum = 0
    delTable = string.maketrans(string.ascii_letters, ' ' * \
                                    len(string.ascii_letters))    
    for tweet in tweets:
        for term in tweet['text'].split():
            sum = sum + 1
            cleanTerm = getCleanTerm(term, delTable)
            freqDict[cleanTerm] = freqDict.get(cleanTerm, 0) + 1

    for k, v in freqDict.iteritems():
        print k, float(v) / sum
        
if __name__ == '__main__':
    main()

    