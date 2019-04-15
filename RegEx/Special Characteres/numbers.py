import re

str = "The rain in Spain"

x = re.findall("[123]", str)
print(x)

if (x):
    print("Yes, there is at least one match")
else:
    print("No match")
