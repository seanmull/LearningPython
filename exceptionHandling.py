try:
    f = open('testfile', 'r')
    f.write('Test write this')
except IOError:
    print("You can cannot write to file")
finally:
    print("Alway execute this")

