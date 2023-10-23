from collections import namedtuple 

tokenG=namedtuple("Token",['Nombre','Valor','Linea','Columna'])

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
    'exportarReporte':'EXTRAERREPORTE',
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
            print(
           'Error: caracter desconocido: {',
           caracter,
           "} en linea",
           numFila+1,
           "Columna: ",
           numCol    
            )
            #indice+=1
            cadena=cadena
            numCol+=1
    return tokensCaptados




entrada='''Claves = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]

Registros = [
    {1, "Barbacoa", 10.50, 20.00, 6}
    {2, "Salsa", 13.00, 16.00, 7}
    {3, "Mayonesa", 15.00, 18.00, 8}
    {4, "Mostaza", 14.00, 16.00, 4}
]

'''
#Para probar que recogia bien los lexemas :D
'''
l=extraerTokens(entrada)
for ll in l:
    print(ll)
    
    '''