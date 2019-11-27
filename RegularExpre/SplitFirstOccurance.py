import re
x = "Ganesh Mahadev Salunkhe"

# Split the string only at the first occurrence:
y = re.split("\s",x,1)

print(y)