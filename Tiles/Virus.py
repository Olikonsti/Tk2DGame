from ENTITY.Tile import *
from TileSpawner import *
from Events import *

class Virus(Tile):
    def __init__(self, tx, ty, game=None):
        Tile.__init__(self, tx, ty, 50, "Virus.png")
        self.game = GlobalGame[0]
        self.name = "Virus"
        self.collider = False
        if random.choice([0, 1]) == 0:
            self.mirror_sprite()



    def update(self, tick):
        X1IsTile = False
        X2IsTile = False
        Y1IsTile = False
        Y2IsTile = False
        for i in RenderItems:
            for j in i:
                if j.name != "Virus" and j.type == "TILE":
                    #print(j.name)
                    if j.tileX == self.tileX + 1 and j.tileY == self.tileY:
                        X1IsTile = True
                    elif j.tileX == self.tileX - 1 and j.tileY == self.tileY:
                        X2IsTile = True
                    elif j.tileX == self.tileX and j.tileY == self.tileY + 1:
                        Y1IsTile = True
                    elif j.tileX == self.tileX and j.tileY == self.tileY - 1:
                        Y2IsTile = True

        if Y1IsTile and tick % 5 == 0:
            self.killblock(self.tileX, self.tileY + 1)
            Virus(self.tileX, self.tileY + 1, self.game)
            #QEvent(self, self.game, 1, lambda: Virus(self.tileX, self.tileY + 1, self.game))

        if Y2IsTile and tick % 5 == 0:
            self.killblock(self.tileX, self.tileY - 1)
            Virus(self.tileX, self.tileY - 1, self.game)
            #QEvent(self, self.game, 1, lambda: Virus(self.tileX, self.tileY - 1, self.game))


        if X2IsTile and tick % 5 == 0:
            self.killblock(self.tileX - 1, self.tileY)
            Virus(self.tileX - 1, self.tileY, self.game)
            #QEvent(self, self.game, 1, lambda: Virus(self.tileX - 1, self.tileY, self.game))


        if X1IsTile and tick % 5 == 0:
            self.killblock(self.tileX + 1, self.tileY)
            Virus(self.tileX - 1, self.tileY, self.game)
            #QEvent(self, self.game, 1, lambda: Virus(self.tileX + 1, self.tileY, self.game))




        Tile.update(self, tick)