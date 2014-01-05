# Tweet Punchcard

A simple Heroku app to display your tweets and your twitter home timeline as Github-style punchcards.

* `fetch_new_tweets.py` uses the Twitter API to fetch data about newly sent/received tweets and update the punchard data. Should be run at regular intervals, e.g. using the Heroku Scheduler.

* `app.py` is a Flask app to render the punchcards using D3.

Data is stored as a lump of JSON in Redis.

## Example

An example app is running [here](http://tweet-punchcard.herokuapp.com/).

## Required Heroku add-ons

* Scheduler

* Redis To Go

## Setup

1. Create a Twitter app. Set the `TWITTER_APP_NAME`, `TWITTER_CONSUMER_KEY` and `TWITTER_CONSUMER_KEY_SECRET` config vars: 

        heroku config:set TWITTER_APP_NAME=MyTwitterApp TWITTER_CONSUMER_KEY=... TWITTER_CONSUMER_SECRET=...

2. Run `python create_oath_token.py` and authorise your app to access your tweets. Follow the instructions to set the remaining config vars.

3. Add Heroku add-ons:

        heroku addons:add scheduler
        heroku addons:add redistogo

4. Push to Heroku

5. Set up fetching of new tweets as a scheduled task. Command: `python fetch_new_tweets.py`. Schedule: up to you.

6. If you can't wait for the first task to run, run it manually:

        heroku run python fetch_new_tweets.py

7. Open your app in a browser and check it works.

## Acknowledgements

* The Twitter OAuth login code is inspired by 'Mining the Social Web' by Matthew Russell ([github](https://github.com/ptwobrussell/Mining-the-Social-Web))

* The D3 punchcard code is based on [this code](https://github.com/jeyb/d3.punchcard) by @jeyb. 
