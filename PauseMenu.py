import tkinter as tk
import tkinter.ttk as ttk
from GLOBAL import *

class Level():
    def __init__(self, name, frame, tohide):
        self.name = name
        self.menu = frame
        self.tohide = tohide
        self.frame = tk.Frame(frame, width=200, height=30)
        self.frame.config(bg=self.tohide.bg)

        self.button = tk.Button(self.frame, text=name, command=self.load)
        self.button.config(bg=self.tohide.bg, fg=self.tohide.fg)
        self.button.pack(pady=(10,10), padx=20)

        self.frame.pack()

    def load(self):
        self.tohide.focus()
        self.tohide.update()
        self.tohide.hide()
        self.tohide.game.paused = False
        self.tohide.game.level.unload()

        self.tohide.game.level.load(self.name)

class PauseMenu(tk.Frame):
    def __init__(self, game):
        self.game = game
        self.fg = "lightgrey"
        self.bg = "#252525"
        tk.Frame.__init__(self, game)
        self.config(bg=self.bg)
        self.config(height=500)
        self.config(width=300)

        self.title = tk.Label(self, text="Paused", fg=self.fg, bg=self.bg)
        self.title.pack()

        self.levelsFrame = tk.LabelFrame(self, text="Load Maps", bg=self.bg, fg=self.fg)
        self.levelsFrame.pack()

        for i in levels:
            if i.endswith(".lvl"):
                Level(i, self.levelsFrame, self)


    def hide(self):
        self.pack_forget()

    def show(self):
        self.pack(expand=True)