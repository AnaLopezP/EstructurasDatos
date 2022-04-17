import funciones

if __name__ == "__main__":
    print("Introduzca el IVA elegido en porcentaje:")
    print("Use un punto para indicar el decimal, si hay")
    iva_elegido = float(input())

    print("El precio final del producto, que sin IVA vale 100:")
    funciones.iva(iva_elegido)