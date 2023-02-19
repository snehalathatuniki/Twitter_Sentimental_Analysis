import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for tweet in sntwitter.TwitterSearchScraper('#sustainability since:2022-01-01 until:2022-12-31').get_items():
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.lang, tweet.user.location])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Content of the Tweet', 'Username', 'Language of Tweet' , 'user location'])

# Write the data to a CSV file
tweets_df2.to_csv('#sustainability.csv')
