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

if (__name__=='__main__'):
    user=input("Enter username:")
    client=get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(5):
        print (status.text)


# url = 'https://api.Twitter.com/1.1/search/tweets.json'
# url2= 'https://api.twitter.com/2/tweets/search/recent?query=conversation_id:1279940000004973111&tweet.fields=in_reply_to_user_id,author_id,created_at,conversation_id'
# q = '%23bbcworldservice&since_id=489366839953489920'
# pms = {'q' : q, 'count' : 100, 'lang' : 'en', 'result_type': 'recent'}  
# res = requests.get(url, params = pms, auth=twitter_auth)   
# tweets = res.json()

