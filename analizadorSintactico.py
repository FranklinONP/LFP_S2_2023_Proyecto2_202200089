#aqui como se construye el sintactico
from datosConsola import printer
from Base_de_Datos import BASEDATOS
from Errores import Errores
from arbol_derivacion import *

objetoError=Errores

Palabras_Reservadas={
    'IMPRIMIR':'IMPRIMIR',
    'CLAVES':'CLAVES',
    'Registros':'REGISTROS',
    'IMPRIMIRLN':'IMPRIMIRLN',
    'conteo':'CONTEO',
    'promedio':'PROMEDIO',
    'contarsi':'CONTARSI',
    'datos':'DATOS',
    'sumar':'SUMAR',
    'max':'MAX',
    'min':'MIN',
    'exportarReporte':'EXPORTARREPORTE',
}

class Parser:
    def __init__(self,tokens,lerrores):
        self.tokens=tokens
        self.listaErrores=lerrores
        self.index=0
        self.printer=printer()
        self.db=BASEDATOS()
        self.ultimaFuncion=None
        
    def siguienteToken(self):
        if self.index>=len(self.tokens):
            token=self.tokens[self.index-1]
            return token
        else:
            token=self.tokens[self.index]
            self.index+=1
            return token
    
    def regresar(self):
        token=self.tokens[self.index]
        self.index-=1
    
    def tokenActual(self):
        if self.index>=len(self.tokens):
            return self.tokens[self.index-1]
        else:
            return self.tokens[self.index]
    
    def parse(self):
        
        raiz=arbolito.addNodo("Raiz")
        self.ultimaFuncion=raiz

        while self.index < len(self.tokens):
            var=self.tokenActual().Nombre
            if self.tokenActual().Nombre=='IMPRIMIR':
                self.imprimir()
            elif self.tokenActual().Nombre=='IMPRIMIRLN':
                self.imprimirln()
            elif self.tokenActual().Nombre=='CLAVES':
                self.claves()
            elif self.tokenActual().Nombre=='REGISTROS':
                self.registros()
            elif self.tokenActual().Nombre=='CONTEO':
                self.conteo()
            elif self.tokenActual().Nombre=='CONTARSI':
                self.contarsi()
            elif self.tokenActual().Nombre=='PROMEDIO':
                self.promedio()
            elif self.tokenActual().Nombre=='DATOS':
                self.datos()
            elif self.tokenActual().Nombre=='SUMAR':
                self.sumar()
            elif self.tokenActual().Nombre=='MAX':
                self.max()
            elif self.tokenActual().Nombre=='MIN':
                self.min()
            elif self.tokenActual().Nombre=='EXPORTARREPORTE':
                self.exportarReporte()
            else:
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                print('Para mientras elimino lo que no son print')
                self.siguienteToken()
            
            if self.index<len(self.tokens):
                self.ultimaFuncion=arbolito.addNodo("Lista de instrucciones")
                arbolito.addArista(raiz,self.ultimaFuncion)
                raiz=self.ultimaFuncion
            
            if self.index == len(self.tokens):
                reporte_html_errores(self.listaErrores)
                arbolito.graficarArbol()
                texto=self.printer.print()
                return texto
                
        #Cauando ya termine de recorrer todo
        texto=self.printer.print()
        for linea in texto.split('\n'):
            print(linea)
    #Agregar-----> agrega sin el salto de linea 
    def imprimir(self):
        self.siguienteToken()#Me va a servir para eliminar esa palabra ---imprimir---
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PARENTESISIZQUIERDO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un parentesis izquierdo')
            return
        tokenn=self.tokenActual().Nombre
        token=self.siguienteToken()
        if token.Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PARENTESISDERECHO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PUNTOYCOMA":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un punto y coma')
            return 
        self.printer.agregar(token.Valor)
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion imprimir")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("imprimir"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(token.Valor))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        
        
        
    #AgregarLinea agrega con un salto de linea
    def imprimirln(self):
        self.siguienteToken()#Me va a servir para eliminar esa palabra ---imprimirln---
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PARENTESISIZQUIERDO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un parentesis izquierdo')
            return
        tokenn=self.tokenActual().Nombre
        token=self.siguienteToken()
        if token.Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error, se esperaba un string')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PARENTESISDERECHO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!="PUNTOYCOMA":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error se esperaba un punto y coma')
            tokenn=self.tokenActual().Nombre
            return 
        self.printer.agregarLinea(token.Valor)
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion imprimirln")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("imprimirln"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(token.Valor))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        
      
    # Pendientes  
    def claves(self):
        self.siguienteToken()
        if self.siguienteToken().Nombre!='IGUAL':
            print('Error: Se esperaba un igual')
            return
        if self.siguienteToken().Nombre !='CORCHETEIZQUIERDO':
            print("Error: Se esperaba un corchete izquiedo")
            return
        #Agregar todas las claves que puedan haber
        if self.tokenActual().Nombre!='STRING':
            print('Error: Se esperaba un string')
            return 
        valor1=self.siguienteToken().Valor
        self.db.agregarClave(valor1)
        while self.tokenActual().Nombre=='COMA':
            self.siguienteToken() # Elimino la coma y paso al siguiente valor
            if self.tokenActual().Nombre!='STRING':
                print('Error: Se esperaba un valor de Clave')
                return 
            valor1=self.siguienteToken().Valor
            self.db.agregarClave(valor1)
        if self.siguienteToken().Nombre!='CORCHETEDERECHO':
            print('Error: se esperaba un corchete derecho')
            return
  
    # Pendientes
    def registros(self):
        self.siguienteToken()#Elimina la palabra registros
        if self.siguienteToken().Nombre!='IGUAL':
            print('Error: se esperaba el simbolo igual')
            return 
        if self.siguienteToken().Nombre !='CORCHETEIZQUIERDO':
            print('Error se esperaba el corchete izquierdo')
            return
        
        while self.tokenActual().Nombre=='LLAVEIZQUIERDA':
            self.siguienteToken()
            contador=0
            
            if self.tokenActual().Nombre!='STRING' and self.tokenActual().Nombre!='Numero':
                print('Error: se esperaba un valor de clave (string/numero)')
                return
            
            valor =self.siguienteToken().Valor
            self.db.agregarValor(contador,valor)
            contador+=1
            
            while self.tokenActual().Nombre=='COMA':
                self.siguienteToken()
                if self.tokenActual().Nombre !='STRING' and self.tokenActual().Nombre !='Numero':
                   print('Error: se esperaba un valor de clave (string/numero)')
                   return
                valor=self.siguienteToken().Valor
                self.db.agregarValor(contador,valor)
                contador+=1
            if self.tokenActual().Nombre!='LLAVEDERECHA':
                print('Error: se esperaba una llave derecha')
                return
            self.siguienteToken()
        self.siguienteToken()
        self.db.imprimirRegistros()
            
    def conteo(self):
        self.siguienteToken()
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba un parentesis izquierdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba un parentesis derecho')    
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error, se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.conteo()))
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion conteo")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("conteo"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        

        #print(self.db.conteo())                  
    
    #Falta que si no es numero me diga que es error
    def promedio(self):
        self.siguienteToken() #Elimino la palabra promedio
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        token=tokenn
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba una clave')
            return
        tokenn=self.tokenActual().Nombre
        clave=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.promedio(clave)))
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion promedio")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("promedio"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(token)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        

         
    def contarsi(self):
        self.siguienteToken() #Elimina el el token contari.si
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba un parentesis izquierdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba un string/Clave')
            return
        tokenn=self.tokenActual().Nombre
        clave=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='COMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba una coma')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING' and self.tokenActual().Nombre!='Numero':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba el valor de una clave')
            return
        tokenn=self.tokenActual().Nombre
        valor=self.siguienteToken().Valor
        
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error: se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Error, se esperaba un punto y coma')
            return
        #llego hasta qui entonces si existe
        self.printer.agregarLinea(str(self.db.contarsi(clave,valor))) 
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion contarsi")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("contarsi"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(clave)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(valor)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
            
    
    def datos(self):
        self.siguienteToken() #Elimino la palabra sumar
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.datos())) 
    
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion datos")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("datos"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
    
    
    def sumar(self):
        self.siguienteToken() #Elimino la palabra sumar
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba una clave')
            return
        tokenn=self.tokenActual().Nombre
        clave=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.sumar(clave)))
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion sumar")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("sumar"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(clave)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        
        
    #Con este empece para el manejo de errore sintacticos
    def max(self):
        self.siguienteToken() #Elimino la palabra sumar
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba una clave')
            return
        tokenn=self.tokenActual().Nombre
        clave=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
                print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.maximo(clave)))   
                
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion max")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("max"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(clave)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        
    
    def min(self):
        self.siguienteToken() #Elimino la palabra sumar
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba una clave')
            return
        tokenn=self.tokenActual().Nombre
        clave=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.minimo(clave))) 
        
        
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion min")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("min"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(str(clave)))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
        
    
    def exportarReporte(self):
        self.siguienteToken() #Elimino la palabra extraerReporte
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.tokenActual().Nombre
        if self.tokenActual().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba una clave')
            return
        tokenn=self.tokenActual().Nombre
        titulo=self.siguienteToken().Valor
        if self.siguienteToken().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.tokenActual().Valor,'Sintactico',self.tokenActual().Linea,self.tokenActual().Columna)
                self.listaErrores.append(error)
                self.siguienteToken()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.tokenActual().Nombre
        if self.siguienteToken().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.db.exportarReporte(titulo)
           
        raiz=arbolito.addNodo("Instruccion")
        instruccion=arbolito.addNodo("Funcion exportarReporte")
        arbolito.addArista(raiz,instruccion)
        arbolito.addArista(instruccion,arbolito.addNodo("exportarReporte"))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis izquierdo"))
        arbolito.addArista(instruccion,arbolito.addNodo(titulo))
        arbolito.addArista(instruccion,arbolito.addNodo("Parentesis derecho"))
        arbolito.addArista(instruccion,arbolito.addNodo("Punto y coma"))
        arbolito.addArista(self.ultimaFuncion,raiz)
             
        
        
