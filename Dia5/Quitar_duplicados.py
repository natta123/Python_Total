lista_numeros = [1,2,2,3,4,5,5,6,7,7,8,8]

def reducir_lista(lista_numeros):
    lista= list(set(lista_numeros))
    return lista
def promedio(lista):
    valor_medio = sum(lista)/len(lista)
    return valor_medio


print(reducir_lista(lista_numeros))