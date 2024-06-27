from funciones import agregar_pelic,listar_peliculas,buscar_por_categoria,guardar_y_salir,menu

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