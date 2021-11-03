def gencubes(n):
    for num in range(n):
        yield num**3

# for x in gencubes(10):
#     print(x)

#  That means when they are called in your
#   code the don't actually return a value 
#   and then exit, the generator functions 
#   will automatically suspend and resume 
#   their execution and state around the 
#   last point of value generation. The 
#   main advantage here is that instead 
#   of having to compute an entire series
#    of values upfront and the generator 
#    functions can be suspended, this 
#    feature is known as state suspension.

g = gencubes(3) #convert function to generator
g
print (next(g))
print (next(g))
print (next(g))

s = 'hello'

# for let in s:
#     print(let)

s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))

# def genfibon(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a+b

# for num in genfibon(10):
#     print(num)