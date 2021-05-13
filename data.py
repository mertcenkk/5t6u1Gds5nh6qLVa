import os
import time

import twint
#get data
def get_data():
    c = twint.Config()
    c.Search = "request for startup"
    c.Limit = 100
    c.Store_csv = True
    c.Output = "tweet_data.csv"
    c.Lang = "tr"
    if os.path.isfile("tweet_data.csv"):
        pass
    else:
        twint.run.Search(c)
