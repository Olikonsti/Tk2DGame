from tkinter import *
from ENTITY.Entity import *
from TileSpawner import *


class World(Canvas):
    def __init__(self, game):
        Canvas.__init__(self)
        self.game = game
        self.w = 1330
        self.h = 830
        self.config(bg="lightblue", bd=0, highlightthickness=0, width=self.w, height=self.h)

        self.startxOff = 30
        self.startyOff = 30

        self.xOff = self.startxOff
        self.yOff = self.startyOff

        self.load("teststage.lvl")

        self.place(x=-30, y=-30)

    def load(self, lvl):
        self.xOff = self.startxOff
        self.yOff = self.startyOff


        SpawnTiles(lvl, self)

    def unload(self):
        clear_events()
        unloadItems()

    def update_world(self, tick):
        for i in RenderItems:
            for j in i:
                j.update(tick)
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

                if Debug:
                    try:
                        self.create_text(j.x + self.xOff, j.y + self.yOff, text=j.NBT)
                    except:
                        pass

                if DrawCollision:
                    for b in j.collisionBoxes:
                        self.create_rectangle(b.x - (b.x2 - b.x)/2 + self.xOff, b.y - (b.y2 - b.y)/2 + self.yOff, b.x2 - (b.x2 - b.x)/2 + self.xOff, b.y2 - (b.y2 - b.y)/2 + self.yOff, outline=b.color, stipple='gray50', fill=b.color)
