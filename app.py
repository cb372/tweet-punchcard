import os
import redis
import sys
from flask import Flask, render_template

import fetch_new_tweets

app = Flask(__name__)
app.logger.debug('hello app')

REDIS_KEY = 'punchcard_data'
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
red = redis.from_url(redis_url)
app.logger.debug('hello redis')

@app.route('/')
def home():
    data = red.get(REDIS_KEY)
    return render_template('index.html', data=data)

@app.route('/wibble')
def update():
    fetch_new_tweets.main()
    return "Update complete!"

@app.route('/<path:path>')
def site(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
