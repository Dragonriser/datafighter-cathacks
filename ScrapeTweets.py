import numpy as np
import pandas as pd

import GetOldTweets3 as got

def get_tweets(keyword,count,fromDate,toDate):

    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                             .setSince(fromDate)\
                                             .setUntil(toDate)\
                                            .setMaxTweets(count)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)

    text_tweets = [[tweet.date, tweet.text] for tweet in tweets]

    #convert to csv
    cols=["Date & Time","Tweet"]
    df=pd.DataFrame(text_tweets ,columns=cols)
    tweetCSV = df.to_csv("output.csv",index=False,header=True)
    
    return tweetCSV