from modelos import Libro


def menu():
    while(True):
        print("=================================")
        print("      GESTIÓN DE BIBLIOTECA")
        print("=================================")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Buscar libro")
        print("4. Listar libros")
        print("5. Realizar préstamo")
        print("6. Registrar devolución")
        print("7. Mostrar préstamos activos")
        print("8. Mostrar préstamos de un usuario")
        print("9. Guardar datos")
        print("0. Salir")
        opcionMenu= input("\nSelecciona una opción: ")

        match opcionMenu:
            case "1":
                print("")



def main():
    menu()




if __name__ == '__main__':
    main()