# n-gram: sequece of n words
# Bow (Bag of words): turn into a dictionary with the keys are the words and the values are the words' frequencies
# bow has no order and grammar. Because the highest frequency words are often meaningless like "the", "a", we can
# weight a term by the inverse of document frequency, or Tf-idf (term frequency - inverse document frequency)
# tf = số lân 1 từ xuất hiện, idf = log((tổng số văn bản)/(số văn bản xuất hiện từ đang xét ở tf)), tf-idf = tf x idf
# idf có tác dụng lọc những từ thông dụng quá mức Sử dụng log trong idf để "dampen" ảnh hưởng khi số văn bản quá lớn.

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

"Separate into sentences, words"
text = '''Hi Mr. Smith, how are you doing today? The weather is great and Python is awesome.'''
print(sent_tokenize(text))
print(word_tokenize(text))
# catch "." in "Mr." is part of a word not a punctuation

"Using stopwords"
sw = stopwords.words("english")
# print(sw)
filtered_sent = [n for n in word_tokenize(text) if n not in sw]
print(filtered_sent)

"Stemming"
ps = PorterStemmer()
words = ["program", "programs", "programer", "programing", "programers"]
for w in words:
    print(w, " : ", ps.stem(w))
