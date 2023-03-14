# Importar módulos
import tkinter as tk
from tkinter import filedialog

# Crear la ventana principal
window = tk.Tk()
window.title("Bloc de notas")

# Crear el área de texto
text_area = tk.Text(window)
text_area.pack(expand=True, fill="both")

# Crear la barra de menú
menu_bar = tk.Menu(window)

# Crear el menú archivo
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nuevo", command=lambda: text_area.delete("1.0", "end"))
file_menu.add_command(label="Abrir", command=lambda: open_file(text_area))
file_menu.add_command(label="Guardar", command=lambda: save_file(text_area))
file_menu.add_separator()
file_menu.add_command(label="Salir", command=window.quit)
menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Crear el menú editar
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cortar", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copiar", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Pegar", command=lambda: text_area.event_generate("<<Paste>>"))
menu_bar.add_cascade(label="Editar", menu=edit_menu)

# Asignar la barra de menú a la ventana
window.config(menu=menu_bar)

# Definir las funciones para abrir y guardar archivos
def open_file(text_area):
    # Pedir al usuario que seleccione un archivo para abrir
    file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        # Borrar el contenido actual del área de texto
        text_area.delete("1.0", "end")
        # Abrir el archivo y leer su contenido
        with open(file_path, "r") as file:
            text = file.read()
        # Insertar el contenido del archivo en el área de texto
        text_area.insert("1.0", text)

def save_file(text_area):
    # Pedir al usuario que seleccione un archivo para guardar o crear uno nuevo
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if file_path:
        # Obtener el contenido actual del área de texto
        text = text_area.get("1.0", "end")
        # Abrir el archivo y escribir su contenido
        with open(file_path, "w") as file:
            file.write(text)

# Iniciar el bucle principal de la ventana
window.mainloop()