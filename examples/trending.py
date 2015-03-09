__author__ = 'calvin'

import os
from twitter import *


woeid = 2427032

CONSUMER_KEY = "Pa1ecpqDx1lhFThkf70EjiIJS"
CONSUMER_SECRET = "S9ybgB7QHnLLqzvS37YYMnUCFNo1W58Y41keN9KfwJOexE9crE"


MY_TWITTER_CREDS = os.path.expanduser('~/.my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("Calvin Eleven Tweets", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter = Twitter(auth=OAuth(
    oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

trends = twitter.trends.place(_id=woeid)

for trend in trends[0].get('trends', None):
    name = trend['name']
    url = trend['url']
    print(name, url)