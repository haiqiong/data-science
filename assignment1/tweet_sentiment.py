import sys
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

def calculateSentScore(tweet, scoreDic):
    terms = tweet.split()
    score = 0.0
    for term in terms:
        if term.lower() in scoreDic:
            score = score + scoreDic[term.lower()]
    return score

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scoreDic = getSentScoreDic(sent_file)
    tweets = getTweets(tweet_file)
    for tweet in tweets:
        print calculateSentScore(tweet["text"], scoreDic)
            

if __name__ == '__main__':
    main()
