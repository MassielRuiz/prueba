diccionario_peliculas={}
def agregar_pelic():
    codigo=input("Ingrese el código de la película: ")
    nombre=input("Ingrese nombre de la pelicula: ")
    anio=input("Ingrese año de estreno de la película: ")
    categoria=input("Ingrese categoria de la película: ")
    actores=input("Ingrese el nombre de los actores (Separados por una coma ): ").split(",")
    director=input("Ingrese el director de la pelicula: ")
    
    diccionario_peliculas[codigo]={
     "nombre": nombre,
     "anio":anio,
     "categoria":categoria,
     "actores": actores,
     "director":director,
    }
     
    print("película agregada correctamente. \n")   
    
def listar_peliculas():
    if diccionario_peliculas: 
        print("listado de peliculas: ")
        for codigo, i in diccionario_peliculas.items():
            print(f"codigo       : {codigo}")
            print(f"nombre       : {i["nombre"]}")
            print(f"categoria    : {i["categoria"]}")
            print(f"actores      : {",".join(i["actores"])}")
            print(f"director     : {i["director"]}")
    else:
        print("No hay película registrada.\n")
        
def buscar_por_categoria():
    categoria_buscar = input("Ingrese la categoría de la película que desea buscar: ")
    encontrado = False
    for codigo, pelicula in diccionario_peliculas.items():
        if pelicula['categoria'].lower() == categoria_buscar.lower():
            print(f"Código    : {codigo}")
            print(f"Nombre    : {pelicula['nombre']}")
            print(f"Año       : {pelicula['anio']}")
            print(f"Categoría : {pelicula['categoria']}")
            print(f"Actores   : {', '.join(pelicula['actores'])}")
            print(f"Director  : {pelicula['director']}\n")
            encontrado = True
    if not encontrado:
        print("No se encontraron películas en esa categoría.\n")


def guardar_y_salir():
    with open("peliculas.txt", "w") as archivo:
        for codigo, pelicula in diccionario_peliculas.items():
            archivo.write(f"Código: {codigo}\n")
            archivo.write(f"Nombre: {pelicula['nombre']}\n")
            archivo.write(f"Año: {pelicula['anio']}\n")
            archivo.write(f"Categoría: {pelicula['categoria']}\n")
            archivo.write(f"Actores: {', '.join(pelicula['actores'])}\n")
            archivo.write(f"Director: {pelicula['director']}\n\n")
    print("Películas guardadas en 'peliculas.txt'. Saliendo del programa...\n")

        
def menu():
    while True:
        print("Menu:")
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película por categoría")
        print("4. Salir y guardar en archivo")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_pelic()
        elif opcion == "2":
            listar_peliculas()
        elif opcion == "3":
            buscar_por_categoria()
        elif opcion == "4":
            guardar_y_salir()
            break
        else:
            print("Opción no válida. Intente nuevamente.\n")

# Ejecutar el menú principal
menu()
