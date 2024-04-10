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
        calculadora_basica()
    elif opcion != 0:
        print("opcion desconocida")


def obtener_opcion() -> int:
    return int(input("Ingrese su opcion: "))


def saludo_personalizado() -> None:
    nombre = input("Ingrese su nombre: ")
    print(f"🤗Hola, {nombre}! Bienvenido.✨✨")

def calculadora_basica() -> None:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    operacion = int(input("Ingrese el número de la operación deseada: "))

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == 1:
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == 2:
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == 3:
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    elif operacion == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no válida.")

if __name__ == '__main__':
    __main__()
