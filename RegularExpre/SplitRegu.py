import re
x = "Ganesh Mahadev Salunkhe"

# The split() function returns a list where the string has been split at each match:
y = re.split("\s",x)

print(y)