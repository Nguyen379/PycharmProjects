import nltk
import random
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


documents = []
category = movie_reviews.categories()

file = movie_reviews.raw(movie_reviews.fileids(category)[0])
file1 = movie_reviews.raw(movie_reviews.fileids(category)[1])
file2 = movie_reviews.raw(movie_reviews.fileids(category)[2])
file3 = movie_reviews.raw(movie_reviews.fileids(category)[3])
file4 = movie_reviews.raw(movie_reviews.fileids(category)[4])

count = CountVectorizer()
tfidf = TfidfVectorizer()
t = tfidf.fit_transform([file, file1, file2, file3, file4])
print(movie_reviews.fileids(category))
print(t)
