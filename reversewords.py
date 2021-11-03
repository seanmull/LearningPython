def rev_words(s):
    words = [word for word in s.split(" ") if word != ""]
    words.reverse()
    return ' '.join(words)

s = 'Hi John,    are you ready to go?'

print(rev_words(s))