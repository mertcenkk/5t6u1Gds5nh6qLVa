import csv
import os.path

import data
tweets = list()
sortedReply = list()
sortedLike = list()
sortedDate = list()

def parse_to_csv():
    with open('tweet_data.csv', 'r',encoding="utf-8") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            tweets.append(
                {'date': row[2], 'username': row[7], 'name': row[8], 'tweet': row[10], "replies_count": int(row[15]),
                 "retweet_count": int(row[16]), "like_count": int(row[17])})

if os.path.isfile("tweet_data.csv"):
    parse_to_csv()
else:
    data.get_data()
    parse_to_csv()

sortedReply = sorted(tweets, key=lambda k: k["replies_count"], reverse=True)
sortedLike = sorted(tweets, key=lambda k: k["like_count"], reverse=True)
sortedRetweet = sorted(tweets, key=lambda k: k["retweet_count"], reverse=True)
sortedDate = sorted(tweets, key=lambda k: k["date"], reverse=True)

def paginate(page, pages):
    pages = page+pages
    if pages> len(tweets):
        pages=0
    return tweets[page:pages]


# for i in range(len(tweets)):
#     print(tweets[i]["date"])
#     print(tweets[i]["username"])
#     print(tweets[i]["tweet"])