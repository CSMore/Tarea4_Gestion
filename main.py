
def __main__() -> None:
    opcion = None
    while opcion != 0:
        print_menu()
        opcion = obtener_opcion()
        procesar_opcion(opcion)


def print_menu() -> None:
    print("╔═════════════════════════=╗")
    print("║         BIENVENIDO       ║")
    print("╠═════════════════════════=╣")
    print("║ 1. Saludo Personalizado  ║")
    print("║ 2. Contador de Números   ║")
    print("║ 3. Calculadora Básica    ║")
    print("║ 0. Salir                 ║")
    print("╚═════════════════════════=╝")


def procesar_opcion(opcion) -> None:
    if opcion == 1:
        saludo_personalizado()
    elif opcion == 2:
        print("contar_numeros()")
    elif opcion == 3:
        print("calculadora_basica()")
    elif opcion != 0:
        print("opcion desconocida")


def obtener_opcion() -> int:
    return int(input("Ingrese su opcion: "))


def saludo_personalizado() -> None:
    nombre = input("Ingrese su nombre: ")
    print(f"Hola, {nombre}! Bienvenido.")


if __name__ == '__main__':
    __main__()