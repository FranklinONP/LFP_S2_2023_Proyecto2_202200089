from tokenGen import TokenO
tokenG=TokenO

from Errores import Errores
objetoError=Errores

numFila=1
numCol=1

#Lado derecho es la llave, y el lado izquierdo es el contenido.
Palabras_Reservadas={
    'imprimir':'IMPRIMIR',
    'Claves':'CLAVES',
    'Registros':'REGISTROS',
    'imprimirln':'IMPRIMIRLN',
    'conteo':'CONTEO',
    'promedio':'PROMEDIO',
    'contarsi':'CONTARSI',
    'datos':'DATOS',
    'sumar':'SUMAR',
    'max':'MAX',
    'min':'MIN',
    'exportarReporte':'EXPORTARREPORTE',
    '(':'PARENTESISIZQUIERDO',
    ')':'PARENTESISDERECHO',
    '{':'LLAVEIZQUIERDA',
    '}':'LLAVEDERECHA',
    '[':'CORCHETEIZQUIERDO',
    ']':'CORCHETEDERECHO',
    ',':'COMA',
    ':':'DOSPUNTOS',
    ';':'PUNTOYCOMA',
    "'''":'COMENTARIOM_MULTILINEA',
    '#':'COMENTARIO',
    '"""':'COMENTARIO_MULTILINEA2',
    '=':'IGUAL'
}


def armarPalabra(cadena,indice):
    palabra=''
    for caracter in cadena:
        if caracter=='"':
            return [palabra,indice]
        palabra+=caracter
        indice+=1
    print('Error, string no encerrado')


def armarNumero(cadena,indice):
    numero=''
    decimal=False
    for caracter in cadena:
        if caracter.isdigit():
            numero+=caracter
            indice+=1
        elif caracter=='.' and not decimal:
            numero+=caracter
            indice+=1
            decimal=True
        else:
            break
    if decimal:
        return [float(numero),indice]
    else:
        return [int(numero), indice]

def extraerTokens(cadena):
    global numCol,numFila
    tokensCaptados=[]
    arregloErrores=[]
    indice=0
    while cadena:
        caracter=cadena[0]
        if caracter==' ':
            numCol+=1
            #indice+=1
            cadena=cadena[1:]
        elif caracter=='\n':
            numCol=1
            numFila+=1
            #indice+=1
            cadena=cadena[1:]
        elif caracter=='\t':
                numCol+=4 
                #indice+=4
                cadena=cadena[4:]   
        elif caracter=='#': #Para comentario de una linea
            ii=1
            while indice<len(cadena) and cadena[0]!='\n':
                ii+=1
                cadena=cadena[1:]
            numCol=1
            numFila+=1
            cadena=cadena[1:]
        #No estoy Seguro================================================================================================
        
        elif caracter=='"' and cadena[indice+1]=='"' and cadena[indice+2]=='"':
            #indice+=3
            cadena=cadena[3:]
            caracter=cadena[0]
            while True:
                if caracter=='"' and cadena[indice+1]=='"' and cadena[indice+2]=='"':
                    break
                if caracter=='\n':
                    numCol=1
                    numFila+=1
                    cadena=cadena[1:]
                    caracter=cadena[0]
                indice+=1
                numCol+=1
                cadena=cadena[3:]
                caracter=cadena[0]
            #indice+=1
        elif caracter=="'" and cadena[1]=="'" and cadena[2]=="'":
            #indice+=3
            cadena=cadena[3:]
            caracter=cadena[0]
            while True:
                if caracter=="'" and cadena[1]=="'" and cadena[2]=="'":
                    break
                if caracter=='\n':
                    numCol=1
                    numFila+=1
                    cadena=cadena[1:]
                indice+=1
                numCol+=1
                cadena=cadena[1:]
                caracter=cadena[0]
            cadena=cadena[3:]
            #indice+=1
        #No estoy Seguro================================================================================================
        elif caracter=='"':
            cadena=cadena[1:]
            string,pos=armarPalabra(cadena,0)
            numCol+=len(string)+1
            #indice+=pos+2                 
            cadena=cadena[pos+1:]
            token=tokenG('STRING',string,numFila,numCol)
            tokensCaptados.append(token)
        elif caracter.isalpha():# Para cuando sea letra o numero, esto sera para las isnstrucciones, las funcionalidades
            #aux=indice
            aux=0
            while aux<len(cadena) and cadena[aux].isalpha():
                aux+=1
            palabrita=cadena[0:aux]
            if palabrita in Palabras_Reservadas:
                numCol+=len(palabrita)
                token=tokenG(Palabras_Reservadas[palabrita],palabrita,numFila,numCol)
                tokensCaptados.append(token)
            else:
                numCol+=len(palabrita)
                error=objetoError(palabrita,'Lexico',numFila,numCol)
                arregloErrores.append(error)
                print("Error sintactico: ",palabrita)
            cadena=cadena[len(palabrita):]
        elif caracter.isdigit():
            numerito,pos=armarNumero(cadena[indice:],0)
            numCol+=pos+1                               #duda///////////////////////////////////////
            #indice+=pos
            cadena=cadena[pos:]
            token=tokenG("Numero",numerito,numFila,numCol)
            tokensCaptados.append(token)
            
        elif caracter in Palabras_Reservadas: # Para los simbolos como, [],{},: etc, que son admitidos
            numCol+=1
            token=tokenG(Palabras_Reservadas[caracter],caracter,numFila,numCol)
            tokensCaptados.append(token)
            #indice+=1
            cadena=cadena[1:]
        else:
            error=objetoError(caracter,'Lexico',numFila,numCol)
            arregloErrores.append(error)
            #indice+=1
            cadena=cadena[1:]
            numCol+=1
        if not cadena:
            reporteTokensAnalizados(tokensCaptados) 
    return tokensCaptados, arregloErrores

def reporteTokensAnalizados(objetos):
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
    html_code += '\t\t<th colspan="{}">{}</th>\n'.format(4, 'Reporte de tokens de Franklin Orlando Noj Perez')

    html_code += '<tr><th>Nombre</th><th>Valor</th><th>Linea</th><th>Columna</th></tr>'
    filas = generar_filas(objetos)
    tabla_html = f'<table style="border-collapse: collapse; width: 50%; margin: auto;"><thead>{html_code}</thead><tbody>{filas}</tbody></table>'
    
    with open('Reporte de token Franklin Noj 202200089.html', 'w') as archivo:
        archivo.write(tabla_html)
    
def generar_filas(objetos):
    filas = ''
    for objeto in objetos:
        fila = f'<tr><td>{objeto.Nombre}</td><td>{objeto.Valor}</td><td>{objeto.Linea}</td><td>{objeto.Columna}</td></tr>'
        filas += fila
    return filas
    