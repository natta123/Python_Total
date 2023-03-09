"""Ejer. donde la consigna es crear un programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas"""

from random import randint

nombre = input("Hola! Ingresa tu nombre: ")
print (f"Bueno {nombre}: He pensado un numero del 1 al 100 \ny tienes solo 8 intentos para adivinarlo")

numero= randint(1,100)
numero_usr= int(input("Ingresa el numero: "))
intentos= 0

while numero_usr < 1 or numero_usr > 100:
    print ("Ingrese un numero entre 1 y 100")
    numero_usr= int(input("Ingresa el numero: "))
 

while intentos < 8:
    
    if numero < numero_usr:
        print ("El numero que pensado es menor. ")
        numero_usr= int(input("Ingresa otro numero: "))
        intentos= intentos + 1
    elif numero > numero_usr:
        print ("El numero que pensado es mayor. ")
        numero_usr= int(input("Ingresa otro numero: "))
        intentos= intentos + 1
    else:
        print (f"FELICITACIONES {nombre}ADIVINASTE EL NUMERO!!! \n el numero era {numero} lo adivinaste en {intentos} intentos")
        break
else:
    print (f"Lo lamento! Se acabaron los intentos, el numero pensado era {numero}")
        

print ("G A M E   O V E R")
    
    
    