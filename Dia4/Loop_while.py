#Ejem. de uso de loop while

monedas=5

while monedas >0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else: print("No tengo mas dinero")

#######################################

respuesta = "s"

while respuesta == "s":
    respuesta = input(" quiere seguir? s/n: ")
else : print ("Gracias")

#######################################

espuesta = "s"

while respuesta == "s":
    pass

print("Hola")

#######################################

nombre= input ("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)
    
#######################################

nombre= input ("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)