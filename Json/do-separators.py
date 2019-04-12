import json

x = {
    "name" : "John",
    "age"  : 30,
    "married" : True,
    "divorced" : False,
    "children" : ("Ann", "Billy"),
    "pets" : None,
    "cars" : [
        {"model":"BMW 230", "mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
    ]
}
#use . and a space to separate objects, and a space, and a space, a = and a space
#to separate keys from their values:
#cambia la coma del json a . y el dos puntos a es igual en este caso
print(json.dumps(x, indent = 4, separators=(". ", " = ")))
