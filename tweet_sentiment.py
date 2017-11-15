import sys
import json

#Five minutes of the the worldwide twitterstream parsed with JSON and placed in
#a Python dictionary

#Estimates the sentiment of each tweet in the stream (output.txt), based on a file
#listing sentiments associated with English language words (AFINN-111.txt).

#Run with the command:
# python tweet_sentiment.py AFINN-111.txt output.txt

path = "/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1"
afinnfile = open(sys.argv[1])
twitter_file = open(sys.argv[2])

scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

for line in twitter_file:
    if "text" in json.loads(line):
        twitter_text = json.loads(line)["text"]
        sentiment = 0
        for word in twitter_text.split():
            if word in scores:
                sentiment = sentiment + scores[word]
        print sentiment

