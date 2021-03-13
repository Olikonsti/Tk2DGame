from ENTITY.Tile import *
from TileSpawner import *
from Events import *

class Lava(Tile):
    def __init__(self, tx, ty, game=None, BLOCK=None):
        Tile.__init__(self, tx, ty, 50, "Lava.png")
        self.game = GlobalGame[0]
        self.name = "Lava"
        self.collider = False
        if random.choice([0, 1]) == 0:
            self.mirror_sprite()
        if BLOCK != None:
            exec("global a; a=" + BLOCK + f"({self.tileX}, {self.tileY})")
            a.collider = False


    def update(self, tick):

        if tick % 25 == 0:
            self.mirror_sprite()

        X1IsTile = False
        X2IsTile = False
        Y1IsTile = False
        for i in RenderItems:
            for j in i:
                if j.type == "TILE" and not j.waterloggable:
                    if j.tileX == self.tileX + 1 and j.tileY == self.tileY:
                        X1IsTile = True
                    elif j.tileX == self.tileX - 1 and j.tileY == self.tileY:
                        X2IsTile = True
                    elif j.tileX == self.tileX and j.tileY == self.tileY + 1:
                        Y1IsTile = True

        if Y1IsTile == False and tick % 10 == 0:
            QEvent("CreateLava", self.game, 12, lambda: Lava(self.tileX, self.tileY + 1, self.game))

        if X2IsTile == False and tick % 5 == 0:
            QEvent("CreateLava", self.game, 12, lambda: Lava(self.tileX - 1, self.tileY, self.game))

        if X1IsTile == False and tick % 5 == 0:
            QEvent("CreateLava", self.game, 12, lambda: Lava(self.tileX + 1, self.tileY, self.game))



        Tile.update(self, tick)