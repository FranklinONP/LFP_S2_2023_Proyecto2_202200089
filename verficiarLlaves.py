cadena = '{1, 33"Barbac6}dsfs}'
cadena = '{1, 33"Barbac6}dsfs}'
indice_inicio = cadena.find('{')
indice_fin = cadena.find('}', indice_inicio)

if indice_inicio != -1 and indice_fin != -1:
    resultado = cadena[indice_inicio:indice_fin + 1]
    print(resultado)
else:
    print("No se encontraron llaves de cierre.")