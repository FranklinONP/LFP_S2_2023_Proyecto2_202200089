import tkinter as tk

def abrir():
    # Lógica para el botón "Abrir"
    pass

def analizar():
    # Lógica para el botón "Analizar"
    texto = "Texto que quieres mostrar después de presionar 'Analizar'"
    cuadro_texto2.delete('1.0', tk.END)  # Borrar el contenido actual del cuadro de texto
    cuadro_texto2.insert(tk.END, texto)  # Insertar el nuevo texto

def reportes():
    # Lógica para el botón "Reportes"
    pass
# Crear una ventana

root = tk.Tk()
root.title("Proyecto 2 ----202200089")

# Creamos los botones en la parte superior
frame_superior = tk.Frame(root)
frame_superior.pack()

btn_abrir = tk.Button(frame_superior, text="Abrir", command=abrir)
btn_abrir.pack(side=tk.LEFT, padx=10)

btn_analizar = tk.Button(frame_superior, text="Analizar", command=analizar)
btn_analizar.pack(side=tk.LEFT, padx=10)

btn_reportes = tk.Button(frame_superior, text="Reportes", command=reportes)
btn_reportes.pack(side=tk.LEFT, padx=10)

# Creamos el cuadro de texto en la parte inferior izquierda
cuadro_texto = tk.Text(root, width=50, height=20)  # Establecer ancho y alto fijo
cuadro_texto.pack(side=tk.LEFT)

# Creamos el cuadro de texto en la parte inferior derecha
cuadro_texto2 = tk.Text(root, width=50, height=20, state=tk.DISABLED)  # Establecer ancho y alto fijo y deshabilitar la edición
cuadro_texto2.pack(side=tk.RIGHT)

root.mainloop()