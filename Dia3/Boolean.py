#Ejem de usos de datos booleanos

var1=True
var2=False
print(type(var1))
print(var1)

##################################

numero= 5 > 2+3
print(type(numero))
print(numero)

##################################

numero= 5 == 2+3
print(type(numero))
print(numero)

##################################

numero= 5 != 2+3
print(type(numero))
print(numero)

##################################

numero= bool(5<6)
print(type(numero))
print(numero)

##################################

lista=[1,2,3,4]
control= 5 in lista
print(type(control))
print(control)

##################################

lista=[1,2,3,4]
control= 5 not in lista
print(type(control))
print(control)