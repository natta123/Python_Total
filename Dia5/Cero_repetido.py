"""Ejer. donde se implementa una funcion que retorna true
si encuentra un "0" repetido 2 veces en una cantidad no definida
de argumentos."""

def cero_repetido(*args):
    aux=0
    for arg in args:
        if arg==0:
            aux= aux+1
    if aux >= 2:
        return True
    else:
        return False



print(cero_repetido(1,2,3,4))
        