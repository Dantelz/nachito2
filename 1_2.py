from tkinter import *
from PIL import Image, ImageTk

t = Tk()
t.title("Alineación táctica")
t.geometry("600x770")
t.resizable(False, False)

imagenes = []
jugadores = {}

img = Image.open("assets/cancha.png").resize((600, 770))
cancha_img = ImageTk.PhotoImage(img)
imagenes.append(cancha_img)

canvas = Canvas(t, width=600, height=770)
canvas.pack()

canvas.create_image(0, 0, anchor=NW, image=cancha_img)

def hacer_movible(item):
    def iniciar_mov(event):
        canvas.tag_raise(item)
        jugadores[item]["start_x"] = event.x
        jugadores[item]["start_y"] = event.y

    def mover(event):
        dx = event.x - jugadores[item]["start_x"]
        dy = event.y - jugadores[item]["start_y"]
        canvas.move(item, dx, dy)
        jugadores[item]["start_x"] = event.x
        jugadores[item]["start_y"] = event.y

    def soltar(event):
        x, y = canvas.coords(item)

        centro_x = x + 50
        centro_y = y + 53

        for otro in jugadores:
            if otro != item:
                ox, oy = jugadores[otro]["pos"]

                otro_centro_x = ox + 50
                otro_centro_y = oy + 53

                distancia = ((centro_x - otro_centro_x)**2 + (centro_y - otro_centro_y)**2) ** 0.5

                if distancia < 80:
                    jugadores[item]["pos"], jugadores[otro]["pos"] = (
                        jugadores[otro]["pos"],
                        jugadores[item]["pos"]
                    )

                    canvas.coords(item, *jugadores[item]["pos"])
                    canvas.coords(otro, *jugadores[otro]["pos"])
                    return

        canvas.coords(item, *jugadores[item]["pos"])

    canvas.tag_bind(item, "<Button-1>", iniciar_mov)
    canvas.tag_bind(item, "<B1-Motion>", mover)
    canvas.tag_bind(item, "<ButtonRelease-1>", soltar)

def cargar_jugador(ruta, x, y):
    img = Image.open(ruta).convert("RGBA").resize((100, 106))
    img_tk = ImageTk.PhotoImage(img)
    imagenes.append(img_tk)

    item = canvas.create_image(x, y, image=img_tk, anchor=NW)

    jugadores[item] = {
        "pos": (x, y),
        "start_x": 0,
        "start_y": 0
    }

    hacer_movible(item)


cargar_jugador("assets/jugador1.png", 250, 575)

cargar_jugador("assets/jugador2.png", 80, 450)
cargar_jugador("assets/jugador3.png", 200, 450)
cargar_jugador("assets/jugador4.png", 320, 450)
cargar_jugador("assets/jugador5.png", 440, 450)

cargar_jugador("assets/jugador6.png", 180, 325)
cargar_jugador("assets/jugador7.png", 320, 325)

cargar_jugador("assets/jugador8.png", 80, 200)
cargar_jugador("assets/jugador9.png", 250, 200)
cargar_jugador("assets/jugador10.png", 420, 200)

cargar_jugador("assets/jugador11.png", 250, 50)

t.mainloop()