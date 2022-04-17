def pasar_mayus(frase1, frase2):
    frase1mayus = frase1.upper()
    frase2mayus = frase2.upper()
    return frase1mayus and frase2mayus

def escribir(frase1, frase2):
    archivo = open("/C:\Users\Usuario\Documents\GitHub\EstructurasDatos\Ejercicio 2/archivo.txt", "w")
    archivo.write(frase1 + "\n")
    archivo.write(frase2)
    archivo.close()
    return archivo