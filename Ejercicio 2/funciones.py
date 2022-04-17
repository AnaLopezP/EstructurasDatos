class vista:
    def __init__(self,frase1, frase2):
        self.frase1 = frase1
        self.frase2 = frase2

    def obtenerInput(self):
        print("Introduzca la primera frase:")
        self.setFrase1(str(input()))
        print("Introduzca la segunda frase:")
        self.setFrase2(str(input()))
    
    def getFrase1(self):
        return self.frase1
    def getFrase2(self):
        return self.frase2
    def setFrase1(self, frase1):
        self.frase1 = frase1
    def setFrase2(self, frase2):
        self.frase2 = frase2
        


class controlador:
    def __init__(self):
        pass
    def pasar_mayus(self, frase):
        frase_mayus = frase.upper()
        return frase_mayus

class DAO:
    def __init__(self):
        pass
    def escribir(self, archivo, frase, modo):
        archivo = open(archivo, modo)
        archivo.write(frase + "\n")
        archivo.close()

    def leer(self, archivo):
        archivo = open(archivo, "r")
        cadena = archivo.read()
        archivo.close()
        return cadena