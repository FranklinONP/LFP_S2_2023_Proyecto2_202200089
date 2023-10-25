#aqui como se construye el sintactico
from print import printer
from Base_de_Datos import BASEDATOS
from Errores import Errores
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
        
    def consume(self):
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
    
    def peek(self):
        if self.index>=len(self.tokens):
            return self.tokens[self.index-1]
        else:
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
            elif self.peek().Nombre=='EXPORTARREPORTE':
                self.exportarReporte()
            else:
                print('Para mientras elimino lo que no son print')
                self.consume()
            if self.index == len(self.tokens):
                reporte_html_errores(self.listaErrores)
        #Cauando ya termine de recorrer todo
        texto=self.printer.print()
        for linea in texto.split('\n'):
            print(linea)
    #Agregar-----> agrega sin el salto de linea 
    def imprimir(self):
        self.consume()#Me va a servir para eliminar esa palabra ---imprimir---
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PARENTESISIZQUIERDO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un parentesis izquierdo')
            return
        tokenn=self.peek().Nombre
        token=self.consume()
        if token.Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PARENTESISDERECHO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PUNTOYCOMA":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un punto y coma')
            return 
        self.printer.agregar(token.Valor)
    #AgregarLinea agrega con un salto de linea
    def imprimirln(self):
        self.consume()#Me va a servir para eliminar esa palabra ---imprimirln---
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PARENTESISIZQUIERDO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un parentesis izquierdo')
            return
        tokenn=self.peek().Nombre
        token=self.consume()
        if token.Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error, se esperaba un string')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PARENTESISDERECHO":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!="PUNTOYCOMA":
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error se esperaba un punto y coma')
            tokenn=self.peek().Nombre
            return 
        self.printer.agregarLinea(token.Valor)
      
    # Pendientes  
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
  
    # Pendientes
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
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba un parentesis izquierdo')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba un parentesis derecho')    
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error, se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.conteo()))
        #print(self.db.conteo())                  
    
    #Falta que si no es numero me diga que es error
    def promedio(self):
        self.consume() #Elimino la palabra promedio
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba una clave')
            return
        tokenn=self.peek().Nombre
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.promedio(clave)))
         
    def contarsi(self):
        self.consume() #Elimina el el token contari.si
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba un parentesis izquierdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba un string/Clave')
            return
        tokenn=self.peek().Nombre
        clave=self.consume().Valor
        if self.consume().Nombre!='COMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba una coma')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING' and self.peek().Nombre!='Numero':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba el valor de una clave')
            return
        tokenn=self.peek().Nombre
        valor=self.consume().Valor
        
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error: se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Error, se esperaba un punto y coma')
            return
        #llego hasta qui entonces si existe
        self.printer.agregarLinea(str(self.db.contarsi(clave,valor)))     
    
    def datos(self):
        self.consume() #Elimino la palabra sumar
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.datos())) 
    
    def sumar(self):
        self.consume() #Elimino la palabra sumar
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba una clave')
            return
        tokenn=self.peek().Nombre
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.sumar(clave)))
        
        
    #Con este empece para el manejo de errore sintacticos
    def max(self):
        self.consume() #Elimino la palabra sumar
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba una clave')
            return
        tokenn=self.peek().Nombre
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
                print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.maximo(clave)))   
    
    def min(self):
        self.consume() #Elimino la palabra sumar
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba una clave')
            return
        tokenn=self.peek().Nombre
        clave=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un punto y coma')
            return
        self.printer.agregarLinea(str(self.db.minimo(clave))) 
    
    def exportarReporte(self):
        self.consume() #Elimino la palabra extraerReporte
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PARENTESISIZQUIERDO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis izquirdo')
            return
        tokenn=self.peek().Nombre
        if self.peek().Nombre!='STRING':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba una clave')
            return
        tokenn=self.peek().Nombre
        titulo=self.consume().Valor
        if self.consume().Nombre!='PARENTESISDERECHO':
            if tokenn in Palabras_Reservadas:
                self.regresar()
                self.regresar()
                error=objetoError(self.peek().Valor,'Sintactico',self.peek().Linea,self.peek().Columna)
                self.listaErrores.append(error)
                self.consume()
            print('Se esperaba un parentesis derecho')
            return
        tokenn=self.peek().Nombre
        if self.consume().Nombre!='PUNTOYCOMA':
            print('Se esperaba un punto y coma')
            return
        self.db.exportarReporte(titulo)
        
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
    