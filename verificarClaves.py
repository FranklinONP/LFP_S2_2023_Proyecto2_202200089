def verificar_subgrupos(cadena):
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
    if codigo and produ and compra and venta and stock ==True:
        #print('True')
        return True 
    else:
        #print('False')
        return False



# Ejemplo de uso
cadena = 'claves edg34=[ @23"codigo"66, 544"producto"54, fggf"precio_compra"gg, fg"precio_venta"gf, fg"stock"gg]ff'
resultado = verificar_subgrupos(cadena)
print(resultado)

# Ejemplo de uso
cadena = '= ["codigo", "producto", "precio_compra", "precio_venta", "stock"]'
resultado = verificar_subgrupos(cadena)
print(resultado)