class Errores:
    def __init__(self, caracter_token,tipoError, linea, columna):
        self.Caracter_token=caracter_token
        self.tipoError=tipoError
        self.Linea = linea
        self.Columna = columna