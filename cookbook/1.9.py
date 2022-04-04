a = {
   'x': 1,
   'y': 2,
   'z': 3
}

b = {
   'w': 10,
   'x': 11,
   'y': 2
}

# key views support set operations

a.keys() & b.keys()

a.keys() - b.keys()

a.items() & b.items()
