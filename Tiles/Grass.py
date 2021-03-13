from ENTITY.Tile import *
from Tiles.Dirt2 import *

class Grass(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Grass.png")
        self.name = "Grass"
        self.collider = True


    def update(self, tick):
        Tile.update(self, tick)
        tileAbove = self.getTileAbove()
        if tick % 400 == 0:
            if tileAbove != None and tileAbove.collider:
                self.texture_change("NA.png")
                for i in RenderItems:
                    for j in i:
                        if j.type != "ENTITY":
                            if j.tileX == self.tileX and j.tileY == self.tileY:
                                i.remove(j)
                Dirt2(self.tileX, self.tileY)
                del self


