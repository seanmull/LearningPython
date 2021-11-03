s = "The quick brown fox jumps over the lazy dog"


def ispangram(str1):
    filteredListOfChar = [char.lower() for char in str1 if char.isalpha()]
    return len(set(filteredListOfChar)) == 26

print(ispangram(s))
