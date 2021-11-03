import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but it does not have the other term.'

match = re.search(patterns[0], text)

if(match):
    print("we have a match")
else:
    print("we do not have a match")