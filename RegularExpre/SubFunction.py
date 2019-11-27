import re

str = "The rain in Spain"

# Replace every white-space character with the number 9:
x = re.sub("\s", "9", str)
print(x)