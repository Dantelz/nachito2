import tkinter as tk

root = tk.Tk()
root.title("Alineación de Fútbol")
root.geometry("600x770")

# Fondo (cancha)
cancha = tk.PhotoImage(file="assets/cancha.png")
fondo = tk.Label(root, image=cancha)
fondo.place(x=0, y=0, width=600, height=770)

# Lista para evitar que se borren imágenes
jugadores_imgs = []

def crear_jugador(x, y):
    img = tk.PhotoImage(file="assets/jugador.png")
    jugadores_imgs.append(img)
    lbl = tk.Label(root, image=img, bg="green")
    lbl.place(x=x, y=y)

# Posiciones (ejemplo 4-4-2)
crear_jugador(250, 650)  # arquero

# defensores
crear_jugador(100, 550)
crear_jugador(200, 550)
crear_jugador(300, 550)
crear_jugador(400, 550)

# mediocampo
crear_jugador(100, 400)
crear_jugador(200, 400)
crear_jugador(300, 400)
crear_jugador(400, 400)

# delanteros
crear_jugador(200, 200)
crear_jugador(300, 200)

root.mainloop()