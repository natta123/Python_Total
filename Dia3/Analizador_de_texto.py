"""Este ejercision consiste en crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis"""


texto= input("Ingrese el texto: ")
i1= input("Ingrese letra 1 para buscar: ").lower()
i2= input("Ingrese letra 2 para buscar: ").lower()
i3= input("Ingrese letra 2 para buscar: ").lower()

#1:
texto= texto.lower()
resultado1= texto.count(i1)
resultado2= texto.count(i2)
resultado3= texto.count(i3)
print(f"La letra {i1} aparece {resultado1} veces")
print(f"La letra {i2} aparece {resultado2} veces")
print(f"La letra {i3} aparece {resultado3} veces")

#2:
lista_texto=texto.split()
palabras= len(lista_texto)
print(f"La cantidad de palabras del texto es: {palabras}")


#3
primera = texto[0]
ultima =  texto[-1]
print(f"La primera letra es: {primera}")
print(f"La primera letra es: {ultima}")


#4:
lista_inv =lista_texto[::-1]
textoinv = " ".join(lista_inv)
print(F"Su texto invertido: \n{textoinv}")

#5:
resultado= texto.find("Python")
boolean= resultado != -1
dic={True: "Si esta",False: "No esta"}
print("La palabra Python ", dic[boolean])