
for i in ['a', 'b', 'c']:
    try:
        print (i ** 2)
    except TypeError:
        print('TypeError: unsupported opertand types')
        break

x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print('ZeroDivision error')



