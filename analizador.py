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
from objetos.comentario import comentario
from objetos.claves import claves 
from objetos.instrucciones import instrucciones
from objetos.registros import registros


global lexemas_captados,num_fila,num_col,pg,listaErrores,listaObjetos
pg=''
num_col=0
num_fila=0
lexemas_captados=[]
listaErrores=[]
listaObjetos=[]

def capturar_lexemas(cadena):
    global num_col
    global num_fila
    global listaErrores
    global listaErrores
    global listaObjetos
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
        
        #---------------------------------------------- NO DEBO TOCAR NADA YA FUNCIONA BIEN ------------------------------------------------------
        #Para comentarios tipo1 :D
        if caracter=='#':
            comentarioTipo1=caracter
            cadena=cadena[1:]
            while caracter!='\n':
                caracter=cadena[0]
                comentarioTipo1+=caracter
                num_col+=1
                cadena=cadena[1:]
            c=comentario(comentarioTipo1)
            listaObjetos.append(c)
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
            c=comentario(comentarioTipo2)
            listaObjetos.append(c)
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
            c=comentario(comentarioTipo3)
            listaObjetos.append(c)
            print('Comentario Tipo3: '+comentarioTipo3,'Fila: ',num_fila,"Columna: ",num_col)
        #---------------------------------------------- NO DEBO TOCAR NADA YA FUNCIONA BIEN ------------------------------------------------------
        # FIN
  
        #Meto cualquier palabras, despues hago las verificaciones
        elif esLetra(caracter):
            #Empiezo a armar la letra
            palabra=''
            while esLetra(caracter):
                palabra+=caracter.lower()
                cadena=cadena[1:]
                caracter=cadena[0]
                num_col+=1
            if palabra=='claves':
                filaAnalizar=''
                while caracter!='\n':
                    filaAnalizar+=caracter.lower()
                    cadena=cadena[1:]
                    caracter=cadena[0]
                    num_col+=1
                if verificar_clave(filaAnalizar):
                    clave=claves('claves =','[',"codigo", "producto", "precio_compra", "precio_venta", "stock",']')
                    listaObjetos.append(clave)
                    claveAgregada=True
            elif palabra =='registros' and claveAgregada==True:
                filaAnalizar=''
                while caracter!='\n':
                    filaAnalizar+=caracter.lower()
                    cadena=cadena[1:]
                    caracter=cadena[0]
                    num_col+=1
                if aperturaRegistro(filaAnalizar):
                    registroIniciado=True
        elif caracter=='{':
            filaAnalizar=''
            while caracter!='\n': #aqui esta mal porque lo esta eliminadno de una vez
                    filaAnalizar+=caracter.lower()
                    cadena=cadena[1:]
                    caracter=cadena[0]
                    num_col+=1
            if verificar_registro(filaAnalizar) and registroIniciado==True:
                #Debo encontrar la forma de extraer los valores que necesito
                cod=False
                c=''
                nprod=False
                n=''
                pco=False
                pc=''
                pve=False
                pv=''
                st=False
                s=''
                np1=True
                np2=True
                np3=True
                np4=True
                while filaAnalizar:
                    char=filaAnalizar[0]
                    if char.isdigit() and cod is False:
                        c,filaAnalizar=armarCodigo(filaAnalizar)
                        filaAnalizar=filaAnalizar[len(c):]
                        cod=True
                    elif char=='"' and cod==True:
                        filaAnalizar=filaAnalizar[1:]
                        n,filaAnalizar=formarPalabra(filaAnalizar)
                        
                        nprod=True
                    elif char.isdigit() and nprod==True and np1==True:
                        pc,filaAnalizar=armarNumero(filaAnalizar)
                        np1=False
                        pco=True
                    elif char.isdigit() and pco==True and np2==True:
                        pv,filaAnalizar=armarNumero(filaAnalizar)
                        np2=False
                        pve=True
                    elif char.isdigit() and pve==True and np3==True:
                        s,filaAnalizar=armarNumero(filaAnalizar)
                        np3=False
                        st=True
                    else:
                        filaAnalizar=filaAnalizar[1:]
                        print('Error sintactivo')
                #Agrego los atributos
                registroN=registros(c,n,pc,pv,s)
                listaObjetos.append(registroN)
            
                
                    
                    
                    
            
                    
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
                
        #Salto de linea, no es necesario agregarlo a la lista de lexemas             
        elif caracter=='\n':
            num_fila+=1
            num_col=1
            pg+=caracter
            lexemas_captados.append(caracter)
            cadena=cadena[1:]
        #Caracteres que sirven para mi cadena
        elif caracter=='=' or caracter=='[' or caracter==']' or caracter==',' or \
            caracter==';' or caracter=='(' or caracter==')' or caracter=='_' or \
            caracter==' ':
                
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
def formarPalabra(string):
    palabrita=''
    while esLetra2(string):
        palabrita+=string[0]
        string=string[1:]
    while string[0]!=',':
        print('Error entre registro')
        string=string[1:]
    string=string[1:] #elimino la coma
    return palabrita,string

