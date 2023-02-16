# find duplicates
duplicates = twitter[twitter.duplicated(subset="tweetID", keep=False)]
print(duplicates.count())

# print the duplicates
duplicates.head(15)

# To remove duplicates
def remove_duplicates(data):
    return data.drop_duplicates(subset="tweetID", keep="first")
twitter = remove_duplicates(twitter)
twitter.info()
