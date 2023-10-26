class printer:
    def __init__(self):
        self.text=''
        self.primeraLinea=True
        
    def agregar(self,texto):
        self.text+=texto
    
    def agregarLinea(self,texto):
        if "\n" not in texto and self.primeraLinea==True:
            self.text+=texto
            self.primeraLinea=False
        else:
            self.text+='\n'+texto
        
    def print(self):
        return self.text