#Ejem. de uso de funcion zip

nombre = ["Ana", "Hugo", "Valeria"]
edades= [65,29,42]
ciudades= ["Lima","Madrid","Mexico"]
combinados= list(zip(nombre,edades,ciudades))
print(combinados)

##############################################

nombre = ["Ana", "Hugo", "Valeria"]
edades= [65,29,42]
ciudades= ["Lima","Madrid","Mexico"]
combinados= list(zip(nombre,edades,ciudades))
print(combinados)

for nombre, edad, ciudad, in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")