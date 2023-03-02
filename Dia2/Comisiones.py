#Calcula la comision de venta de un empleado (13% de lo vendido)

vendedor = input("Ingrese su nombre: ")
venta= input("Ingrese su venta total: ")
venta= float(venta)
comision= round(venta*0.13,2)
print(f"Felicitaciones {vendedor} tu comision es: {comision}")