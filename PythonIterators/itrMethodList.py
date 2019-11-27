Listitr = ["Apple","Banana","Grapes","Mango"]
str = iter(Listitr)


print(next(str))
print(next(str))

## next(obj) is same as obj.__next__()

#prints Grapes
print(str.__next__())

#prints Mango
print(str.__next__())
