from ENTITY.Tile import *
from Events import *

class Explosive(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "NA.png")
        self.name = "Explosive"
        self.game = GlobalGame[0]
        QEvent(self, self.game, 100, self.explode)

    def explode(self):
        print("exploded")
        for i in RenderItems:
            for j in i:
                if j.type != "ENTITY" and j.name == self.name:
                    if j.tileX == self.tileX and j.tileY == self.tileY:
                        i.remove(j)
                        del j

    def update(self, tick):

        Tile.update(self, tick)