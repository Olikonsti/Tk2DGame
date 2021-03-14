from ENTITY.Tile import *

class Leaves(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "NA.png")
        self.name = "Leaves"


    def update(self, tick):

        Tile.update(self, tick)