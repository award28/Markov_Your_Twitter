import tokenize as tok
import tempfile
import re

input_text = input('Enter file name: ')
in_str = ''
with open(input_text, 'r') as f:
    for line in f.readlines():
        in_str = in_str + line
f.close()
in_str = in_str.replace('-\n', '')
in_str = in_str.replace('\n', ' ')
remove = '><=+/\\][=+@#$%^&*~`,\':;\"-_'
for c in remove:
     in_str = in_str.replace(c, '')
words = list()
for w in re.split(r' |([.?!]+)', in_str):
    if w:
        words.append(w)
print(words)
table = dict()
for i, w in enumerate(words):
    if w in table and i < len(table)-1:
        print(w)
        table[w].append(words[i+1])
    else:
        if i < len(table)-1:
            table[w] = list(words[i+1])
        else:
            table[w] = list()
print(table)
