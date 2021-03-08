from ENTITY.Tile import *

class Dirt2(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Dirt2.png")
        self.name = "DIRT2"


    def update(self, tick):

        Tile.update(self, tick)