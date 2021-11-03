def uni_char(s):
    bag = set(s)
    return len(bag) - len(s) == 0

    


s = 'abccefg'

print(uni_char(s))