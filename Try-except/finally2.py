'''
try:
    f = open("demofile.txt")
    f.write("Lorem Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

    #The program can continue, without leaving the file object open
'''

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    f.close()

#The program can continue, without leaving the file object open
