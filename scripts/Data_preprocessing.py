from nltk.util import ngrams

def tokenize(text):
    ngram = ngrams(text.split(),2)
    return  [" ".join(gram) for gram in ngram]
