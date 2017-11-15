from __future__ import division

import sys
import json

#Calculate the term frequency histogram of the livestream Twitter data (over five minutes , in Septermber 2017)
#For each term, the result is equal to the number of occurrences of the term in all tweets divided by the
#number of occurences of all of the terms in all of the tweets.

twitter_file = open(sys.argv[1])  #imports the raw twitterstream data

#twitter_file = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/output.txt")

term_frequency = {}   # initializes the dictionary that will contain the raw frequecy for each word
all_word_total = 0

for line in twitter_file:
    if "text" in json.loads(line):
        twitter_text = json.loads(line)["text"]
        for word in twitter_text.split():
            if word not in term_frequency:
                term_frequency[word] = 1
            if word in term_frequency:
                term_frequency[word] += 1
        all_word_total += len(twitter_text.split())

for word in term_frequency:
    print word, term_frequency[word] / all_word_total
