from random import shuffle


lista_numeros=[1,1,2,3,5,8,9]

def lanzar_moneda ():
    resultado= " "
    moneda= ["Cara","Cruz"]
    shuffle(moneda)
    resultado= moneda [0]
    return resultado



def probar_suerte (resultado,lista):
    if resultado == "Cara":
        print ("La lista se autodestruirá")
        lista.clear()
        return lista
    if resultado == "Cruz":
        print ("La lista fue salvada")
        return lista
    
print (probar_suerte(lanzar_moneda(),lista_numeros))