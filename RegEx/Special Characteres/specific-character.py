import re

str = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", str)

print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
