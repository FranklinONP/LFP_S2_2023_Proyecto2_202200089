cadena = 'dsgd=dfs [jkjkjk'
indice_inicio = cadena.find('=')
indice_fin = cadena.find('[', indice_inicio)

if indice_inicio != -1 and indice_fin != -1:
    resultado = cadena[indice_inicio:indice_fin + 1]
    print('True')
else:
    print("No se encontraron llaves de cierre.")
print('oooooooooooooooooooooooooooo')

def aperturaRegistro(cadena):
    indice_inicio = cadena.find('=')
    indice_fin = cadena.find('[', indice_inicio)

    if indice_inicio != -1 and indice_fin != -1:
        resultado = cadena[indice_inicio:indice_fin + 1]
        print('True desde Funcion')
    else:
        print("No se encontraron llaves de cierre.") 
aperturaRegistro('Hola=[')       