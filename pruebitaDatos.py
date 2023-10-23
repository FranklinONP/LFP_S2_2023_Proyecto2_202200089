mi_diccionario = {
    'clave1': [1, 2, 3, 4, 5],
    'clave2': [10, 20, 30, 40, 50],
    'clave3': [100, 200, 300, 400, 500]
}

# Obtener las claves en orden original
claves = list(mi_diccionario.keys())

# Obtener los valores en orden original
valores = list(mi_diccionario.values())

# Imprimir los encabezados de columna sin espacios al inicio
encabezados = '\t'.join(clave.lstrip() for clave in claves)
print(encabezados)

# Imprimir los valores sin espacios al inicio
for i in range(len(valores[0])):
    fila = [str(valores[j][i]) for j in range(len(valores))]
    fila_str = '\t'.join(fila)
    print(fila_str)