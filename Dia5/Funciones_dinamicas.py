#Ejem. de ccomplejización del uso defunciones

def chequear_3_cifras(numero):
    return numero in range(100,1000) 

resultado = chequear_3_cifras(652)
print(resultado)

##############################################

def chequear_3_cifras(numero):
    return numero in range(100,1000) 

suma= 520 + 480

resultado = chequear_3_cifras(suma)
print(resultado)

##############################################

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    
numeros= [55,99,6000]

resultado = chequear_3_cifras(numeros)
print(resultado)

##############################################

def chequear_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

numeros= [555,99,6000]

resultado = chequear_3_cifras(numeros)
print(resultado)

##############################################

def chequear_3_cifras(lista):
    lista_3_cifras= []
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

numeros= [555,99,600]

resultado = chequear_3_cifras(numeros)
print(resultado)