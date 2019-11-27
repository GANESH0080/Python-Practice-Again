thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)
# The index() method finds the first occurrence of the specified value.
print(x)

# The index() method raises an exception if the value is not found
x = thistuple.index(88)