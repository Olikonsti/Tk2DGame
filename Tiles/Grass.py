from ENTITY.Tile import *

class Grass(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Grass.png")
        self.name = "Grass"
        self.collider = True


    def update(self, tick):
        Tile.update(self, tick)