from biseccion import biseccion
from newton_raphson import newton_raphson
from riemann import riemann
from trapecio import trapecio

import math
# Funciones de validació
def pedir_funcion(funcion):
    while True:
        try:
            expresion = input(f"Ingrese la función {funcion}(x): ")
            return lambda x: eval(expresion, {"x": x, "math": math})
        except Exception:
            print("Error!. Función inválida. Ejemplo válido: x**2 - 4, math.sin(x), math.exp(-x), etc.")

def pedir_float(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error!. Debe ingresar un número válido.")

def pedir_entero(texto):
    while True:
        try:
            valor = int(input(texto))
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            print("Error!. Debe ingresar un número entero positivo.")

# Menú principal

def menu():
    while True:
        print("\n--- MÉTODOS NUMÉRICOS ---")
        print("1. Bisección")
        print("2. Newton-Raphson")
        print("3. Riemann")
        print("4. Trapecio")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            funcion = pedir_funcion("f")
            a = pedir_float("Límite inferior a: ")
            b = pedir_float("Límite superior b: ")
            resultado = biseccion(funcion, a, b)
            if resultado:
                raiz, iteraciones = resultado
                print(f" Raíz encontrada: {raiz:.6f} en {iteraciones} iteraciones.")
        elif opcion == "2":
            funcion = pedir_funcion("f")
            derivada = pedir_funcion("f'")
            x0 = pedir_float("Ingrese el valor inicial x0: ")
            resultado = newton_raphson(funcion, derivada, x0)
            if resultado:
                raiz, iteraciones = resultado
                print(f" Raíz encontrada: {raiz:.6f} en {iteraciones} iteraciones.")
        elif opcion == "3":
            funcion = pedir_funcion("f")
            a = pedir_float("Límite inferior a: ")
            b = pedir_float("Límite superior b: ")
            n = pedir_entero("Cantidad de rectángulos (n): ")
            area = riemann(funcion, a, b, n)
            print(f" Área aproximada por Riemann: {area:.6f}")
        elif opcion == "4":
            funcion = pedir_funcion("f")
            a = pedir_float("Límite inferior a: ")
            b = pedir_float("Límite superior b: ")
            n = pedir_entero("Cantidad de trapecios (n): ")
            area = trapecio(funcion, a, b, n)
            print(f" Área aproximada por Trapecio: {area:.6f}")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Error!. Opción no válida. Intente de nuevo.")

# Iniciar
if __name__ == "__main__":
    menu()