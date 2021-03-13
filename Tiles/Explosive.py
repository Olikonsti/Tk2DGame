from ENTITY.Tile import *

class Explosive(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "NA.png")
        self.name = "Explosive"
        self.game = GlobalGame[0]


    def update(self, tick):

        Tile.update(self, tick)