
print()
example = set ()
print(example)
print()
dir(example)
print(dir(example))
print()
help(example.add)

example.add(42)
example.add(False)
example.add(98765)
example.add("add anything")

example
print(example)
print()

example.add(42)
print(example) #sets do not contains duplicate
print()

# use the length function to see the elements of a set
len(example)
print(len(example))
print()

help(example.remove)

example.remove(42)
len(example)
print(len(example))
print(example)
print()

example.remove(50) # remove an element that is not part of the set and you get an error

help(example.discard)

example.discard(50) # discard if you try to remove an element which is not in th set, the method does nothing and simply returns without making a change
