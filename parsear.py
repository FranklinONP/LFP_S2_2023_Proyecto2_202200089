#aqui como se construye el sintactico
from print import printer
from Base_de_Datos import BASEDATOS


class Parser:
    def __init__(self,tokens):
        self.tokens=tokens
        self.index=0
        self.printer=printer()
        self.db=BASEDATOS()
        
    def consume(self):
        token=self.tokens[self.index]
        self.index+=1
        return token
    
    def peek(self):
        return self.tokens[self.index]
    
    def parse(self):
        while self.index < len(self.tokens):
            var=self.peek().Nombre
            if self.peek().Nombre=='IMPRIMIR':
                self.imprimir()
            elif self.peek().Nombre=='IMPRIMIRLN':
                self.imprimirln()
            elif self.peek().Nombre=='CLAVES':
                self.claves()
            elif self.peek().Nombre=='REGISTROS':
                self.registros()
            elif self.peek().Nombre=='CONTEO':
                self.conteo()
            elif self.peek().Nombre=='CONTARSI':
                self.contarsi()
            elif self.peek().Nombre=='PROMEDIO':
                self.promedio()
            elif self.peek().Nombre=='DATOS':
                self.datos()
            elif self.peek().Nombre=='SUMAR':
                self.sumar()
            elif self.peek().Nombre=='MAX':
                self.max()
            elif self.peek().Nombre=='MIN':
                self.min()
            else:
                print('Para mientras elimino lo que no son print')
                self.consume()
        #Cauando ya termine de recorrer todo
        texto=self.printer.print()
        for linea in texto.split('\n'):
            print(linea)
    #Agregar-----> agrega sin el salto de linea 
    def imprimir(self):
        self.consume()#Me va a servir para eliminar esa palabra ---imprimir---
        if self.consume().Nombre!="PARENTESISIZQUIERDO":
            print('Error se esperaba un parentesis izquierdo')
            return
        token=self.consume()
        if token.Nombre!='STRING':
            print('Error, se esperaba un string')
            return
        if self.consume().Nombre!="PARENTESISDERECHO":
            print('Error se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!="PUNTOYCOMA":
            print('Error se esperaba un punto y coma')
            return 
        self.printer.agregar(token.Valor)
    #AgregarLinea agrega con un salto de linea
    def imprimirln(self):
        self.consume()#Me va a servir para eliminar esa palabra ---imprimirln---
        if self.consume().Nombre!="PARENTESISIZQUIERDO":
            print('Error se esperaba un parentesis izquierdo')
            return
        token=self.consume()
        if token.Nombre!='STRING':
            print('Error, se esperaba un string')
            return
        if self.consume().Nombre!="PARENTESISDERECHO":
            print('Error se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!="PUNTOYCOMA":
            print('Error se esperaba un punto y coma')
            return 
        self.printer.agregarLinea(token.Valor)
        
    def claves(self):
        self.consume()
        if self.consume().Nombre!='IGUAL':
            print('Error: Se esperaba un igual')
            return
        if self.consume().Nombre !='CORCHETEIZQUIERDO':
            print("Error: Se esperaba un corchete izquiedo")
            return
        #Agregar todas las claves que puedan haber
        if self.peek().Nombre!='STRING':
            print('Error: Se esperaba un string')
            return 
        valor1=self.consume().Valor
        self.db.agregarClave(valor1)
        while self.peek().Nombre=='COMA':
            self.consume() # Elimino la coma y paso al siguiente valor
            if self.peek().Nombre!='STRING':
                print('Error: Se esperaba un valor de Clave')
                return 
            valor1=self.consume().Valor
            self.db.agregarClave(valor1)
        if self.consume().Nombre!='CORCHETEDERECHO':
            print('Error: se esperaba un corchete derecho')
            return
  
    def registros(self):
        self.consume()#Elimina la palabra registros
        if self.consume().Nombre!='IGUAL':
            print('Error: se esperaba el simbolo igual')
            return 
        if self.consume().Nombre !='CORCHETEIZQUIERDO':
            print('Error se esperaba el corchete izquierdo')
            return
        
        while self.peek().Nombre=='LLAVEIZQUIERDA':
            self.consume()
            contador=0
            
            if self.peek().Nombre!='STRING' and self.peek().Nombre!='Numero':
                print('Error: se esperaba un valor de clave (string/numero)')
                return
            
            valor =self.consume().Valor
            self.db.agregarValor(contador,valor)
            contador+=1
            
            while self.peek().Nombre=='COMA':
                self.consume()
                if self.peek().Nombre !='STRING' and self.peek().Nombre !='Numero':
                   print('Error: se esperaba un valor de clave (string/numero)')
                   return
                valor=self.consume().Valor
                self.db.agregarValor(contador,valor)
                contador+=1
            if self.peek().Nombre!='LLAVEDERECHA':
                print('Error: se esperaba una llave derecha')
                return
            self.consume()
        self.consume()
        self.db.imprimirRegistros()
            
    def conteo(self):
        self.consume()
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Error: se esperaba un parentesis izquierdo')
            return
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Error: se esperaba un parentesis derecho')    
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Error, se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.conteo()))
        #print(self.db.conteo())                  
    
    #Falta que si no es numero me diga que es error
    def promedio(self):
        self.consume() #Elimino la palabra promedio
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Se esperaba un parentesis izquirdo')
            return
        if self.peek().Nombre!='STRING':
           print('Se esperaba una clave')
           return
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.promedio(clave)))
         
    def contarsi(self):
        self.consume() #Elimina el el token contari.si
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Error: se esperaba un parentesis izquierdo')
            return
        if self.peek().Nombre!='STRING':
            print('Error: se esperaba un string/Clave')
            return
        clave=self.consume().Valor
        if self.consume().Nombre!='COMA':
            print('Error: se esperaba una coma')
            return
        if self.peek().Nombre!='STRING' and self.peek().Nombre!='Numero':
            print('Error: se esperaba el valor de una clave')
            return
        valor=self.consume().Valor
        
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Error: se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Error, se esperaba un punto y coma')
            return
        #llego hasta qui entonces si existe
        self.printer.agregarLinea(str(self.db.contarsi(clave,valor)))     
    
    #No hace nada todavia
    def datos(self):
        pass
    
    def sumar(self):
        self.consume() #Elimino la palabra sumar
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Se esperaba un parentesis izquirdo')
            return
        if self.peek().Nombre!='STRING':
           print('Se esperaba una clave')
           return
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.sumar(clave)))
        
    def max(self):
        self.consume() #Elimino la palabra sumar
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Se esperaba un parentesis izquirdo')
            return
        if self.peek().Nombre!='STRING':
           print('Se esperaba una clave')
           return
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.maximo(clave)))   
    
    def min(self):
        self.consume() #Elimino la palabra sumar
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            print('Se esperaba un parentesis izquirdo')
            return
        if self.peek().Nombre!='STRING':
           print('Se esperaba una clave')
           return
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            print('Se esperaba un parentesis derecho')
            return
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.minimo(clave))) 