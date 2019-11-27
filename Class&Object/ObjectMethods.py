class myclass :
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunction(self) :
      print("Your name is :" ,self.name + " and Age is: " ,self.age)

P1 = myclass("John", 36)
P1.myfunction()