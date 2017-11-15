import sys
import json

#Based on the five minutes of Twitter data, make the best guess as to the happiest US state.

#The state abreviations:
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


path = "/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1"

#afinnfile = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/AFINN-111.txt")
#twitter_file = open("/Users/stuartbarnum/Desktop/Coursera/datasci_course_materials/assignment1/output.txt")

afinnfile = open(sys.argv[1])  #load  term sentiment calibration file (AFINN-111.txt) from command prompt
twitter_file = open(sys.argv[2])  #input raw twitter data from command prompt

#"Happiest state" based on the sentiments of tweets appearing to originate in the respective states.
#The twitterstream is parsed with JSON and placed in a Python dictionary (with "place" indicating apparent
#location and "text" indicating the US state).

scores = {} # initialize an empty dictionary
for line in afinnfile:
    term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
    scores[term] = int(score)  # Convert the score to an integer.

states_sentiment = {}

for line in twitter_file:
    if "text" in json.loads(line):
        twitter_text = json.loads(line)["text"]
        sentiment = 0
        for word in twitter_text.split():
            if word in scores:
                sentiment = sentiment + scores[word]
    if 'place' in json.loads(line) and json.loads(line)['place'] != None:
        for state in states:
            if state in json.loads(line)['place']['full_name'].split():
                if state not in states_sentiment:
                    states_sentiment[state] = [sentiment, 1]
                else:
                    states_sentiment[state][0] += sentiment
                    states_sentiment[state][1] += 1

result = ['x', 0]
for state in states_sentiment:
    r = states_sentiment[state][0] / states_sentiment[state][1]
    if r > result[1]:
        result = [state, r]

print result[0]


