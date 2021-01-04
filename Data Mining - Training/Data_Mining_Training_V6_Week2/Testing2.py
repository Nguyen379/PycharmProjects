import nltk
import random
from nltk.corpus import movie_reviews
import pickle

"Text classification"
# Movie reviews contain 2 category negative and positive each containing numerous txt files
documents = []
for category in movie_reviews.categories():
    # get the categories of movie_reviews.
    # each category has numerous fileids.txt files
    for fileid in movie_reviews.fileids(category):
        # get all the words in that fileid and add it in with the category for classification
        documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
# print(documents)

"Frequency Distribution"
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())
# get a list of all words that appear in all files
all_words2 = nltk.FreqDist(all_words)
# convert into a dictionary of frequency
word_features = list(all_words2.keys())[:3000]


# get the 3000 least common words in all words
# all_words2 keys are arranged from least to most common

# print(all_words2["stupid"])
# get a particular word


def find_features(document):
    features = {}
    words = set(document)
    for word in word_features:
        features[word] = (word in words)
        # equal to True or False
    return features


# print(find_features(movie_reviews.words("neg/cv000_29416.txt")))
# get feature words of a particular file

"Feature words"

featuresets = []
for (all_words, category) in documents:
    featuresets.append((find_features(all_words), category))
# print(featuresets)
# get the features words of each file of each category

"Training and testing with NaiveBayesClassfier"

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

classfier = nltk.NaiveBayesClassifier.train(training_set)
# print(nltk.classify.accuracy(classfier, testing_set))
# classfier.show_most_informative_features(15)

# save_classfier = open("naivebayes.pickle", "wb")
# pickle.dump(classfier, save_classfier)
# save_classfier.close()
# save file uing pickle

"Saving model with pickle"
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
# print(nltk.classify.accuracy(classifier, testing_set))
