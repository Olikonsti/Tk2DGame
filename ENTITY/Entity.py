from GLOBAL import *

class CollisionBox():
    def __init__(self, colissionList, x, y, x2, y2, color):
        colissionList.append(self)
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.color = color

class Entity():
    def __init__(self, x, y, layer, ImagePath, image_width, image_height):

        self.path = TexturePath + ImagePath
        self.image_original = Image.open(self.path).convert("RGBA")

        self.image_ = self.image_original.resize((image_width, image_height), Image.BOX)
        self.image = ImageTk.PhotoImage(self.image_)

        self.image_width = image_width
        self.image_height = image_height

        self.layer = 0
        self.draw_type = "IMAGE"

        self.type = "ENTITY"
        self.name = "Entity.Entity"

        self.collider = False

        self.x = x
        self.y = y

        self.collisionBoxes = []

        self.width = 10
        self.height = 10

        RenderItems[layer].append(self)

    def mirror_sprite(self):
        self.image_ = ImageOps.mirror(self.image_)
        self.image = ImageTk.PhotoImage(self.image_)

    def texture_change(self, imagePath, mirror=False):
        self.path = TexturePath + imagePath
        self.image_original = Image.open(self.path).convert("RGBA")

        self.image_ = self.image_original.resize((self.image_width, self.image_height), Image.BOX)
        if mirror:
            self.image_ = ImageOps.mirror(self.image_)
        self.image = ImageTk.PhotoImage(self.image_)

    def update(self, tick):
        pass