from ENTITY.Tile import *

class Roots(Tile):
    def __init__(self, tx, ty):
        Tile.__init__(self, tx, ty, random.choice([20, 40]), "Roots.png")
        self.name = "Roots"
        if random.choice([1, 0, 0]) == 0:
            self.mirror_sprite()
        self.collider = False
        self.waterloggable = True

    def update(self, tick):

        Tile.update(self, tick)

class GrassBunch(Tile):
    def __init__(self, tx, ty, layer=random.choice([20, 40])):
        Tile.__init__(self, tx, ty, layer, "GrassBunch.png")
        self.name = "GRASSBUNCH"
        if random.choice([1, 0]) == 0:
            self.mirror_sprite()
        self.collider = False
        self.waterloggable = True


    def update(self, tick):

        Tile.update(self, tick)

class GrassBottom(Tile):
    def __init__(self, tx, ty, layer=random.choice([20, 40])):
        Tile.__init__(self, tx, ty, layer, "GrassBottom.png")
        self.name = "GRASSBOTTOM"
        if random.choice([1, 0]) == 0:
            self.mirror_sprite()
        self.collider = False
        self.waterloggable = True


    def update(self, tick):

        Tile.update(self, tick)