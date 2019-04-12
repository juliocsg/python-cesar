import re

str = "hello world"

x = re.findall("^hello", str)

if (x):
    print("Yes, the string start 'hello'")
else:
    print("No match")
