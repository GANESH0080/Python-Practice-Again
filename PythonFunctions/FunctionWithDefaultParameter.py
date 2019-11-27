# The following example shows how to use a default parameter value.

# If we call the function without parameter, it uses the default value:

def function(fruit = "Mango") :
    print("Fruitname is :" ,fruit)
    # print("Fruitname is :" +fruit)
function("Grapes")
function("Apple")
# We will use default parameter in below function call when we not pass parameter
function()
function("Banana")