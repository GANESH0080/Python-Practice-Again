tupleitr = ("Apple","Banana","Grapes","Mango")
str = iter(tupleitr)

print(next(str))
print(next(str))
print(next(str))
print(next(str))

#Getting error "StopIteration" because no values avaialble in tuple after Mango
#print(next(str))
