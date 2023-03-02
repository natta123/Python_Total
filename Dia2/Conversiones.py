#Conversiones implicitas

num1= 20
num2= 30
num1= num1+ num2
print(type(num1))
print(type(num2))

#Conversiones explicitas

num1= 5.8
print(num1)
print(type(num1))
num2= int(num1)
print(num2)
print(type(num2))

########################
edad=input("Ingrese su edad: ")
print(type(edad))
edad=int(edad)
nueva_edad= 1 + edad
print("tu nueva edad es: " , nueva_edad)
print(type(edad))
