# -*- coding: utf-8 -*-

import sys
import os
import twitter
import json
import redis

from datetime import *
from dateutil import *
from dateutil.parser import parse
from dateutil.tz import tzoffset

from twitter__login import login

# Constants
MAX_PAGES = 10 
JST = tzoffset("JST", 9 * 3600)
REDIS_KEY = 'punchcard_data'

def main():
    redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
    red = redis.from_url(redis_url)

    print 'Loading JSON blob from Redis'
    jsonBlob = red.get(REDIS_KEY)
    if jsonBlob == None:
        print 'JSON blob not found in Redis. Creating a new one'
        data = {
            'lastUpdated': 'Never',
            'myTweets': {
                'since_id': 1,
                'count': 0,
                'punchcard': [[0] * 24 for i in range(7)]
            },
            'timeline': {
                'since_id': 1,
                'count': 0,
                'punchcard': [[0] * 24 for i in range(7)]
            }
        }
    else:
        data = json.loads(jsonBlob)

    t = login()

    print 'Building punchcard data for my tweets'
    updateData(t, "user", data['myTweets'])

    print 'Building punchcard data for timeline'
    updateData(t, "home", data['timeline'])
    
    data['lastUpdated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print 'Writing updated data to Redis'
    jsonBlob = json.dumps(data, indent = 4)
    red.set(REDIS_KEY, jsonBlob)

    print 'Done'

"""Extract the day and hour of a tweet,
where day is an int (0 = Monday, 6 = Sunday)
and hour is an int in the range [0..23].
The time will be in the JST (UTC+9).

A tweet's timestamp will be in the form:
  Thu Jun 24 14:21:11 +0000 2010
"""
def extractDayAndHour(tweet):
    timestamp = parse(tweet['created_at']).astimezone(JST)
    return (timestamp.weekday(), timestamp.hour)
    
def updateData(t, timeline_name, data):
    KW = {  # For the Twitter API call
    'count': 200,
    'skip_users': 'true',
    'include_entities': 'false',
    'since_id': data['since_id'],
    }

    max_id = data['since_id']
    page_num = 1
    num_tweets = 0

    while page_num <= MAX_PAGES:
        KW['page'] = page_num
        api_call = getattr(t.statuses, timeline_name + '_timeline')
        page_tweets = api_call(**KW)
        num_tweets += len(page_tweets)
        print 'Fetched %i tweets (total %i so far)' % (len(page_tweets), num_tweets)

        for tweet in page_tweets:
            # Update punch card data
            (day, hour) = extractDayAndHour(tweet)
            data['punchcard'][day][hour] += 1

            # Update the max tweet ID
            max_id = max(max_id, tweet['id'])

        if (len(page_tweets) == 0):
            print 'No more tweets to fetch'
            break
        page_num += 1

    print 'Punch card:'
    for day in data['punchcard']:
        print day

    # Update data fields
    data['since_id'] = max_id
    data['count'] += num_tweets


if __name__ == '__main__':
    main()
