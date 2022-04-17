def pasar_mayus(frase1):
    frase_mayus = frase1.upper()
    print(frase_mayus)
    return frase_mayus

def escribir(frase1, frase2):
    archivo = open("archivo.txt", "w")
    archivo.write(frase1 + "\n")
    archivo.write(frase2)
    archivo.close()
    return archivo