def armarCodigo(cadena):
    codigo=''
    while cadena[0].isdigit():
        codigo+=cadena[0]
        cadena=cadena[1:]
    while cadena[0]!=',':
        print('Error entre registro')
        cadena=cadena[1:]
    cadena=cadena[1:] #elimino la coma
    return codigo,cadena

def armarNumero(cadena):
    numero=''
    decimal=False
    while True:
        char=cadena[0]
    #for char in cadena:
        if char.isdigit():
            numero+=char
            #num_col+=1
        elif char =='.' and not decimal:
            numero+=char
            #num_col+=1
            decimal=True
        else:
            break
        cadena=cadena[1:]
    
    while cadena[0]!=',' and cadena[0]!='}' :
        print('Error entre registro')
        cadena=cadena[1:]
    if decimal:
        numero=float(numero)
        return numero,cadena
    else:
        numero=int(numero)  
        return numero,cadena
def esLetra2(caracter):
    if ('A' <= caracter <= 'Z') or ('a' <= caracter <= 'z') or caracter==' ' or caracter=='_':
        return True
    else:
        return False
    
def verificar_clave(cadena):
    # Buscar los subgrupos entre corchetes
    codigo=False
    produ=False
    compra=False
    venta=False
    stock=False
    if '[' in cadena and '=' in cadena[:cadena.index('[')]:
        inicio = cadena.find("[")
        fin = cadena.find("]")
        if inicio != -1 and fin != -1:
            # Obtener el contenido entre corchetes
            contenido = cadena[inicio+1:fin-1]

            # Reemplazar los corchetes por comas en el contenido
            contenido = contenido.replace("[", ",").replace("]", ",")

            # Dividir los subgrupos por comas y eliminar espacios en blanco
            subgrupos = [subgrupo.strip() for subgrupo in contenido.split(",")]

            # Verificar la cantidad de subgrupos
            if len(subgrupos) == 5:
                # Verificar las palabras clave en cada subgrupo
                palabras_clave = ["codigo", "producto", "precio_compra", "precio_venta", "stock"]
                for i, subgrupo in enumerate(subgrupos):
                    # Verificar que el subgrupo esté encerrado entre comillas
                    
                    if palabras_clave[i] in subgrupo:
                        if palabras_clave[i]=='codigo':
                            codigo=True
                        elif palabras_clave[i]=='producto':
                            produ=True
                        elif palabras_clave[i]=='precio_compra':
                            compra=True
                        elif palabras_clave[i]=='precio_venta':
                            venta=True
                        elif palabras_clave[i]=='stock':
                            stock=True
        else:
            print('No se encontro corchete de cierre')
    if codigo and produ and compra and venta and stock ==True:
        #print('True')
        return True 
    else:
        #print('False')
        return False
    
def aperturaRegistro(cadena):
    indice_inicio = cadena.find('=')
    indice_fin = cadena.find('[', indice_inicio)

    if indice_inicio != -1 and indice_fin != -1:
        resultado = cadena[indice_inicio:indice_fin + 1]
        print('True desde Funcion')
        return True
    else:
        print("No se encontraron llaves de cierre.") 
        return False   

def verificar_registro(cadena):
    # Verificar si la cadena comienza y termina con llaves
    if cadena.startswith("{") and cadena.endswith("}"):
        # Eliminar las llaves del principio y del final
        cadena = cadena[1:-1]
        
        # Dividir la cadena por comas
        elementos = cadena.split(",")
        
        # Verificar la cantidad de elementos
        if len(elementos) == 5:
            # Verificar las condiciones de cada elemento
            if elementos[0].strip().isdigit() and any(caracter.isalpha() for caracter in elementos[1].strip()[1:-1]) and any(caracter.isdigit() or caracter.replace('.', '', 1).isdigit() for caracter in elementos[2].strip()) and any(caracter.isdigit() or caracter.replace('.', '', 1).isdigit() for caracter in elementos[3].strip()) and any(caracter.isdigit() for caracter in elementos[4].strip()):
                return True
    
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
print('-----------------')
print('-----------------')
for l in listaErrores:
    print(l)
print('-----------------')
print('-----------------')

for l in listaObjetos:
    if isinstance(l,comentario):
        print(l.comentario)
    else:
        print(l,'no es comentario')