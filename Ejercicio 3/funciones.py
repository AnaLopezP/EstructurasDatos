def iva(tipo):
     if tipo == 1:
          iva = 5.5
     else:
          iva = 20
     iva = iva/100
     precio = 100 + 100*iva
     return precio