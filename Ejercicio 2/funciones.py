def pasar_mayus(frase1, frase2):
    frase1mayus = frase1.upper()
    print(frase1mayus)
    frase2mayus = frase2.upper()
    print(frase2mayus)
    return frase1mayus and frase2mayus

def escribir(frase1, frase2):
    archivo = open("archivo.txt", "w")
    archivo.write(frase1 + "\n")
    archivo.write(frase2)
    archivo.close()
    return archivo