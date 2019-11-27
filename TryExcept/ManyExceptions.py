try :
    print(x)
except NameError:
    print("An exception occurred")
except :
    print("An exception occurred")