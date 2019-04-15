#The finally block gets executed no matter if the try block raises any error or not

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
