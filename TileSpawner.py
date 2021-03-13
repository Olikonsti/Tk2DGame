from Tiles.Dirt import *
from Tiles.Grass import *
from Tiles.Dirt2 import *
from Tiles.Foliage import *
from Tiles.Brick import *
from Tiles.Chest import *
from Tiles.Wood import *
from Tiles.Water import *
from Entities.Player import *
from ENTITY.Background import *
from GLOBAL import *


LevelData = {}

def SpawnTiles(list, world):
    print("Starting Load of " + list)
    try:
        f = open(LevelPath + list, "r")
        data = f.read()
        f.close()
        exec(data)

    except Exception as e:
        print(e)

    list = datanew


    print("Spawing World Tiles")
    if LevelData["ground"]:
        groundOffset = 17
        for i in range(50):
            #GrassBottom(i, groundOffset - 1, layer=10)
            if random.choice([0, 1, 1, 1, 1]) == 0:
                GrassBunch(i, groundOffset - 1, layer=10)
            Grass(i, groundOffset)
            Dirt2(i, groundOffset + 1)
            for j in range(5):
                Dirt(i, j + 2 + groundOffset)

    # create Background
    if LevelData["bg"] != None:
        Background(650, 500, LevelData["bg"], 1700, 1100)

    for i in range(28):
        for j in range(200):
            tile = list[i+2][j]

            if tile[0] == "G":
                Grass(j + x_w_off, i + y_w_off)

            elif tile[0] == "P":
                a = Player(world.w/2, world.h/2, world)
                print("Loading Map Player attributes:")
                for k in LevelData["Player"]:
                    print(k + ": " + str(LevelData["Player"][k]))
                    exec(f'a.{k} = {LevelData["Player"][k]}')

            elif tile[0] == "W":
                Wood(j + x_w_off, i + y_w_off)

            elif tile[0] == "L":
                block = None
                if tile[1] == "G":
                    block = "Grass"
                elif tile[1] == "D":
                    block = "Dirt2"
                Water(j + x_w_off, i + y_w_off, world.game, BLOCK=block)

            elif tile[0] == "C":
                a = Chest(j + x_w_off, i + y_w_off)
                a.NBT = LevelData["Chest"]["C" + tile[1]]


            elif tile[0] == "D":
                if tile[1] == "2":
                    Dirt2(j + x_w_off, i + y_w_off)
                else:
                    Dirt(j + x_w_off, i + y_w_off)

            elif tile[0] == "F":
                GrassBottom(j + x_w_off, i + y_w_off)

            elif tile[0] == "B":
                Brick(j + x_w_off, i + y_w_off)

            elif tile[0] == "R":
                if tile[1] == "":
                    pass
                elif tile[1] == "1":
                    Roots(j + x_w_off, i + y_w_off).rotate_sprite(270)
                elif tile[1] == "2":
                    Roots(j + x_w_off, i + y_w_off).rotate_sprite(90)
                elif tile[1] == "3":
                    Roots(j + x_w_off, i + y_w_off)
                    Roots(j + x_w_off, i + y_w_off).rotate_sprite(270)
                elif tile[1] == "4":
                    Roots(j + x_w_off, i + y_w_off)
                    Roots(j + x_w_off, i + y_w_off).rotate_sprite(90)
                else:
                    Roots(j + x_w_off, i + y_w_off)