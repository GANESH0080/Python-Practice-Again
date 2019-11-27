a = "Hello, World!"
m = "ganesh "
s = "      Hello Ganesh "

# Print the second char
print("Printing first One Character :" ,a[0])

# Print the 12th char
print("Printing 12th Character :" +a[12])

# Print the last one char
print("Printing last character :" ,a[-1])

# Print the second last
print("Printing second last Character :" ,a[-2]+m)

# Printing 2 to 2 characters from string
print(a[2:8])

print("Printing original String:", s)

# The strip() method removes any whitespace from the beginning or the end:
print(s.strip())

#The len() method returns the length of a string including the spaces
print("Length of the String is: " ,len(s))

#The lower() method returns the string in lower case:
print("String in Lowercase:" ,s.lower())

#The upper() method returns the string in upper case:
print("String in Lowercase:" ,s.upper())