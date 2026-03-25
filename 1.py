import tkinter as tk
from tkinter import ttk
import math

def click(valor):
    actual = pantalla.get()
    pantalla.set(actual + str(valor))

def limpiar():
    pantalla.set("")

def borrar():
    pantalla.set(pantalla.get()[:-1])

def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.set(str(resultado))
    except:
        pantalla.set("error")

def raiz():
    try:
        valor = float(pantalla.get())
        pantalla.set(str(math.sqrt(valor)))
    except:
        pantalla.set("error")

def cuadrado():
    try:
        valor = float(pantalla.get())
        pantalla.set(str(valor**2))
    except:
        pantalla.set("error")

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")
root.resizable(False, False)

pantalla = tk.StringVar()

frame_pantalla = tk.Frame(root, bg="white", height=100)
frame_pantalla.pack(fill="both")

label = tk.Label(frame_pantalla, textvariable=pantalla, anchor="e", bg="white", fg="black", font=("Segoe UI", 28))
label.pack(expand=True, fill="both", padx=10, pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack(expand=True, fill="both")

botones = [
    ["%", "CE", "C", "⌫"],
    ["1/x", "x2", "√", "÷"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["+/-", "0", ".", "="]
]

for i, fila in enumerate(botones):
    for j, texto in enumerate(fila):
        if texto == "=":
            comando = calcular
        elif texto == "C" or texto == "CE":
            comando = limpiar
        elif texto == "⌫":
            comando = borrar
        elif texto == "√":
            comando = raiz
        elif texto == "x2":
            comando = cuadrado
        else:
            comando = lambda t=texto: click(t.replace("÷", "/").replace("x", "*"))

        b = tk.Button(frame_botones, text=texto, font=("Segoe UI", 14), command=comando)
        b.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)

for i in range(6):
    frame_botones.rowconfigure(i, weight=1)

for j in range(4):
    frame_botones.columnconfigure(j, weight=1)

root.mainloop()