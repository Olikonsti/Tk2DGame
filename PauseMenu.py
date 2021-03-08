import tkinter as tk
import tkinter.ttk as ttk
from GLOBAL import *

class Level():
    def __init__(self, name, frame):
        self.name = name
        self.menu = frame
        self.frame = tk.Frame(frame, width=200, height=30)

        self.button = ttk.Button(self.frame, text=name, command=self.load)
        self.button.pack()

        self.frame.pack()

    def load(self):
        self.frame.focus()
        self.frame.update()
        self.menu.hide()
        self.menu.game.paused = False
        self.menu.game.level.unload()

        self.menu.game.level.load(self.name)

class PauseMenu(tk.Frame):
    def __init__(self, game):
        self.game = game
        tk.Frame.__init__(self, game)
        self.config(height=500)
        self.config(width=300)
        for i in levels:
            if i.endswith(".lvl"):
                Level(i, self)


    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack(expand=True)