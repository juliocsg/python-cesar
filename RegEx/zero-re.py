import re
str = "The rain in Spain"
#Check if the string contains "ai" followed by 0 or more "x" character:

x = re.findall("aix*", str)

print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
