import funciones

if __name__ == "__main__":
    print("Introduzca la primera frase:")
    frase_1 = str(input())
    print("Introduzca la segunda frase:")
    frase_2 = str(input())

    frase_1_mayus = funciones.pasar_mayus(frase_1)
    frase_2_mayus = funciones.pasar_mayus(frase_2)
    funciones.escribir(frase_1_mayus, frase_2_mayus)
