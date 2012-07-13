# -*- coding: utf-8 -*-

import os
import twitter

from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import conf

def login():

    try:
        (oauth_token, oauth_token_secret) = read_token_file(conf.TOKEN_FILE)
    except IOError, e:
        (oauth_token, oauth_token_secret) = oauth_dance(conf.APP_NAME, conf.CONSUMER_KEY,
                conf.CONSUMER_SECRET)

        if not os.path.isdir('out'):
            os.mkdir('out')

        write_token_file(conf.TOKEN_FILE, oauth_token, oauth_token_secret)
         
    return twitter.Twitter(domain='api.twitter.com', api_version='1',
                        auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                        conf.CONSUMER_KEY, conf.CONSUMER_SECRET))

if __name__ == '__main__':
    login()
