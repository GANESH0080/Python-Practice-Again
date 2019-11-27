# The power of lambda is better shown when you use them as an anonymous function inside another function.
# function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunction(n) :
    return lambda a : a*n

strvar = myfunction(2)
print(strvar(11))