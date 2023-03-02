texto= "Este es el texto de Nata"

resultado= texto.upper()

print(resultado)

#######################################

texto= "Este es el texto de Nata"

resultado= texto[2].upper()

print(resultado)

#######################################

texto= "Este es el texto de Nata"

resultado= texto.lower()

print(resultado)

#######################################

texto= "Este es el texto de Nata"

resultado= texto.split()

print(resultado)

#######################################
"""Separa segunn donde encuentra el
el caracter dado por parametro"""
 
texto= "Este es el texto de Nata"

resultado= texto.split("t")

print(resultado)

#######################################
"""Agrega las de una lista separadas por
la cadena donde se invoca el metodo"""

a="Aprender"
b="Phyton"
c="es"
d="genial"
e=" ".join([a,b,c,d])
print(e)

#######################################
"""A diferencia de index al no encontrar
el caracter retorna -1"""

texto= "Este es el texto de Nata"

resultado= texto.find("s")

print(resultado)

#######################################

texto= "Este es el texto de Nata"

resultado= texto.replace("Nata","todos")

print(resultado)

#######################################

texto= "Este es el texto de Nata"

resultado= texto.replace("e","X")

print(resultado)



