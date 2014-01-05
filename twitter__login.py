# -*- coding: utf-8 -*-

import os
import twitter

import conf

def login():
    return twitter.Twitter(domain='api.twitter.com', api_version='1.1',
                auth=twitter.oauth.OAuth(conf.OAUTH_TOKEN, conf.OAUTH_TOKEN_SECRET,
                                         conf.CONSUMER_KEY, conf.CONSUMER_SECRET))

if __name__ == '__main__':
    login()
