# import modules
import tweepy
from Crawler import config

# Define functions
'''
 Core functionality
 https://docs.tweepy.org/en/stable/client.html?highlight=client
'''
def getClient():
    return tweepy.Client(bearer_token=config.bearer_token,
                           consumer_key=config.consumer_key,
                           consumer_secret=config.consumer_secret,
                           access_token=config.access_token,
                           access_token_secret=config.access_token_secret)

'''
 Limits: https://developer.twitter.com/en/docs/twitter-api/rate-limits
 Tweepy-Docs: https://docs.tweepy.org/en/stable/
 search_recent_tweets: https://docs.tweepy.org/en/stable/client.html?highlight=search_recent_tweets#tweepy.Client.search_recent_tweets
 query: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#build
'''
def getTweets(query, max_results):
    # Get tweets
    tweets = getClient().search_recent_tweets(query=query, max_results=max_results)
    tweet_data = tweets.data

    # Convert to json Array
    results = []
    if tweet_data and len(tweet_data) > 0:
            for tweet in tweet_data:
                    jsonEntry = {}
                    jsonEntry['text'] = tweet.text
                    results.append(jsonEntry)
    else:
        return 'No tweets'

    return results

if __name__ == '__main__':
    searchQuery = "#dog"
    max_results = 10
    print(getTweets(searchQuery, max_results))
