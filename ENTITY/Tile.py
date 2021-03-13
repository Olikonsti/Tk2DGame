from GLOBAL import *

class CollisionBox():
    def __init__(self, colissionList, x, y, x2, y2, color):
        colissionList.append(self)
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color

class Tile():
    def __init__(self, tilex, tiley, layer, imagePath):

        self.path = TexturePath + imagePath
        self.image_original = Image.open(self.path).convert("RGBA")

        self.image_ = self.image_original.resize((TileSize, TileSize),Image.BOX)
        self.image = ImageTk.PhotoImage(self.image_)

        self.image_width = TileSize
        self.image_height = TileSize

        self.layer = 0
        self.draw_type = "IMAGE"

        self.type = "TILE"
        self.name = "Tile.Tile"

        self.waterloggable = False
        self.collider = True

        self.x = 0
        self.y = 0

        self.tileX = tilex
        self.tileY = tiley

        self.collisionBoxes = []

        self.width = TileSize
        self.height = TileSize

        RenderItems[layer].append(self)

    def kill(self):
        pass

    def getTileAbove(self):
        block = None
        for i in RenderItems:
            for j in i:
                if j.type == "TILE":
                    if j.tileX == self.tileX and j.tileY == self.tileY - 1:
                        block = j
        return block

    def mirror_sprite(self):
        self.image_ = ImageOps.mirror(self.image_)
        self.image = ImageTk.PhotoImage(self.image_)

    def rotate_sprite(self, degrees):
        self.image_ = self.image_.rotate(degrees)
        self.image = ImageTk.PhotoImage(self.image_)

    def texture_change(self, imagePath, mirror=False):
        self.path = TexturePath + imagePath
        self.image_original = Image.open(self.path).convert("RGBA")

        self.image_ = self.image_original.resize((self.image_width, self.image_height), Image.BOX)
        if mirror:
            self.image_ = ImageOps.mirror(self.image_)
        self.image = ImageTk.PhotoImage(self.image_)

    def calc_pos(self):
        self.x = self.tileX * TileSize
        self.y = self.tileY * TileSize

    def update(self, tick):
        pass