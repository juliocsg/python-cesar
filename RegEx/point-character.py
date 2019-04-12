import re

str = "hello world"

#Search for a sequence that starts with "be", followed by two(any) characters, and an "o":

x = re.findall("he..o", str)
print(x)
