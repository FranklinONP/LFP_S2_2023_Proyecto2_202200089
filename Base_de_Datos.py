class BASEDATOS:
    def __init__(self):
        self.claves={}
        
    def agregarClave(self,clave):
        self.claves[clave]=[]
        
    def agregarValor(self,posicion,valor):
        clave=list(self.claves.keys())[posicion]
        self.claves[clave].append(valor)
        
    def conteo(self):
        clave=list(self.claves.keys())[0]
        return len(self.claves[clave])
    
    def promedio(self,clave):
        try:
            if clave in self.claves:
                valores = self.claves[clave]
                promedio = sum(valores) / len(valores)
                return promedio
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
        
    def contarsi(self,clave,valor):
        return self.claves[clave].count(valor)
    
    def sumar(self,clave):
        try:
            if clave in self.claves:
                valores = self.claves[clave]
                suma = sum(valores)
                return suma
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
    
    def maximo(self,clave):
        try:
            maxx = max(self.claves[clave])
            if isinstance(maxx, (int, float)):
                return maxx
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
    
    
    
    def minimo(self,clave):
        try:
            minn = min(self.claves[clave])
            if isinstance(minn, (int, float)):
                return minn
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
        
                
    def imprimirRegistros(self):
        print('_'*50)
        print('Valores')
        for clave in self.claves:
            print(clave,self.claves[clave])
            