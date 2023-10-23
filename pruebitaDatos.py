import html

mi_diccionario = {
    'clave1': [1, 2, 3, 4, 5],
    'clave2': [10, 20, 30, 40, 50],
    'clave3': [100, 200, 300, 400, 500]
}

# Obtener las claves en orden original
claves = list(mi_diccionario.keys())

# Obtener los valores en orden original
valores = list(mi_diccionario.values())

titulo='Reporte de Franklin'
# Generar el código HTML de la tabla
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


html_code += '<table>\n'
html_code += '\t<tr>\n'
html_code += '\t\t<th colspan="{}">{}</th>\n'.format(len(claves), titulo)
html_code += '\t</tr>\n'

html_code += '\t<tr>\n'
html_code += '\t\t<th>{}</th>\n'.format('</th>\n\t\t<th>'.join(claves))
html_code += '\t</tr>\n'

for i in range(len(valores[0])):
    html_code += '\t<tr>\n'
    fila = [html.escape(str(valores[j][i])) for j in range(len(valores))]
    html_code += '\t\t<td>{}</td>\n'.format('</td>\n\t\t<td>'.join(fila))
    html_code += '\t</tr>\n'

html_code += '</table>'

# Guardar el código HTML en un archivo
with open('tabla.html', 'w') as file:
    file.write(html_code)