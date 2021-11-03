from functools import reduce


def word_lengths(phrase):
    return [len(word) for word in phrase.split(" ")]


s = 'How long are the words in this phrase'

print(word_lengths(s))


def digits_to_num(digits):
    index = len(digits) - 1
    num = 0
    for digit in digits:
        num += digit * pow(10, index)
        index -= 1
    return num


arr = [3, 4, 3, 2, 1]
print(digits_to_num(arr))


def filter_words(word_list, letter):
    return [word for word in word_list if word[0] == letter]


l = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']

print(filter_words(l, 'h'))


def concatenate(L1, L2, connector):
    return [item[0] + connector + item[1] for item in zip(L1, L2)]


L1 = ['A', 'B']
L2 = ['a', 'b']
connector = '-'

print(concatenate(L1, L2, connector))

text = [["Hello", "World!"], ["Lets", "Eat"]]

comp = [word for words
        in text for word in words]

print(comp)


def d_list(L):
    return {l[1]: l[0] for l in enumerate(L)}


list = ['a', 'b', 'c']
print(d_list(list))

nums = [0, 2, 2, 1, 5, 5, 6, 10]


def count_match_index(L):
    listOfNumsThatMatchIndex = \
        [n for n in enumerate(L) if n[0] == n[1]]
    return len(listOfNumsThatMatchIndex)


print(count_match_index(nums))
