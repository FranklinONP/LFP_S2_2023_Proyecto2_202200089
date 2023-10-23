import html
class BASEDATOS:
    def __init__(self):
        self.claves={}
        
    def agregarClave(self,clave):
        self.claves[clave]=[]
        
    def agregarValor(self,posicion,valor):
        clave=list(self.claves.keys())[posicion]
        self.claves[clave].append(valor)
        
    def conteo(self):
        clave=list(self.claves.keys())[0]
        return len(self.claves[clave])
    
    def promedio(self,clave):
        try:
            if clave in self.claves:
                valores = self.claves[clave]
                promedio = sum(valores) / len(valores)
                return promedio
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
        
    def contarsi(self,clave,valor):
        return self.claves[clave].count(valor)
    
    def datos(self):
        claves=list(self.claves.keys())
        valores=list(self.claves.values())
        encabezados = '\t'.join(clave.lstrip() for clave in claves)
        # Imprimir los encabezados de columna sin espacios al inicio
        encabezados = '\t'.join(clave.lstrip() for clave in claves)
        datosSTR=encabezados+'\n'
        # Imprimir los valores sin espacios al inicio
        for i in range(len(valores[0])):
            fila = [str(valores[j][i]) for j in range(len(valores))]
            fila_str = '\t'.join(fila)+'\n'
            datosSTR+=fila_str
        return datosSTR


    def sumar(self,clave):
        try:
            if clave in self.claves:
                valores = self.claves[clave]
                suma = sum(valores)
                return suma
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
    
    def maximo(self,clave):
        try:
            maxx = max(self.claves[clave])
            if isinstance(maxx, (int, float)):
                return maxx
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
    
    
    
    def minimo(self,clave):
        try:
            minn = min(self.claves[clave])
            if isinstance(minn, (int, float)):
                return minn
            else:
                return False
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            return False
        
    def exportarReporte(self,title):
        # Obtener las claves en orden original
        claves = list(self.claves.keys())

        # Obtener los valores en orden original
        valores = list(self.claves.values())

        titulo=title
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
        with open('Reporte Franklin Noj.html', 'w') as file:
            file.write(html_code)
        
                
    def imprimirRegistros(self):
        print('_'*50)
        print('Valores')
        for clave in self.claves:
            print(clave,self.claves[clave])
            