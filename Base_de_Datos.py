class BASEDATOS:
    def __init__(self):
        self.claves={}
        
    def agregarClave(self,clave):
        self.claves[clave]=[]
        
    def agregarValor(self,posicion,valor):
        clave=list(self.claves.keys())[posicion]
        self.claves[clave].append(valor)
        
    