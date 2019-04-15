import re

str = "8 times before 11:45 AM"

#Check if the string has any + charaters:

x = re.findall("[%]", str)

print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
