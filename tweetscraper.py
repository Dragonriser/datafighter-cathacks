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

  return text_tweets
list_of_tweets=get_tweets("coronavirus",200,"2020-01-01","2020-03-27")
cols=["Date & Time","Tweet"]
df=pd.DataFrame(list_of_tweets,columns=cols)
df.to_csv("output.csv",index=False,header=True)
df1 = pd.read_csv (r'output.csv')
df1.to_json (r'output.json')