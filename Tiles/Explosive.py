from ENTITY.Tile import *
from Events import *
from ENTITY.Entity import *

class Explosive(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Explosive.png")
        self.name = "Explosive"
        self.game = GlobalGame[0]
        self.exploded = False
        QEvent(self, self.game, 100, self.showAnimation)

    def showAnimation(self):
        self.exploded = True

        self.texture_change("Explosive3.png")
        QEvent(str(self) + "animation2", self.game, 10, self.showAnimation2)

    def showAnimation2(self):
        self.exploded = True
        self.explosion = Entity(self.x, self.y, 60, "Explosion.png", 100, 100)
        self.texture_change("Explosion.png")
        QEvent(str(self) + "realExplode", self.game, 10, self.explode)

    def explode(self):
        self.explosion.killEntity()
        for i in RenderItems:
            for j in i:
                if j.type != "ENTITY" and j.name == self.name:
                    if j.tileX == self.tileX and j.tileY == self.tileY:
                        i.remove(j)
                        del j
                elif j.type != "ENTITY":
                    if j.tileX == self.tileX + 1 and j.tileY == self.tileY:
                        i.remove(j)
                        del j
                    elif j.tileX == self.tileX - 1 and j.tileY == self.tileY:
                        i.remove(j)
                        del j
                    elif j.tileX == self.tileX and j.tileY == self.tileY + 1:
                        i.remove(j)
                        del j
                    elif j.tileX == self.tileX and j.tileY == self.tileY - 1:
                        i.remove(j)
                        del j

    def update(self, tick):
        if not self.exploded:
            if tick % 10 == 0:
                self.texture_change("Explosive2.png")
            if (tick + 5) % 10 == 0:
                self.texture_change("Explosive.png")

        Tile.update(self, tick)