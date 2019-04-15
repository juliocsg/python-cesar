import re
#Split the string at the first white-space character:

str = "The rain in Spain"
x = re.split("\s", str, 1)
print(x)
