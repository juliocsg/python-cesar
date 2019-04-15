import re

#Replace all white-space characters with the digit "9":

str = "The rain in Spain"
#Cambia el espacio por un valor numérico
x = re.sub("\s", "9", str)

print(x)
