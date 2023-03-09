#Ejem. de uso de funciones

precios_cafe= [("capuchino",1.5),("expresso",1.2),("moka",1.9)]

for elemento in precios_cafe:
    print(elemento)


################################################################

for cafe,precio in precios_cafe:
    print(cafe)

################################################################

def cafe_mas_caro (lista_precios):
    precio_mayor= 0
    cafe_caro= ""
    
    for cafee,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor= precio
            cafe_caro= cafee
        else:
            pass
    return (cafe_caro,precio_mayor)        

cafe,precio= cafe_mas_caro(precios_cafe)
print(f"El cafe mas coro es {cafe} y el precio es {precio}")