#Ejer. donde se implementa el codigo para  jugar al ahorcado

from random import choice

lista=["arreglo","tiburon","camarada"]
palbra_elegida= " "
intento= []
numero_de_intento=0

def elegir_palabra(lista_palabras,intento):
    palabra= choice(lista_palabras)
    for n in palabra:
        intento.append(" _ ")
    return palabra,intento

def verificar_letra(letra,palabra,intento):
    palabra=list(palabra)
    intento=list(intento)
    for index, item in enumerate(palabra):
            if letra == item:
                intento[index]= letra              
    return intento
    
def mostrar (intento):
    texto=" "
    for index, item in enumerate(intento):
        texto= texto + item
    return texto


palbra_elegida, intento= elegir_palabra (lista,intento)
print("Bienvenido al ahorcado!")
print("Tu palabra es: ")
print(mostrar(intento))
letra = input ("Ingrese una letra: ")
comparar= list(palbra_elegida)


while not (letra.isalpha()) or numero_de_intento < 5: 
    intento_anterior=intento
    letra.lower()
    intento = verificar_letra(letra,palbra_elegida,intento)
    print("********************")
    print(mostrar(intento))
    print ("Te quedan ", 5 -numero_de_intento, "intentos")
    print("********************")
    if  intento_anterior==intento:
        numero_de_intento+= 1
    elif comparar == intento:
        break
    letra = input ("Ingrese una letra: ")

if comparar == intento:
    print("Ganaste!")
elif comparar != intento:
    print(f"Perdistee la palabra elegida era: {palbra_elegida}")
    
    

