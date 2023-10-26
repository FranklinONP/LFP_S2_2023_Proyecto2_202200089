import tkinter as tk
from tkinter import font
from tkinter import ttk
import webbrowser
from tkinter import filedialog

# Importo los analizadores
from analizadorLexico import extraerTokens
from analizadorSintactico import Parser

global textoEditor
textoEditor=''

def abrir():
    file_path = filedialog.askopenfilename(filetypes=[("Archivos bizdata", "*.bizdata"),("Archivos de texto", "*.txt"), ("Archivos HTML", "*.html")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                cuadro_texto.delete("1.0", tk.END)  # Borrar el contenido existente en el cuadro de texto
                cuadro_texto.insert(tk.END, content)  # Insertar el contenido del archivo en el cuadro de texto
        except FileNotFoundError:
            print(f"Archivo no encontrado: {file_path}")

def analizar():
    # Lógica para el botón "Analizar"
    global textoEditor
    textoEditor= cuadro_texto.get("1.0", tk.END)
    
    tokens,listaErrores=extraerTokens(textoEditor)
    
    parser=Parser(tokens,listaErrores)
    texto2=parser.parse()
    cuadro_texto2.configure(state=tk.NORMAL)  # Habilitar el cuadro de texto temporalmente
    cuadro_texto2.delete('1.0', tk.END)  # Borrar el contenido actual del cuadro de texto
    cuadro_texto2.insert(tk.END, texto2)  # Insertar el nuevo texto
    cuadro_texto2.configure(state=tk.DISABLED)  # Volver a deshabilitar el cuadro de texto
    
def reportes():
    # Lógica para el botón "Reportes"
    pass

def opcion1():
    file_path = "Reporte de errores de Franklin Noj 202200089.html" 
    webbrowser.open(file_path)

def opcion2():
    file_path = "Reporte de token Franklin Noj 202200089.html"  
    webbrowser.open(file_path)

def opcion3():
    print("Opción 3")
# Crear una ventana

root = tk.Tk()
root.title("Proyecto 2 ||| Lenguajes Formales y de Programacion ||| Franklin Noj 202200089")

# Establecer el tamaño de la ventana
root.geometry("1200x600")  # Anchura x Altura

# Establecer el color de fondo de la ventana
root.configure(bg="gray")
# Creamos los botones en la parte superior
frame_superior = tk.Frame(root)
frame_superior.pack()

button_font = font.Font(family="Arial", size=24, weight="bold", slant="italic")
btn_abrir = tk.Button(frame_superior, text="Abrir", command=abrir,borderwidth=1, relief="ridge", bg="orange", activebackground="yellow", font=button_font)
btn_abrir.pack(side=tk.LEFT, padx=3)

btn_analizar = tk.Button(frame_superior, text="Analizar", command=analizar,borderwidth=1, relief="ridge", bg="orange", activebackground="yellow", font=button_font)
btn_analizar.pack(side=tk.LEFT, padx=3)


# Crear el botón "Reportes"
style = ttk.Style()
style.configure("TMenubutton", background="orange", foreground="black",borderwidth=1 ,font=("Arial", 24, "bold"))
btn_reportes = ttk.Menubutton(frame_superior, text="Reportes",style="TMenubutton")
btn_reportes.pack(side=tk.LEFT, padx=1)

# Crear el menú desplegable para Reportes
reportes_menu = tk.Menu(btn_reportes, tearoff=False)

# Estilo para los subbotones del menú
style.configure("TMenubutton.TButton", background="orange", foreground="black", borderwidth=1, font=("Arial", 12, "bold"))

# Agregar las opciones al menú desplegable
reportes_menu.add_command(label="Reporte de Errores", command=opcion1)
reportes_menu.add_command(label="Reporte de Tokens", command=opcion2)
reportes_menu.add_command(label="Arbol de derivacion", command=opcion3)

# Aplicar el estilo a los subbotones en el menú desplegable
for item in reportes_menu.winfo_children():
    btn_widget = reportes_menu.entrycget(item, "command")
    style.configure(btn_widget, **style.configure("TMenubutton.TButton"))


# Configurar el menú desplegable en el botón "Reportes"
btn_reportes["menu"] = reportes_menu

# Creamos el cuadro de texto en la parte inferior izquierda
cuadro_texto = tk.Text(root, width=75, height=30)  # Establecer ancho y alto fijo
cuadro_texto.pack(side=tk.LEFT)
# Establecer el color del borde y el grosor
cuadro_texto.configure(highlightbackground="black", highlightthickness=3)

# Creamos el cuadro de texto en la parte inferior derecha
cuadro_texto2 = tk.Text(root, width=75, height=30, state=tk.DISABLED)  # Establecer ancho y alto fijo y deshabilitar la edición
cuadro_texto2.pack(side=tk.RIGHT)
# Establecer el color del borde y el grosor
cuadro_texto2.configure(highlightbackground="black", highlightthickness=3)

root.mainloop()