def reporte_html_errores(objetos):
    html_code = '<style>\n'
    html_code += 'table {\n'
    html_code += '\tborder-collapse: collapse;\n'
    html_code += '\tmargin-left: auto;\n'
    html_code += '\tmargin-right: auto;\n'
    html_code += '}\n'
    html_code += 'th, td {\n'
    html_code += '\tpadding: 8px;\n'
    html_code += '\tborder: 1px solid black;\n'
    html_code += '}\n'
    html_code += '</style>\n'
    html_code += '\t\t<th colspan="{}">{}</th>\n'.format(4, 'Reporte de errores de Franklin Orlando Noj Perez')

    html_code += '<tr><th>Caracter/token</th><th>Tipo de error</th><th>Linea</th><th>Columna</th></tr>'
    filas = generar_filas(objetos)
    tabla_html = f'<table style="border-collapse: collapse; width: 50%; margin: auto;"><thead>{html_code}</thead><tbody>{filas}</tbody></table>'
    
    with open('Reporte de errores de Franklin Noj 202200089.html', 'w') as archivo:
        archivo.write(tabla_html)
    
def generar_filas(objetos):
    filas = ''
    for objeto in objetos:
        fila = f'<tr><td>{objeto.Caracter_token}</td><td>{objeto.tipoError}</td><td>{objeto.Linea}</td><td>{objeto.Columna}</td></tr>'
        filas += fila
    return filas
    