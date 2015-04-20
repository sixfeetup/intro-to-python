"""
Copyright 2015 Six Feet Up, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
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
