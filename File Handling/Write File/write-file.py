f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
