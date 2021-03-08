from ENTITY.Tile import *

class Chest(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Chest.png")
        self.name = "Chest"
        self.collider = False


    def update(self, tick):
        Tile.update(self, tick)