# If you have a JSON string, you can parse it by using the json.loads() method.


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# The result will be a Python dictionary.
print(y['age'])

