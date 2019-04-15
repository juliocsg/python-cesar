import re

#The string property returns the search string:

str = "The rain in Spain"
x = re.search(r"\b5\w+", str)
print(x)
