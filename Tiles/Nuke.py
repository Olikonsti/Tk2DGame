from ENTITY.Tile import *
from Events import *
from ENTITY.Entity import *
from ENTITY.Background import *

class Nuke(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, 20, "Nuke.png")
        self.name = "Nuke"
        self.game = GlobalGame[0]
        self.exploded = False
        QEvent(self, self.game, 100, self.showAnimation)

    def showAnimation(self):
        self.exploded = True
        QEvent(str(self) + "animation2", self.game, 10, self.showAnimation2)

    def showAnimation2(self):
        self.exploded = True
        self.explosion = Entity(self.x, self.y, 60, "Explosion.png", 100, 100)
        self.texture_change("Explosion.png")
        QEvent(str(self) + "realExplode", self.game, 10, self.explode)

    def explode(self):
        self.explosion.killEntity()
        self.explosion = Entity(self.x, self.y, 60, "Explosion.png", 1700, 1700)
        Background(650, 500, "pbg.png", 1700, 1100)

    def update(self, tick):
        if not self.exploded:
            if tick % 10 == 0:
                self.texture_change("Nuke.png")
            if (tick + 5) % 10 == 0:
                self.texture_change("Nuke2.png")

        Tile.update(self, tick)