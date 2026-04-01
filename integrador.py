import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

ARCHIVO = "inventario.json"

# ------------------ LÓGICA ------------------

def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return []

def guardar_datos():
    with open(ARCHIVO, "w") as f:
        json.dump(inventario, f, indent=4)

def actualizar_tree():
    for fila in tree.get_children():
        tree.delete(fila)
    for prod in inventario:
        tree.insert("", tk.END, values=(
            prod["codigo"],
            prod["descripcion"],
            prod["precio"],
            prod["categoria"],
            prod["cantidad"]
        ))

def limpiar_campos():
    entry_codigo.delete(0, tk.END)
    entry_desc.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    spin_cantidad.delete(0, tk.END)
    spin_cantidad.insert(0, "0")

def validar():
    if not entry_codigo.get() or not entry_desc.get():
        messagebox.showerror("Error", "Código y descripción obligatorios")
        return False
    try:
        float(entry_precio.get())
    except:
        messagebox.showerror("Error", "Precio inválido")
        return False
    return True

def guardar():
    if not validar():
        return
    
    nuevo = {
        "codigo": entry_codigo.get(),
        "descripcion": entry_desc.get(),
        "precio": float(entry_precio.get()),
        "categoria": entry_categoria.get(),
        "cantidad": int(spin_cantidad.get())
    }
    
    inventario.append(nuevo)
    guardar_datos()
    actualizar_tree()
    limpiar_campos()

def seleccionar(event):
    seleccionado = tree.focus()
    if seleccionado:
        valores = tree.item(seleccionado, "values")
        
        entry_codigo.delete(0, tk.END)
        entry_codigo.insert(0, valores[0])
        
        entry_desc.delete(0, tk.END)
        entry_desc.insert(0, valores[1])
        
        entry_precio.delete(0, tk.END)
        entry_precio.insert(0, valores[2])
        
        entry_categoria.delete(0, tk.END)
        entry_categoria.insert(0, valores[3])
        
        spin_cantidad.delete(0, tk.END)
        spin_cantidad.insert(0, valores[4])

def modificar():
    seleccionado = tree.focus()
    if not seleccionado:
        return
    
    if not validar():
        return
    
    valores = tree.item(seleccionado, "values")
    
    for prod in inventario:
        if prod["codigo"] == valores[0]:
            prod["descripcion"] = entry_desc.get()
            prod["precio"] = float(entry_precio.get())
            prod["categoria"] = entry_categoria.get()
            prod["cantidad"] = int(spin_cantidad.get())
            break
    
    guardar_datos()
    actualizar_tree()
    limpiar_campos()

def borrar():
    seleccionado = tree.focus()
    if not seleccionado:
        return
    
    valores = tree.item(seleccionado, "values")
    
    for prod in inventario:
        if prod["codigo"] == valores[0]:
            inventario.remove(prod)
            break
    
    guardar_datos()
    actualizar_tree()
    limpiar_campos()

# ------------------ INTERFAZ ------------------

ventana = tk.Tk()
ventana.title("Sistema de Inventario")
ventana.geometry("800x400")

inventario = cargar_datos()

# PANEL IZQUIERDO
panel_izq = ttk.LabelFrame(ventana, text="Panel de Operaciones")
panel_izq.pack(side="left", fill="y", padx=10, pady=10)

ttk.Label(panel_izq, text="Código").pack()
entry_codigo = ttk.Entry(panel_izq)
entry_codigo.pack()

ttk.Label(panel_izq, text="Descripción").pack()
entry_desc = ttk.Entry(panel_izq)
entry_desc.pack()

ttk.Label(panel_izq, text="Precio").pack()
entry_precio = ttk.Entry(panel_izq)
entry_precio.pack()

ttk.Label(panel_izq, text="Categoría").pack()
entry_categoria = ttk.Entry(panel_izq)
entry_categoria.pack()

ttk.Label(panel_izq, text="Cantidad").pack()
spin_cantidad = ttk.Spinbox(panel_izq, from_=0, to=1000)
spin_cantidad.pack()

ttk.Button(panel_izq, text="Guardar", command=guardar).pack(pady=5)
ttk.Button(panel_izq, text="Modificar", command=modificar).pack(pady=5)
ttk.Button(panel_izq, text="Borrar", command=borrar).pack(pady=5)

# PANEL DERECHO
panel_der = ttk.LabelFrame(ventana, text="Inventario")
panel_der.pack(side="right", fill="both", expand=True, padx=10, pady=10)

columnas = ("codigo", "descripcion", "precio", "categoria", "cantidad")

tree = ttk.Treeview(panel_der, columns=columnas, show="headings")

for col in columnas:
    tree.heading(col, text=col.capitalize())

tree.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(panel_der, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

tree.bind("<<TreeviewSelect>>", seleccionar)

actualizar_tree()

ventana.mainloop()