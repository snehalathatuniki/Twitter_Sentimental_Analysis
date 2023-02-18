# find duplicates
duplicates = twitter[twitter.duplicated(subset="tweetID", keep=False)]
print(duplicates.count())

# print the duplicates
duplicates.head(15)

# To remove duplicates
def remove_duplicates(data):
    return data.drop_duplicates(subset="tweetID", keep="first") #method used to remove duplicates
twitter = remove_duplicates(twitter)
twitter.info()

import re # provides regular expression matching operations.
def remove_punct(text):
    text  = "".join([char for char in text if char not in string.punctuation]) 
    ##string module that contains all punctuation characters
    ##non-punctuation characters is then joined back together into a string using the join() method
    text = re.sub('[0-9]+', '', text)
    ##removes the digits from the string
    return text

twitter['tweetContext'] = twitter['tweetContext'].apply(lambda x: remove_punct(x))
#Pandas method that applies a function to each element of a DataFrame.
twitter.head(12)
