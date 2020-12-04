
opc = 0 
while opc != 4: 
    print("_________________________") 
    print("| 1.-  AGREGAR ARCHIVO  |")
    print("_________________________")
    print("| 2.- AGREGAR CANCION   |")
    print("_________________________")
    print("| 3.-   VER ARCHIVO     |")
    print("_________________________")
    print("| 4.-       BYE         |")
    print("_________________________")
    opc = int(input("Elige una: ")) 
    if opc == 1: 
        nombre = input("nombre del archivo: ") 
        archivo = open(nombre + ".txt", "a+") 

        archivo.close() 
    if opc == 2: 
        nombre = input("nombre del archivo: ") 

        archivo = open(nombre + ".txt", "a+") 

        

        cancion = input("Nombre de la cancion: ") 
        interprete = input("Nombre del interprete: ") 
        genero = input("Genero de la musica: ") 

        archivo.write("Cancion: {},    Interprete: {},     Genero: {} \n".format(cancion, interprete, genero)) 

        archivo.close() 
    if opc == 3: 
        nombre = input("nombre del archivo: ") 
        archivo = open(nombre + ".txt", "r") 
        print("________________________________________________________________") 
        print("                       Archivo: {} ".format(nombre))              
        print("________________________________________________________________") 

        lineas = archivo.readlines() 
        for lin in lineas:

            print(lin) 
        print("________________________________________________________________") 
        print() 



print("BYE") 
