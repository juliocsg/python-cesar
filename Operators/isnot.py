x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x

print(x is not y)
#returns True because x is not the same object as y, even if
#they have the same content
print(x <> y)
#to demostrate the difference between "is not" and
#"<>" this comparison returns false because
#x is equal to y
