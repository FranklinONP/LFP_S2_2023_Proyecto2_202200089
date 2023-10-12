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

@/

'''
from objetos.instrucciones import instrucciones
from objetos.registros import registros

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
    
    claveAgregada=False
    registroIniciado=False
    registroTerminado=False
    
    
    
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
            lexemas_captados.append(caracter)
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
            #si palabra es clave, otro if verifica que traiga todo sino es error sintactico
            pg+=palabra
            lexemas_captados.append(palabra)
            #print('Creo la palabra: --',palabra,'--','Fila:',num_fila,'Columna',num_col)
                
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
            if caracter!=' ':
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
            num_fila+=1
            listaErrores.append('Error Lexico')
            listaErrores.append('Error: '+str(caracter))
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
    if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z') or caracter==' ' or caracter=='_':
        return True
    else:
        return False
    
def armasTokens(lista):
    while lista:
        lexema=lista[0]
        lista.pop(0)
        if lexema=='claves':
            igual=False
            ci=False
            cc=False
            c1=False
            codigo=False
            c2=False
            coma1=False
            c3=False
            producto=False
            c4=False
            coma2=False
            c5=False
            precioC=False
            c6=False
            coma3=False
            c7=False
            precioV=False
            c8=False
            coma4=False
            c9=False
            stock=False
            c10=False
            lexema=lista[0]
            while lexema!='\n':
                if lexema=='=':
                    igual=True
                elif igual==True and lexema=='[':
                    ci=True
                elif igual==True and ci==True and lexema=='"':
                    c1=True
                elif igual==True and ci==True and c1==True and lexema =='codigo':
                    codigo=True
                elif igual==True and ci==True and c1==True and codigo==True and lexema =='"':
                    c2=True    
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and lexema==',':
                    coma1=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and lexema=='"':
                    c3=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and lexema=='producto':
                    producto=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and lexema=='"':
                    c4=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and  lexema==',':
                        
                    coma2=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and  lexema=='"':
                        c5=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and  lexema=='precio_compra':
                        precioC=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and  lexema=='"':
                        c6==True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and  lexema==',':
                        coma3==True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and  lexema=='"':
                        c7==True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and  lexema=='precio_venta':
                        precioV=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and  lexema=='"':
                        c8=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and  lexema==',':
                        coma4=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and coma4==True\
                        and  lexema=='"':
                        c9=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and coma4==True\
                        and c9==True and  lexema=='stock':
                        stock=True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and coma4==True\
                        and c9==True and stock ==True and  lexema=='"':
                        c10==True
                elif igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and coma4==True\
                        and c9==True and stock ==True and c10==True and  lexema==']':
                        cc==True
                if igual==True and ci==True and c1==True and codigo==True and c2==True and coma1==True and c3==True and producto==True and c4==True \
                    and coma2==True and c5==True and precioC==True and c6==True and c7==True and precioV==True and c8==True and coma4==True\
                        and c9==True and stock ==True and c10==True and  cc==True:
                            print('Se encontro la instruccion correcta')
                            print()
                else:
                    print('Error Sintactico'+str(lexema))
                lista.pop(0)
                lexema=lista[0]
                
                        
                        
                    
            
      
capturar_lexemas(entrada)
#armasTokens(lexemas_captados)

print('-----------------')
print(pg)
print('////////////')

for l in listaErrores:
    print(l)