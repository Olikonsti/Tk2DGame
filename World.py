from GLOBAL import *
from tkinter import *
from ENTITY.Entity import *
from TileSpawner import *
from threading import *
import pygame as pg


class World(Canvas):
    def __init__(self, game):
        Canvas.__init__(self)
        self.game = game
        self.w = 1330
        self.h = 830
        self.tps_clock = pg.time.Clock()
        self.config(bg="#57D2F4", bd=0, highlightthickness=0, width=self.w, height=self.h)

        self.startxOff = 30
        self.startyOff = 30

        self.xOff = self.startxOff
        self.yOff = self.startyOff

        self.current_lvl = "teststage.lvl"

        self.load(self.current_lvl)

        self.place(x=-30, y=-30)

        self.backThread = Thread(target=self.backEndLoop)
        #self.backThread.start()

    def load(self, lvl):
        self.xOff = self.startxOff
        self.yOff = self.startyOff

        self.current_lvl = lvl
        SpawnTiles(lvl, self)

    def unload(self):
        clear_events()
        unloadItems()

    def backEndLoop(self):
        while True:
            self.tps_clock.tick(TPS)
            for i in RenderItems:
                for j in i:
                    j.update(self.game.ticks)

    def update_world(self, tick):
        for i in RenderItems:
            for j in i:
                j.update(self.game.ticks)
        self.draw()


    def draw(self):
        self.delete(ALL)
        for i in RenderItems:
            for j in i:
                if j.draw_type == "RECT":
                    if j.type == "TILE":
                        j.calc_pos()
                        self.create_rectangle(j.x + self.xOff, j.y + self.yOff, j.x+j.width + self.xOff, j.y+j.height + self.yOff, outline="", fill="green")
                if j.draw_type == "IMAGE":
                    if j.type == "TILE":
                        j.calc_pos()
                        self.create_image(j.x + self.xOff, j.y + self.yOff, image=j.image)
                    else:
                        self.create_image(round(j.x + self.xOff), round(j.y + self.yOff), image=j.image)
                if j.draw_type == "BACKGROUND":
                    self.create_image(j.x + self.xOff/7, j.y+self.yOff/7, image=j.image)


                if Debug:
                    try:
                        self.create_text(j.x + self.xOff, j.y + self.yOff, text=j.NBT)
                    except:
                        pass

                if DrawCollision:
                    for b in j.collisionBoxes:
                        self.create_rectangle(b.x - (b.x2 - b.x)/2 + self.xOff, b.y - (b.y2 - b.y)/2 + self.yOff, b.x2 - (b.x2 - b.x)/2 + self.xOff, b.y2 - (b.y2 - b.y)/2 + self.yOff, outline=b.color, stipple='gray50', fill=b.color)

