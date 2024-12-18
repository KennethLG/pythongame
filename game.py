import tkinter as tk

from config import HEIGHT, WIDTH
from player import Player


class Game:
    def __init__(self):
        self.create_window()
        self.create_canvas()
        self.init_instances()
        self.set_buttons()
        self.game_loop()

    def init_instances(self):
        self.instances = []
        self.instances.append(Player())

    def update_instances(self):
        for instance in self.instances:
            instance.update()

    def create_window(self):
        self.window = tk.Tk()
        self.window.title("Game")

    def create_canvas(self):
        self.canvas = tk.Canvas(self.window, width=WIDTH, height=HEIGHT)
        self.canvas.pack()

    def set_buttons(self):
        self.window.bind("<KeyPress>", self.key_pressed)
        self.window.bind("<KeyRelease>", self.key_released)

    def key_pressed(self, event):
        for instance in self.instances:
            instance.handle_event("keyPressed", event)

    def key_released(self, event):
        for instance in self.instances:
            instance.handle_event("keyReleased", event)

    def draw_instances(self):
        for instance in self.instances:
            instance.draw(self.canvas)

    def redraw(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="black")
        self.draw_instances()

    def game_loop(self):
        self.update_instances()
        self.redraw()
        self.window.after(int(1000 / 60), self.game_loop)

    def start(self):
        self.window.mainloop()
