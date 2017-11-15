from __future__ import division
import sys
import json

path = "/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1"

#afinnfile = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/AFINN-111.txt")
#twitter_file = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/output.txt")

afinnfile = open(sys.argv[1])
twitter_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary for the given scores
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited.
    scores[term] = int(score)  # Convert the score to an integer.

new_scores = {}  # initialize an empty dictionary for the calculated scores

#Parse the five minutes of the twitterstream (in September of 2017) with JSON.

#Calculate the sentiments of the each tweet using the given list, and then form a dictionary in which the each "word"
#score is assigned a list: [sum of sentiments, number of tweets that contain the word]. Output the ratio of the
# first element of the list to the second.

tweet_scores = {}  #initiazing the dictionary of tweet scores

for line in twitter_file:
    if "text" in json.loads(line):
        twitter_text = json.loads(line)["text"]
        sentiment = 0
        for word in twitter_text.split():
            if word in scores:
                sentiment = sentiment + scores[word]

        for word in twitter_text.split():
            if word not in scores:
                if word not in new_scores:
                    new_scores[word] = [sentiment, 1]
                if word in new_scores:
                    new_scores[word][0] += sentiment
                    new_scores[word][1] += 1

for word in new_scores:
    print word, new_scores[word][0] / new_scores[word][1]



