#Ejem. de aplicacion de estructura de control Match

serie= "n-02"

match serie:
    case "n-01":
        print("Samsung")
    case "n-02":
        print("Nokia")
    case "n-03":
        print("Moto")
    case _:
        print("No existe producto")
        
###################################################

cliente= {"nombre": "Nata", "edad": 30, "ocupacion": "estudiante"}
pelicula= {"titulo": "matrixk", "ficha_tecnica":{"protagonista":"keanu reeves","director":"Lana y lilly wachowski" }}
elemento= [cliente,pelicula,"libro"]

for e in elemento:
    match e:
        case{ "nombre": nombre,
              "edad": edad,
              "ocupacion": ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {"titulo": titulo,
              "ficha_tecnica": {"protagonista": protagonista,
                                "director": director}}:
            print("esto es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("no se que esto")  