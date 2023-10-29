class printer:
    def __init__(self):
        self.text=''
        
    def agregar(self,texto):
        self.text+=texto
    
    def agregarLinea(self,texto):
        self.text+=texto+"\n"
        
    def print(self):
        return self.text