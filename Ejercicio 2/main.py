import funciones

if __name__ == "__main__":
    vista = funciones.vista("", "")
    vista.obtenerInput()

    controlador = funciones.controlador()
    cadena = vista.getFrase1()
    frase_1_mayus = controlador.pasar_mayus(cadena)
    frase_2_mayus = controlador.pasar_mayus(vista.getFrase2())

    dao = funciones.DAO()
    dao.escribir("archivo.txt", frase_1_mayus, "w")
    dao.escribir("archivo.txt", frase_2_mayus, "a")
    print(dao.leer("archivo.txt"))
    
