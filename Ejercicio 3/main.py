import funciones

if __name__ == "__main__":
    print("Introduzca el tipo de producto: 1 --> alimentario, 2 --> servicio")
    respuesta = int(input())
    precio_final = funciones.iva(respuesta)
    print("El precio final del producto, que sin IVA vale 100: " + str(precio_final))
