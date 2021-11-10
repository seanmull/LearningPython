st = "Print only the words that start with the letter s in this sentence"
# for num in filter(lambda s: s[0] == 's', st.split(" ")):
#     print(num)

# for num in [num for num in range(0,11) if num % 2 == 0]:
#     print(num)

# for num in [num for num in range(1,51) if num % 3 == 0]:
#     print(num)

st = "Print every word in this sentence that has a even number of letter"
# for s in filter(lambda s: len(s) % 2 == 0, st.split(" ")):
#     print(f"{s} is even!")

# for id, num in enumerate(range(1,101)):
#     if(num % 3 == 0 and num % 5 == 0):
#         print(id + 1 ," Fizzbuzz")
#     elif(num % 3 == 0):
#         print(id + 1, " Fizz")
#     elif(num % 5 == 0):
#         print(id + 1, " Buzz")

st = "Create a list of the first letters of every word in the string"

list = [word[0] for word in st.split(" ")]
print(list)
