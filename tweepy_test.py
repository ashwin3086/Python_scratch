import tweepy
from tweepy import OAuthHandler
consumer_key='wdIHUveP64KOhdJiGVEdjkp8B'
consumer_secret='6jyY1sA6Dz6aZlYPXJ2nE9GwwhU4KcmPqdLmCnPGqp8xuunX96'
access_token='567899563-1HmNAIgXYxX2FcVRpPB2Y6OhJ1zyjzOB4FjGRn33'
access_secret='bNAmEuMy1FWgARaHRkbZ893DdvYCxBW9W8C7pGiqIQBw5'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

import json
def process_or_store(tweet):
    print(json.dumps(tweet))

for status in tweepy.Cursor(api.home_timeline).items(200):
    # Process a single status
    #print(status.text) 
	process_or_store(status._json)

#
#for friend in tweepy.Cursor(api.friends).items(1):
#    process_or_store(friend._json)	
	

