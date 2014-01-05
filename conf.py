# -*- coding: utf-8 -*-

import os

# Go to http://twitter.com/apps/new to create an app and get these items
# See also http://dev.twitter.com/pages/oauth_single_token

APP_NAME = os.getenv('TWITTER_APP_NAME', 'MyApp')
CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY', 'MyConsumerKey')
CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET', 'MyConsumerSecret')
OAUTH_TOKEN = os.getenv('TWITTER_OAUTH_TOKEN', 'MyOAuthToken')
OAUTH_TOKEN_SECRET = os.getenv('TWITTER_OAUTH_TOKEN_SECRET', 'MyOAuthTokenSecret')
