from random import randint 

resp= " "

def lanzar_dados ():
    
    dado1=randint (1,7)
    dado2=randint (1,7)
    
    return (dado1,dado2)

def evaluar_jugada (num1,num2):
    suma_dados=num1+num2
    respuesta= " "
    if suma_dados<=6:
        respuesta="La suma de tus dados es "+ str(suma_dados)+ ". Lamentable"
        return respuesta
    if suma_dados>6 and suma_dados<10:
        respuesta="La suma de tus dados es " +str(suma_dados) + ". Tienes buenas chances"
        return respuesta
    if suma_dados >=10:
        respuesta= "La suma de tus dados es " +str(suma_dados) +". Parece una jugada ganadora"
        return respuesta


num1,num2= lanzar_dados()
resp= evaluar_jugada (num1,num2)

print(resp)