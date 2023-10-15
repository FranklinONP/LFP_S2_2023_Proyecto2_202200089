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
            if self.peek().Nombre=='IMPRIMIR':
                self.imprimir()
            elif self.peek().Nombre=='IMPRIMIRLN':
                self.imprimirln()
            #elif self.peek().Nombre=='Claves':
            #    self.claves()
            else:
                print('Para mientras elimino lo que no son print')
                self.consume()
        #Cauando ya termine de recorrer todo
        texto=self.printer.print()
        for linea in texto.split('\n'):
            print(linea)
        
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
        if self.consume.Nombre!='IGUAL':
            print('Error: Se esperaba un igual')
            return
        if self.consume().Nombre !='CORCHETE IZQUIERDO':
            print("Error: Se esperaba un corchete izquiedo")
            return
        #Agregar todas las claves que puedan haber
        if self.peek().Nombre!='STRING':
            print('Error: Se esperaba un string')
            return 
        valor1=self.consume().Valor
        self.db.agregarClave(valor1)
        while self.peek().Nombre!='COMA':
            self.consume() # Elimino la coma y paso al siguiente valor
            if self.peek().Nombre!='STRING':
                print('Error: Se esperaba un valor de Clave')
                return 
            valor1=self.consume().Valor
            self.db.agregarClave(valor1)
        if self.consume().Nombre!='CORCHETEDERECHO':
            print('Error: se esperaba un corchete derecho')
            return
        
        
        