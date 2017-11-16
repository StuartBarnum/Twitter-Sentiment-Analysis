import sys
import json

#Find the top ten hashtages from among the tweets in the five minutes of the twitterstream accessed in
#September of 2017

#twitter_file = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/output.txt")
twitter_file = open(sys.argv[1])  #input the twitterstream test from the command prompt

tags_count = {}

for line in twitter_file:
    if "text" in json.loads(line):
        twitter_text = json.loads(line)["text"]
        twitter_words = twitter_text.split()
        for word in twitter_words:
            if word[0] == '#':
                hash = word[1:]
                if hash not in tags_count:
                    tags_count[hash] = 1
                else:
                    tags_count[hash] += 1

#initializing the top ten
top_ten = {}
n = 0
for tag in tags_count:
    if n < 10:
        top_ten[tag] = tags_count[tag]
        n = n + 1
    if n >= 10:
        minimum = min(top_ten, key=lambda k: top_ten[k])  # equals the key with the minimum value
        if top_ten[minimum] < tags_count[tag]:
            del top_ten[minimum]                 # if minimum value is less, replace it with tag
            top_ten[tag] = tags_count[tag]

#printing in descending order
n = 0
while n < 10:
    for index in top_ten:   # for loop selects an arbitrary element of the top_ten index
        key1 = index
        break
    for key2 in top_ten:
        if top_ten.get(key2) > top_ten.get(key1):
            key1 = key2
    print key1, top_ten.get(key1)
    del top_ten[key1]
    n += 1

# RESULTS
# The top ten from my September 2017 five-minute sample, together with the number of instances:
#     izmirescort 198
#     방탄소년단 114
#     BTS 55
#     แอฟทักษอร 54
#     JIMIN 52
#     지민 41
#     bornovaescort 33
#     Lチキチーズ 32
#     EXO 32
#     เต้ยเชียร์ 32

