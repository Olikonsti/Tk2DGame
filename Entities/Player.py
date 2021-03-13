from ENTITY.Entity import *
from Events import *
from TileSpawner import *


class Player(Entity):
    def __init__(self, x, y, world):
        self.world = world
        Entity.__init__(self, x, y, 30, "player_still.png", 55, 100)

        self.startspeed = 5
        self.speed = self.startspeed  # can be a double

        self.startx = x
        self.starty = y

        self.canbuild = True
        self.canbreak = True

        self.name = "PLAYER"

        self.walk_direction = "R"
        self.animation_delay = 16

        self.height = 77
        self.width = 55
        self.onground = False

        self.vely = 0

    def die(self):
        self.vely = 0
        self.x = self.startx
        self.y = self.starty
        self.world.xOff = self.world.startxOff
        self.world.yOff = self.world.startyOff

    def animate(self, tick, direction):
        texture = None
        if tick % self.animation_delay == 0:
            texture = "player_step1.png"
        if (tick + self.animation_delay / 2) % self.animation_delay == 0:
            texture = "player_step2.png"

        if direction == "L" and texture != None:
            self.texture_change(texture, mirror=True)
        elif texture != None:
            self.texture_change(texture)

    def waterjump(self):
        self.vely = -3

    def update(self, tick):

        # break blocks
        if (self.world.game.rc.clicked or self.world.game.mrc.clicked) and self.canbreak:
            if self.world.game.mrc.clicked:
                blockX = round((self.world.game.mrc.event.x - self.world.xOff) / TileSize)
                blockY = round((self.world.game.mrc.event.y - self.world.yOff) / TileSize)
            else:
                blockX = round((self.world.game.rc.event.x - self.world.xOff) / TileSize)
                blockY = round((self.world.game.rc.event.y - self.world.yOff) / TileSize)
            self.world.game.mrc.clicked = False
            self.world.game.rc.clicked = False
            for i in RenderItems:
                for j in i:
                    if j.type != "ENTITY":
                        if j.tileX == blockX and j.tileY == blockY:
                            i.remove(j)
                            del j


        if (self.world.game.lc.clicked or self.world.game.mlc.clicked) and self.canbuild:

            isBlock = False
            if self.world.game.mlc.clicked:
                blockX = round((self.world.game.mlc.event.x - self.world.xOff) / TileSize)
                blockY = round((self.world.game.mlc.event.y - self.world.yOff) / TileSize)
            else:
                blockX = round((self.world.game.lc.event.x - self.world.xOff) / TileSize)
                blockY = round((self.world.game.lc.event.y - self.world.yOff) / TileSize)
            self.world.game.mlc.clicked = False
            self.world.game.lc.clicked = False
            for i in RenderItems:
                for j in i:
                    if j.type != "ENTITY":
                        if j.tileX == blockX and j.tileY == blockY:
                            isBlock = True

            # creating Blocks
            if not isBlock:
                Grass(blockX, blockY)


        self.speed = self.startspeed
        collisiony = False
        collisionx1 = False
        collisionx2 = False
        collisionytop = False
        self.inwater = False
        for j in RenderItems:
            for i in j:



                # collisons

                if DrawCollision:
                    i.collisionBoxes.clear()
                    CollisionBox(i.collisionBoxes, i.x, i.y, i.x + i.width, i.y + i.height, "white")

                if i.collider or i.name == "Water":
                    if self.y + self.vely + self.height >= i.y and self.y + self.vely <= i.y + i.height and ((self.x > i.x and self.x < i.x + i.width) or(self.x + self.width > i.x and self.x < i.x + i.width)):
                        if DrawCollision:
                            CollisionBox(i.collisionBoxes, i.x, self.y + self.vely + self.height, i.x + i.width, i.y + i.height, "blue")
                        if i.name != "Water":
                            collisiony = True
                            self.onground = True
                        else:
                            self.inwater = True
                    if self.y + self.vely + self.height - 3 >= i.y and self.y + self.vely - 23 <= i.y + i.height and ((self.x > i.x and self.x < i.x + i.width) or(self.x + self.width > i.x and self.x < i.x + i.width)):
                        if DrawCollision:
                            CollisionBox(i.collisionBoxes, i.x, self.y + self.height - 3, i.x + i.width,
                                     i.y + i.height, "red")
                        if i.name != "Water":
                            collisionytop = True
                            self.onground = False

        for j in RenderItems:
            for i in j:
                if i.collider:
                    if self.y + self.height > i.y + 5 and self.y < i.y + i.height + 5 and ((self.x > i.x and self.x - 5 < i.x + i.width)):
                        collisionx1 = True
                    if self.y + self.height > i.y + 5 and self.y < i.y + i.height + 5 and ((self.x + self.width + 5 > i.x and self.x < i.x + i.width)):
                        collisionx2 = True

        if collisiony == False:
            self.onground = False

        if self.inwater:
            self.speed = 1
            self.vely = self.vely/2 + 0.8
        else:
            self.vely += 0.6

        if self.onground and self.world.game.space.clicked == False:
            self.vely = 0

        if collisionytop:
            self.vely = 0

        self.world.yOff = -(self.y) + self.world.h/2


        self.y += self.vely
        if self.world.game.space.clicked and (self.onground or self.inwater):
            if self.inwater:

                self.waterjump()
                QEvent("waterJ", self.world.game, 1, self.waterjump)

            else:
                self.vely = -17


        if self.world.game.d.clicked and not collisionx2:
            self.animate(tick, self.walk_direction)
            if self.walk_direction == "L":
                self.walk_direction = "R"
                self.mirror_sprite()
            self.x += self.speed
            self.world.xOff -= self.speed


        if self.world.game.a.clicked and not collisionx1:
            self.animate(tick, self.walk_direction)
            if self.walk_direction == "R":
                self.walk_direction = "L"
                self.mirror_sprite()
            self.x -= self.speed
            self.world.xOff += self.speed

        if self.y > 900:
            QEvent("palyer.die", self.world.game, 10, self.die)
        Entity.update(self, tick)