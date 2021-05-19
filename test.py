import sys,tweepy
import requests
from requests_oauthlib import OAuth1

def twitter_auth():
    try:
        consumer_key = '6gL1BMq1AtLt1FLEszxjexu8Z'
        consumer_secret = 'wg0Ei56L7sY0094Y6oCKM1u2nXvq3g04PrlqhnsNCT4scOxBa9'
        access_token = '1393901011190771714-x65HpN0w1n51tLkta2RHh7Xqsw6YKa'
        access_secret = 'fYayf9c1KEG6j4DCbxr1HEEruMd0ZK0wMWWStrsXKLsbu'
    except KeyError:
        sys.stderr.write("Twitter_ environment variable not set \n")
        sys.exit(1)
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth

def get_twitter_client():
    auth = twitter_auth()
    client=tweepy.API(auth,wait_on_rate_limit=True)
    return client


id_of_tweet = "1394819922320969730"
if (__name__=='__main__'):
   
    client=get_twitter_client()
    tweet = client.get_status(id_of_tweet,count=200,tweet_mode="extended")
    
print(tweet)
# api=tweepy.API(auth=twitter_auth(),wait_on_rate_limit=True)




# url = 'https://api.Twitter.com/1.1/search/tweets.json'
# q = '%23bbcworldservice&since_id=489366839953489920'
# pms = {'q' : q, 'count' : 100, 'lang' : 'en', 'result_type': 'recent'}
# res = requests.get(url, params = pms, auth=twitter_auth)
# tweets = res.json()

# print(id_of_tweet.full_text)
# print(id_of_tweet.user.name)
# print(id_of_tweet.favorite_count)
# print(id_of_tweet.retweet_count)

