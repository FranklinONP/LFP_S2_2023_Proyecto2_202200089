entrada='''#COMENTARIO
"""    
COMENTARIO MULTILINEA 

 """
'.'.'   
 COMENTARIO MULTILINEA 
 
'.'.'

claves = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]

Registros = [
    {1, "Barbacoa", 10.50, 20.00, 6}
    {2, "Salsa", 13.00, 16.00, 7}
    {3, "Mayonesa", 15.00, 18.00, 8}
    {4, "Mostaza", 14.00, 16.00, 4}
]


imprimir("Reporte de ");
imprimir("Abarroteria");
imprimirln("Reporte de ");
imprimirln("Abarroteria");

datos();
conteo();
    promedio("producto");
contarsi("stock", 0);
    sumar("stock");
    max("precio_venta");
    min("precio_compra");
exportarReporte("Reporte HTML de abarroteria");

'''

global lexemas_captados,num_fila,num_col,pg,listaErrores
pg=''
num_col=0
num_fila=0
lexemas_captados=[]
listaErrores=[]

def capturar_lexemas(cadena):
    global num_col
    global num_fila
    global listaErrores
    global listaErrores
    global pg
    
    num_col=1
    num_fila=1
    indice=0
    pg=''
    nError=0
    while cadena:
        
        caracter=cadena[0]
        
        #Para comentarios tipo1 :D
        if caracter=='#':
            comentarioTipo1=caracter
            cadena=cadena[1:]
            while caracter!='\n':
                caracter=cadena[0]
                comentarioTipo1+=caracter
                num_col+=1
                cadena=cadena[1:]
            print('Comentario Tipo1: '+comentarioTipo1,'Fila: ',num_fila,"Columna: ",num_col)
            num_fila+=1
            num_col=1  
        #Para comentarios tipo2 :D
        elif cadena[:3]=='"""':
            cadena=cadena[3:] 
            num_col+=3
            comentarioTipo2=''
            while cadena[:3]!='"""':
                caracter=cadena[0]
                comentarioTipo2+=caracter
                if caracter=='\n':
                    num_fila+=1
                    num_col=1
                num_col+=1
                cadena=cadena[1:]
            cadena=cadena[3:]
            num_col+=2
            print('Comentario Tipo2: '+comentarioTipo2,'Fila: ',num_fila,"Columna: ",num_col)
        #Para comentarios tipo3 :D
        elif cadena[:5]=="'.'.'":
            cadena=cadena[5:] 
            num_col+=5
            comentarioTipo3=''
            while cadena[:5]!="'.'.'":
                caracter=cadena[0]
                comentarioTipo3+=caracter
                if caracter=='\n':
                    num_fila+=1
                    num_col=1
                num_col+=1
                cadena=cadena[1:]
            cadena=cadena[5:]
            num_col+=4
            print('Comentario Tipo3: '+comentarioTipo3,'Fila: ',num_fila,"Columna: ",num_col)

        #Salto de linea, no es necesario agregarlo a la lista de lexemas
        elif caracter=='\n':
            num_fila+=1
            num_col=1
            pg+=caracter
            cadena=cadena[1:]
            
            
        #Meto cualquier palabras, despues hago las verificaciones
        elif esLetra(caracter):
            #Empiezo a armar la letra
            palabra=''
            while esLetra(caracter):
                palabra+=caracter.lower()
                cadena=cadena[1:]
                caracter=cadena[0]
                num_col+=1
            pg+=palabra
            lexemas_captados.append(palabra)
            print('Creo la palabra: --',palabra,'--','Fila:',num_fila,'Columna',num_col)
                
        #Palabras con espacion entre ellas
        elif caracter=='"':
            num_col+=1
            pg+=caracter
            
            cadena=cadena[1:]
            caracter=cadena[0]
            palabraCompuesta=''
            while esLetra2(caracter):
                palabraCompuesta+=caracter
                cadena=cadena[1:]
                caracter=cadena[0]
                num_col+=1
            if len(palabraCompuesta)>3:
                pg+=palabraCompuesta
                lexemas_captados.append(palabraCompuesta) 
        #Caracteres que sirven para mi cadena
        elif caracter=='=' or caracter=='[' or caracter==']' or caracter==',' or \
            caracter==';' or caracter=='(' or caracter==')' or caracter=='_' or \
            caracter=='{' or caracter=='}'or caracter==' ':
            pg+=caracter
            lexemas_captados.append(caracter)
            cadena=cadena[1:]
            num_col+=1
        
        #Para formar los numeros
        elif caracter.isdigit():
            decimal=False
            numero=''
            iteraciones=0
            for char in cadena:
                if char.isdigit():
                    numero+=char
                    num_col+=1
                    iteraciones+=1
                elif char =='.' and not decimal:
                    numero+=char
                    num_col+=1
                    iteraciones+=1
                    decimal=True
                else:
                    break
            if decimal:
                numero=float(numero)
            else:
                numero=int(numero)
            cadena=cadena[iteraciones:]
            lexemas_captados.append(numero)
            pg+=str(numero)      
        else:
            cadena=cadena[1:]
            
'''
def existeRegistro(cadena):
    posicion=0
    codigo=''
    while cadena[posicion].isdigit() or esLetra(posicion[0]):
        codigo+=cadena
        if cadena[0+1].isdigit() or esLetra(cadena[0+1]):
            posicion+1       
        else:
            posicion+1
            break
    while cadena[posicion]!=',':
        posicion+=1
        #Primer coma
        if cadena[posicion]==',':
            posicion+=1
            # Inicializa un contador para contar las comillas
            contador_comillas = 0

            # Inicializa una bandera para verificar si estamos dentro de una expresión entre comillas
            dentro_de_comillas = False
'''                        
                            
    
        
def esLetra(caracter):
    if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z'):
        return True
    else:
        return False
def esLetra2(caracter):
    if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z') or caracter==' ':
        return True
    else:
        return False
    
def extraerLexemas(lista):
    while lista:
        pass
      
capturar_lexemas(entrada)

print('-----------------')
print(pg)