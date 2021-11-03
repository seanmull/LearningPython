def compress(s):
    if s == "": return ""
    compressionStr = ""
    curLetter = s[0]
    counter = 0
    for letter in s:
        if letter != curLetter:
            compressionStr += curLetter + str(counter)
            curLetter = letter
            counter = 1
        else:
            counter += 1
    return compressionStr + curLetter + str(counter)

s = 'AAAAAABBBBCCCC'

print(compress(s))