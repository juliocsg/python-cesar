import re

str = "hello world"

#Check if the string ends with 'world'

x = re.findall("world$", str)
if (x):
    print("Yes, the string ends with 'world'")
else:
    print("No match")
