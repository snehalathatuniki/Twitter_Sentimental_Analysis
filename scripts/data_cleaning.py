# To find duplicates
# Select all rows in the "twitter" dataframe that have duplicated values in the "tweetID" column
duplicates = twitter[twitter.duplicated(subset="tweetID", keep=False)]

# Count the number of rows in the "duplicates" dataframe
print(duplicates.count())
#prints the duplicates

# print the duplicates
duplicates.head(15)

# To remove duplicates
# We define a function called "remove_duplicates" that takes a dataframe as input
def remove_duplicates(data):
    # Removes duplicates in the "tweetID" column of the input dataframe, 
    # keeping only the first occurrence of each duplicated row
    return data.drop_duplicates(subset="tweetID", keep="first")

# Apply the "remove_duplicates" function to the "twitter" dataframe and assign the result back to "twitter"
twitter = remove_duplicates(twitter)

# Import the "string" modules
import string
# Defining a function to remove punctuation, numbers and whitespaces from a string:
def remove_punctuation_and_numbers(text):
    # Replace punctuation with spaces
    text = text.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    # Remove numbers
    text = ''.join([i for i in text if not i.isdigit()])
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

# Import the "re" modules
import re

# Define a function to remove URLs, hashtags, and mentions from a string
def remove_URL_mentions_hashtags(text):
    # Remove URLs
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b','', text, flags=re.MULTILINE)
    # Remove hashtags
    text = re.sub(r'#\w*', '', text)
    # Remove mentions
    text = re.sub(r'@\w*', '', text)
    return text.strip() #the strip() method to remove any extra whitespace from the string.

# Apply the function to the tweet text column
twitter['tweetContext'] = twitter['tweetContext'].apply(remove_URL_mentions_hashtags)

# We defining a function called "remove_special_characters" that may remove any other special charcters remaining:
def remove_special_characters(text):
    # Remove consecutive newline characters from the "tweetContext" column of the input dataframe
    text = re.sub(r'\n+', ' ', text)
    # Remove special characters (except for apostrophes) from the "tweetContext" column of the input dataframe
    re.sub(r"[^\w\s\n']|_", '', text)
    # Remove URLs, mentions, and hashtags from the "tweetContext" column of the input dataframe
    text = re.sub(r'(http\S+)|(@\S+)|(#\S+)', '', text)
    # Remove all non-alphanumeric characters except apostrophes
    text = re.sub(r"[^a-zA-Z0-9' ]+", '', text)
    # Remove usernames
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    return text.strip()

# Apply the function to the tweet text column
twitter['tweetContext'] = twitter['tweetContext'].apply(remove_special_characters)
