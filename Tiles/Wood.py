from ENTITY.Tile import *

class Wood(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Wood.png")
        self.name = "Wood"
        self.collider = True


    def update(self, tick):
        Tile.update(self, tick)