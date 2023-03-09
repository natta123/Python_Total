def suma(**kwargs):
    total=0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print (suma(x=3,y=5,z=2))

######################################################

def prueba (num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")
    
    for arg in args:
        print(f"arg= {arg}")
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        
prueba (15,50,100,200,300,400,x="1",y="2",z="3")

######################################################

def prueba (num1,num2,*args,**kwargs):
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")
    
    for arg in args:
        print(f"arg= {arg}")
    
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        
args=[100,200,300,400]
kwargs={"x":"1","y":"2","z":"3"}
prueba (15,50,args,kwargs)