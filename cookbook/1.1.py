x = [1, 2, 3]

# unpack based exact number of values to unpack
a, b, c = x

a
b
c

# valueeerror since not enough values
a, b, c, d = x

# valueeerror since too many values
a, b = x

# if we want the head and the rest
a, *b = x

a
b

# if we want the tail and the rest
*a, b = x

a
b
