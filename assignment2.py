#project code
#write-up can be found in the readme.md file

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from twython import Twython
import pprint
import matplotlib.pyplot as plot


def twitter_ukraine(keyword, tweet_number=100):
    """scrub through twitter for tweets with #Russia and return the first 100 tweets as a list"""
    ###enters API keys###
    APP_KEY = "9iNbqBABwgvjucc9dE2pW7mTm"
    APP_SECRET = "PIVYIesOdEVCvrdQbI81YzrpPCdExhA32QkvsYefgSkijBKeZK"
    twitter = Twython(APP_KEY, APP_SECRET)
    ###searches###
    data = twitter.search(q=f"{keyword}", count=tweet_number)
    ###creates list of tweets###
    global ukraine_tweets
    ukraine_tweets = []
    for status in data["statuses"]:
        ukraine_tweets.append(status["text"])
    return ukraine_tweets


def twitter_russia(keyword, tweet_number=100):
    """scrub through twitter for tweets with #Russia and return the first 100 tweets as a list"""
    ###enters API keys###
    APP_KEY = "9iNbqBABwgvjucc9dE2pW7mTm"
    APP_SECRET = "PIVYIesOdEVCvrdQbI81YzrpPCdExhA32QkvsYefgSkijBKeZK"
    twitter = Twython(APP_KEY, APP_SECRET)
    ###searches###
    data = twitter.search(q=f"{keyword}", count=tweet_number)
    ###creates list of tweets###
    global russia_tweets
    russia_tweets = []
    for status in data["statuses"]:
        russia_tweets.append(status["text"])
    return russia_tweets


def sentiment_ukraine(): 
    global ukraine_score
    ukraine_score = []
    for tweets in ukraine_tweets: 
        score = SentimentIntensityAnalyzer().polarity_scores(tweets)
        ukraine_score.append(score)
    return ukraine_score


def sentiment_russia(): 
    global russia_score
    russia_score = []
    for tweets in russia_tweets: 
        score = SentimentIntensityAnalyzer().polarity_scores(tweets)
        russia_score.append(score)
    return russia_score


def ukraine_analyze(): 
    total_neutral = 0
    total_negative = 0 
    total_positive = 0
    total_compound = 0
    for scores in ukraine_score:
        total_neutral = total_neutral + scores['neu']
        total_negative = total_negative + scores['neg']
        total_positive = total_positive + scores['pos']
        total_compound = total_compound + scores['compound']
    avg_neutral = total_neutral/len(ukraine_score)
    avg_negative = total_negative/len(ukraine_score)
    avg_positive = total_positive/len(ukraine_score)
    avg_compound = total_compound/len(ukraine_score)
    print(avg_neutral, avg_negative, avg_positive, avg_compound)


def russia_analyze(): 
    total_neutral = 0
    total_negative = 0 
    total_positive = 0
    total_compound = 0
    for scores in russia_score:
        total_neutral = total_neutral + scores['neu']
        total_negative = total_negative + scores['neg']
        total_positive = total_positive + scores['pos']
        total_compound = total_compound + scores['compound']
    avg_neutral = total_neutral/len(russia_score)
    avg_negative = total_negative/len(russia_score)
    avg_positive = total_positive/len(russia_score)
    avg_compound = total_compound/len(russia_score)
    print(avg_neutral, avg_negative, avg_positive, avg_compound)


def twitter_zelensky(keyword, tweet_number=1000):
    """scrub through twitter for tweets related to Prime Minister Zelensky and return the first 100 tweets as a list"""
    ###enters API keys###
    APP_KEY = "9iNbqBABwgvjucc9dE2pW7mTm"
    APP_SECRET = "PIVYIesOdEVCvrdQbI81YzrpPCdExhA32QkvsYefgSkijBKeZK"
    twitter = Twython(APP_KEY, APP_SECRET)
    ###searches###
    data = twitter.search(q=f"{keyword}", count=tweet_number)
    ###creates list of tweets###
    global zelensky_tweets
    zelensky_tweets = []
    for status in data["statuses"]:
        zelensky_tweets.append(status["text"])
    return zelensky_tweets


def twitter_putin(keyword, tweet_number=1000):
    """scrub through twitter for tweets related to Vladimir Putin and return the first 100 tweets as a list"""
    ###enters API keys###
    APP_KEY = '9iNbqBABwgvjucc9dE2pW7mTm'
    APP_SECRET = 'PIVYIesOdEVCvrdQbI81YzrpPCdExhA32QkvsYefgSkijBKeZK'
    twitter = Twython(APP_KEY, APP_SECRET)
    ###searches###
    data = twitter.search(q=f"{keyword}", count=tweet_number)
    ###creates list of tweets###
    global putin_tweets
    putin_tweets = []
    for status in data['statuses']:
        putin_tweets.append(status['text'])
    return putin_tweets


def sentiment_zelensky(): 
    global zelensky_score
    zelensky_score = []
    for tweets in zelensky_tweets: 
        score = SentimentIntensityAnalyzer().polarity_scores(tweets)
        zelensky_score.append(score)
    return zelensky_score


def sentiment_putin(): 
    global putin_score
    putin_score = []
    for tweets in putin_tweets: 
        score = SentimentIntensityAnalyzer().polarity_scores(tweets)
        putin_score.append(score)
    return putin_score


def zelensky_analyze(): 
    total_neutral = 0
    total_negative = 0 
    total_positive = 0
    total_compound = 0
    global zelensky_negative
    zelensky_negative = []
    global zelensky_positive
    zelensky_positive = []
    for scores in zelensky_score:
        total_neutral = total_neutral + scores['neu']
        total_negative = total_negative + scores['neg']
        total_positive = total_positive + scores['pos']
        total_compound = total_compound + scores['compound']
        zelensky_negative.append(scores['neg'])
        zelensky_positive.append(scores['pos'])
    avg_neutral = total_neutral/len(zelensky_score)
    avg_negative = total_negative/len(zelensky_score)
    avg_positive = total_positive/len(zelensky_score)
    avg_compound = total_compound/len(zelensky_score)
    print(avg_neutral, avg_negative, avg_positive, avg_compound)


def putin_analyze(): 
    total_neutral = 0
    total_negative = 0 
    total_positive = 0
    total_compound = 0
    global putin_negative
    putin_negative = []
    global putin_positive
    putin_positive = []
    for scores in putin_score:
        total_neutral = total_neutral + scores['neu']
        total_negative = total_negative + scores['neg']
        total_positive = total_positive + scores['pos']
        total_compound = total_compound + scores['compound']
        putin_negative.append(scores['neg'])
        putin_positive.append(scores['pos'])
    avg_neutral = total_neutral/len(putin_score)
    avg_negative = total_negative/len(putin_score)
    avg_positive = total_positive/len(putin_score)
    avg_compound = total_compound/len(putin_score)
    print(avg_neutral, avg_negative, avg_positive, avg_compound)

def zelensky_visual():
    plot.scatter(zelensky_positive, zelensky_negative, c = "blue")
    plot.xlabel('Positive')
    plot.ylabel('Negative')
    plot.show()

def putin_visual():
    plot.scatter(putin_positive, putin_negative, c = "red")
    plot.xlabel('Positive')
    plot.ylabel('Negative')
    plot.show()

def main(): 
    twitter_putin('putin', 1000)
    twitter_zelensky('zelensky', 1000)
    sentiment_putin()
    sentiment_zelensky()
    zelensky_analyze()
    putin_analyze()
    zelensky_visual()
    putin_visual()

if __name__ == "__main__":
       main()