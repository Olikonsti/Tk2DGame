from ENTITY.Tile import *

class Brick(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Brick.png")
        self.name = "Brick"
        self.collider = True


    def update(self, tick):
        Tile.update(self, tick)