A simple Heroku app to display your tweets and your twitter home timeline as Github-style punchcards.

* `fetch_new_tweets.py` uses the Twitter API to fetch data about newly sent/received tweets and update the punchard data. Should be run at regular intervals, e.g. using the Heroku Scheduler.

* `app.py` is a Flask app to render the punchcards using D3.

Data is stored as a lump of JSON in Redis.

== Example ==

An example app is running [here](http://sharp-journey-9303.herokuapp.com/).

== Required Heroku add-ons ==

* Scheduler

* Redis To Go

== Setup ==

1. Create a Twitter app. Rename `conf.py.example` to `conf.py` and fill in the details for your app.

2. Run `python twitter__login.py` and authorise your app to access your tweets. Add the resulting file `out/twitter.oauth` to git.

3. Add Heroku add-ons:

    heroku addons:add scheduler
    heroku addons:add redistogo:nano

4. Push to Heroku

5. Set up fetching of new tweets as a scheduled task. Command: `python fetch_new_tweets.py`. Schedule: up to you.

6. If you can't wait for the first task to run, run it manually:

    heroku run python fetch_new_tweets.py

7. Open your app in a browser and check it works.

== Acknowledgements ==

* The Twitter OAuth login code is taken from 'Mining the Social Web' by Matthew Russell ([github](https://github.com/ptwobrussell/Mining-the-Social-Web))

* The D3 punchcard code is based on [this code](https://github.com/jeyb/d3.punchcard) by @jeyb. 
