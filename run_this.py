from PIL import Image
import numpy as np
import os

from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames

# Make high resolution of GUI (not blurry)
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

Tk().withdraw()

# Show an "Open" dialog box and return the path to the selected file.
filenames = askopenfilenames(initialdir=os.getcwd())

# Convert the tuple to a list.
filenames = list(filenames)

# Open each files and save it as WebP
for item in filenames:
     im = Image.open(item)
     item = item.rstrip(".png")
     item = item + ".webp"
     im.save(item, format = "WebP", lossless = True)
