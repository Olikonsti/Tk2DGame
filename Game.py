from World import *
import pygame as pg
from imageKey import KeyBind
from Events import *
from PauseMenu import *


class Game(Tk):
    def __init__(self):
        Tk.__init__(self)

        GlobalGame.append(self)

        self.fps_clock = pg.time.Clock()
        self.ticks = 0
        self.paused = False
        self.title(Title + " - " + Version)
        self.iconbitmap(TexturePath + "icon.ico")

        self.d = KeyBind("d", self, self.loop)
        self.a = KeyBind("a", self, self.loop)
        self.mlc = KeyBind("B1-Motion", self, self.loop, release="ButtonRelease-1")
        self.mrc = KeyBind("B3-Motion", self, self.loop, release="ButtonRelease-3")
        self.lc = KeyBind("Button-1", self, self.loop, release="ButtonRelease-1")
        self.rc = KeyBind("Button-3", self, self.loop, release="ButtonRelease-3")
        self.space = KeyBind("space", self, self.loop)
        self.resizable(False, False)
        self.bind("<Escape>", self.pause)
        self.geometry("1300x800")

        self.level = World(self)
        self.pauseMenu = PauseMenu(self)



        while True:
            self.fps_clock.tick(FPS)
            self.loop()

    def pause(self, event = None):
        if not self.paused:
            self.paused = True
            self.image_original = Image.open(TexturePath + "pbg.png").convert("RGBA")

            self.image = ImageTk.PhotoImage(self.image_original)
            self.level.create_image(0, 0, image=self.image)
            self.level.update()
            self.pauseMenu.show()
        else:
            self.paused = False
            self.pauseMenu.hide()

    def loop(self):
        if self.ticks % 3 == 0:
            self.update()
        else:
            self.update_idletasks()
        if not self.paused:
            self.ticks += 1
            self.level.update_world(self.ticks)
            for i in event_queue:
                i.update()

