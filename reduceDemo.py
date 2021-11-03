from functools import reduce
#http://www.python-course.eu/images/reduce_diagram.png

l = [47, 11, 42, 13]

print(reduce(lambda x,y : x+y, l))

print(reduce(lambda x,y : x if (x > y) else y , l ))