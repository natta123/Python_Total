#Ejem. de uso de argumentos indefinidos *args

def suma (*args):
    total=0
    for arg in args:
        total+=arg
    return total


print(suma(5,6,6,7))

################################################

def suma (*args):
   
    return sum(args)


print(suma(5,6,6,7,12,34,5,2))