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