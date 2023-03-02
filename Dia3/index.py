#Ejem. de aplicacion del metodo index

mi_texto= "Esta es una prueba"
resultado= mi_texto[0]
print(resultado)
resultado= mi_texto[9]
print(resultado)
resultado= mi_texto[-4]
print(resultado)

##############################################

resultado= mi_texto.index("n")
print(resultado)

#Buscar desde un indice determinado

resultado= mi_texto.index("a",5)
print(resultado)

#Buscar desde y hasta un indice determinado

resultado= mi_texto.index("a",5, 12)
print(resultado)

#Buscar desde y hasta un indice determinado
#en orden inverso

resultado= mi_texto.rindex("a")
print(resultado)
