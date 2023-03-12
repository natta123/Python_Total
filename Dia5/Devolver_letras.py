"""Ejer. donde se implementa una funcion que recibe como parametro
una palabra y devuelve sus letras sin repetir en orden alfabetico"""

def letras_ordenadas(palabra):
    palabra=palabra.lower()
    setaux= list(set(palabra))
    setaux.sort()
    return setaux

string= "Holacomoestas"

print(letras_ordenadas(string))