from nltk.util import ngrams
import nltk
from nltk.corpus import stopwords

def tokenize(text):
    # Generates bi-gram tuples using the NLTK library's ngrams function
    # Input: tweet and the size of the n-grams
    ngram = ngrams(text.split(),2)
    # Joins the bi-grams into strings and returns them as a list
    return  [" ".join(gram) for gram in ngram]

def remove_stop_words(tokens):
    # Creates a set of stop words for the English language using the 'stopwords' module
    stop_words = set(stopwords.words('english'))
    # Create a new list of tokens that do not appear in the set of stop words using list comprehension
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Return the filtered tokens list
    return filtered_tokens
