import tokenize as tok
import tempfile
import re
import sys
import random

def train_table(table, in_str):
    in_str = in_str.replace('-\n', '')
    in_str = in_str.replace('\n', ' ')
    # remove = '><=+/\\][=+#$%^&*~`,\':;\"-_'
    # for c in remove:
    #      in_str = in_str.replace(c, '')
    words = list()
    for w in re.split(r' |([0-9]*`.[0-9]+)|([.?!]+ )', in_str):
        if w:
            words.append(w)
    for i, w in enumerate(words):
        if w in table and i < len(words)-1:
            table[w].append(words[i+1])
        else:
            if i < len(words)-1:
                table[w] = list()
                table[w].append(words[i+1])
            else:
                table[w] = list()
    return table

def read_and_train(tweets):
    lines = tweets.split('</p>\n<p>') # for peanut gal txt
    markov_table = dict()
    for l in lines:
        if l[:3] == '\'\'\'':
            print(l[:3])
            pass
        markov_table = train_table(markov_table, l)
    return markov_table

def generate_text(markov_table, length):
    key = list(markov_table.keys())[random.randint(0, len(markov_table)-1)]
    old = ''
    new = key
    while len(new) < length:
        if key == '.' or key == '?' or key == '!':
            old = new
        #print('key: ', key, ' len: ', len(markov_table[key]))
        if len(markov_table[key]) == 0:
            return new
        key = markov_table[key][random.randint(0, len(markov_table[key])-1)]
        if key == '.' or key == '?' or key == '!':
            new = new + key
        else:
            new = new + ' ' + key
    return old

f_name = sys.argv[1]
data = ''
with open(f_name, 'r') as f:
    for line in f.readlines():
        data = data + line
f.close()
markov_table = read_and_train(data[3:len(data)-5])
while(True):
    tweet = ''
    while len(tweet) < 3:
        tweet = generate_text(markov_table, 1000).replace(' . ', '. ')
    print(tweet)
    res = input('Another? ')
    if res == 'n':
        break
