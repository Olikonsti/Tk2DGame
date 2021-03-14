import random
from PIL import Image
from PIL import ImageTk
from PIL import ImageOps
from Config import *


blockList = ["Grass", "Brick", "Wood", "Dirt", "Dirt2", "Water", "Lava", "Explosive", "Nuke", "Spikes", "Leaves", "Log", "Virus", "Acid", "GrassBottom", "GrassBunch", "Roots", "Chest"]
RenderItems = []
GlobalGame = []

for i in range(RenderLayers):  # -
    RenderItems.append([])  # -
def unloadItems():
    for i in range(100000):
        for i in RenderItems:
            for j in i:
                j.kill()
                i.remove(j)
    print(len(RenderItems))
    sum = 0
    for i in RenderItems:
        for j in i:
            sum += 1
    print(sum)
