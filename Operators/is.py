x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)

#returns True because z is the same object as x

print(x is y)

#returns False because x is not the same object as y,
# even if they have thew same content
print(x == y)
# to demostrate the difference between
# "is" and "==" this comparison returns
# True because x is equal to y
