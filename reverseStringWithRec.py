def reverseStringWithRec(s):
    if s == "": return ""
    return s[-1] + reverseStringWithRec(s[:-1])

s = 'Hello'
print(reverseStringWithRec(s))
# print(s[:-1])