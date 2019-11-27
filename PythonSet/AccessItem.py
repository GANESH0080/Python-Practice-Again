thisset = {"apple", "banana", "cherry"}
print(thisset)

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# print(thisset[1])

for x in thisset :
    print(x)

# Check if "banana" is present in the set:
print("banana" in thisset)