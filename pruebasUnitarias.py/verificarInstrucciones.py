def instrucciones(cadena):
    indice_inicio = cadena.find('();')

    if indice_inicio != -1:
        primer_parentesis = cadena[indice_inicio:indice_inicio + 3]  # Tomamos los 3 caracteres de '();'
        print("Se encontró '();':", primer_parentesis)
    else:
        print("No se encontró '();' en la cadena.")
        
instrucciones('Algo = (); y algo más')

print('========================================')

def instruccionClave(cadena):
    if cadena.find('("producto");') != -1 or cadena.find('("precio_compra");') != -1 \
        or cadena.find('("precio_venta");') != -1 or cadena.count('("stock");') != -1:
        print('True')
    else:
        print('False')
 
 
instruccionClave('dfsa("producto");')       