from ENTITY.Tile import *

class Dirt(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Dirt.png")
        self.name = "DIRT"


    def update(self, tick):

        Tile.update(self, tick)