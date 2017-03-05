import tokenize as tok
import tempfile
import re

input_text = input('Enter file name: ')
in_str = ''
with open(input_text, 'r') as f:
    for line in f.readlines():
        in_str = in_str + line
f.close()
remove = ',\':;\"\n'
for c in remove:
     in_str = in_str.replace(c, '')

print(re.split('([a-zA-Z0-9]*)|([.?!]*)', in_str))
