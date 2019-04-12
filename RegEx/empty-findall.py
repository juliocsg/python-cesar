import re

str = "The rain in Spain"

#Check if "Portugal" is in the string

x = re.findall("Portugal", str)
print(x)

if (x):
    print("Yes, there is at least one match!")
else:
    print("No match")
