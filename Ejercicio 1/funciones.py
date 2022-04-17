class Bloque:
    def __init__(self):
        self.instrucciones = []

    def agregarInstruccion(self, instruccion):
        self.instrucciones.append(instruccion)

class Si:
    def __init__(self, condicion, entonces, si_no):
        self.condicion = condicion
        self.entonces = entonces
        self.si_no = si_no

    def verificacion(self):
        if self.condicion:
            Mostrar(self.entonces).mnsj()
        else:
            Mostrar(self.si_no).mnsj()

class MientrasQue:
    def __init__(self, condicion, bloque):
        self.condicion = condicion
        self.bloque = bloque
        while self.condicion:
            Mostrar(self.bloque).mnsj()

class Mostrar:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def mnsj(self):
        print(self.mensaje)


def visitante():
    ok = Mostrar("OK")
    ko = Mostrar("KO")
    opcion1 = 2 + 2 == 4
    opcion2 = 2 + 2 == 22

    op1 = Si(opcion1, ok.mensaje, ko.mensaje)
    op1.verificacion()

    op2 = Si(opcion2, ok.mensaje, ko.mensaje)
    op2.verificacion()

    bloque_opcion = Bloque()
    bloque_opcion.agregarInstruccion(op1)
    bloque_opcion.agregarInstruccion(op2)
    mientras = MientrasQue(True, bloque_opcion)
    print(bloque_opcion.instrucciones)
