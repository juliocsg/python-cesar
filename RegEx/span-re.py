import re

#Search for an upper case "S" character in a begining
# of a word, and print its position:

str = "The rain in Spain"
x = re.search("\b5\w+", str)
print(x.span())

