# -*- coding: utf-8 -*-

import twitter
from twitter.oauth_dance import oauth_dance

import conf
print 'hello'
(oauth_token, oauth_token_secret) = oauth_dance(conf.APP_NAME, conf.CONSUMER_KEY, conf.CONSUMER_SECRET)

print 'Run the following command to save OAuth token info as Heroku config vars:'
print
print 'heroku config:set TWITTER_OAUTH_TOKEN=%s TWITTER_OAUTH_TOKEN_SECRET=%s' % (oauth_token, oauth_token_secret)
