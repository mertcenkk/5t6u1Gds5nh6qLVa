from flask import Flask, render_template
from tweet import tweets, sortedReply, sortedLike, sortedRetweet,sortedDate
import tweet
app = Flask(__name__)

@app.route('/')
def index(page=0):
    page = page
    pages = 5
    #tweets = tweet.paginate(page,pages)
    return render_template('show_tweets.html', tweets=tweets, count=len(tweets))
@app.route('/order_by_reply')
def sort_by_reply():
    return render_template('show_tweets.html', tweets=sortedReply, count=len(tweets))

@app.route('/order_by_like')
def sort_by_like():
    return render_template('show_tweets.html', tweets=sortedLike, count=len(tweets))

@app.route('/order_by_retweet')
def sort_by_retweet():
    return render_template('show_tweets.html', tweets=sortedRetweet, count=len(tweets))

@app.route('/order_by_date')
def sort_by_date():
    return render_template('show_tweets.html', tweets=sortedDate, count=len(tweets))
