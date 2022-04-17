import funciones

if __name__ == "__main__":
    vista = funciones.vista("", "")
    vista.obtenerInput()
    print(vista.getFrase1())


    '''frase_1_mayus = funciones.pasar_mayus(funciones.vista.getFrase1())
    frase_2_mayus = funciones.pasar_mayus(funciones.vista.getFrase2())
    funciones.escribir(frase_1_mayus, frase_2_mayus)'''
