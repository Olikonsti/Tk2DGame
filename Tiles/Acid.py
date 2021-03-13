from ENTITY.Tile import *
from TileSpawner import *
from Events import *

class Acid(Tile):
    def __init__(self, tx, ty, game=None):
        Tile.__init__(self, tx, ty, 50, "Acid.png")
        self.game = GlobalGame[0]
        self.name = "Acid"
        self.collider = False
        if random.choice([0, 1]) == 0:
            self.mirror_sprite()

    def createNext(self, tx, ty):
        self.killblock(tx, ty)
        Acid(tx, ty, self.game)

    def update(self, tick):
        X1IsTile = False
        X2IsTile = False
        Y1IsTile = False
        Y2IsTile = False
        for i in RenderItems:
            for j in i:
                if j.name == "Acid":
                    if j.tileX == self.tileX + 1 and j.tileY == self.tileY:
                        X1IsTile = True
                    if j.tileX == self.tileX - 1 and j.tileY == self.tileY:
                        X2IsTile = True
                    if j.tileX == self.tileX and j.tileY == self.tileY + 1:
                        Y1IsTile = True

        if not Y1IsTile and tick % 5 == 0:
            QEvent("CreateAcid", self.game, 2, lambda: self.createNext(self.tileX, self.tileY + 1))

        if not X2IsTile and tick % 5 == 0:
            QEvent("CreateAcid", self.game, 2, lambda: self.createNext(self.tileX - 1, self.tileY))

        if not X1IsTile and tick % 5 == 0:
            QEvent("CreateAcid", self.game, 2, lambda: self.createNext(self.tileX + 1, self.tileY))





        Tile.update(self, tick)