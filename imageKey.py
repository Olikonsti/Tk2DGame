from tkinter import *
from PIL import Image
from PIL import ImageTk

TEXTURE_FOLDER = "textures/"
SCALING_FACTOR = 5
PIXEL_X = 100

image_list = []

def setScalingFactor(factor):
    global SCALING_FACTOR
    SCALING_FACTOR = factor

def setPixelX(pixels):
    global PIXEL_X
    PIXEL_X = pixels

def increaseScalingFactor(factor):
    global SCALING_FACTOR
    SCALING_FACTOR += factor

def redraw_images():
    print(image_list)
    for i in image_list:
        i.redraw()

def applySize(canvas):
    width = canvas.winfo_width()
    print(width)
    SCALING_FACTOR = width / PIXEL_X
    setScalingFactor(SCALING_FACTOR)
    print(width)
    redraw_images()
    print(width)

class KeyBind():
    def __init__(self, key, master, loop):
        self.app_loop = loop
        self.master = master
        self.master.bind("<" + key + ">", self.click)
        self.master.bind("<KeyRelease-" + key + ">", self.unclick)
        self.clicked = False



    def click(self, event=None):
        if self.clicked == False:
            self.clicked = True
            self.app_loop()
            #self.master.after(10, self.unclick)

    def unclick(self, event=None):
        self.clicked = False

class TKImage():
    def __init__(self, canvas, path):
        self.path = path
        self.canvas = canvas
        scaling_factor = SCALING_FACTOR
        self.image_original = Image.open(TEXTURE_FOLDER + path).convert("RGBA")

        self.original_image_width, self.original_image_height = self.image_original.size
        self.image_ = self.image_original.resize((round(self.original_image_width * scaling_factor), round(self.original_image_height * scaling_factor)), Image.BOX)
        self.image_width, self.image_height = self.image_.size
        self.image = ImageTk.PhotoImage(self.image_)
        del self.image_
        image_list.append(self)

    def place(self, x=10, y=10):
        self.x = x
        self.y = y
        self.canvas.create_image(x * SCALING_FACTOR + self.image_width/2, y * SCALING_FACTOR + self.image_height/2, image=self.image)

    def redraw(self):
        scaling_factor = SCALING_FACTOR

        self.original_image_width, self.original_image_height = self.image_original.size
        self.image_ = self.image_original.resize(
            (round(self.original_image_width * scaling_factor), round(self.original_image_height * scaling_factor)), Image.BOX)
        self.image_width, self.image_height = self.image_.size
        self.image = ImageTk.PhotoImage(self.image_)
        del self.image_
        self.place(self.x, self.y)


