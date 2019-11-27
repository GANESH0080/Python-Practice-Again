# The issuperset() method returns True if all items in the specified set exists in the original set,
# otherwise it retuns False.


x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)