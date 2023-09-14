    # Import

import pandas as pd
import sys
import math
import numpy as np
import tkinter as tk
from tkinter.filedialog import askopenfile, askopenfilename, askdirectory




def add_column(array, col, index):
    return [row[:index] + [col] + row[index:] for row in array]

    # General

imagePaths = []
actionPaths = []
eX = []
eY = []
option = 0
scale = 1
#grid = np.array([], dtype=str)
grid = pd.DataFrame([])

tk.Tk().withdraw()

#print("Shortcut Grid:\n    1  2  3  4  5\n  1 x  x  x  x  x\n  2 x  x  x  x  x\n  3 x  x  x  x  x\n  4 x  x  x  x  x\n  5 x  x  x  x  x")

def itemValues():
    x = 1.0
    while True:
        try:
            x = float(input("Choose the horizontal position for the " + str(len(imagePaths) + 1) + ". shortcut on the grid\n    "))
            break
        except ValueError:
            print("Please enter a number or float!")

    y = 1.0
    while True:
        try:
            y = float(input("Choose the vertical position for the " + str(len(imagePaths) + 1) + ". shortcut on the grid\n    "))
            break
        except ValueError:
            print("Please enter a number or float!")

    imagePath = "C:\Path\To\File\Or\Folder"
    print("Choose the icon for the " + str(len(imagePaths) + 1) + ". shortcut")
    imagePath = askopenfilename(title = "Select an icon for the shortcut", filetypes = (("png files","*.png"),("jpeg files","*.jpg"),("ico files","*.ico")))
    print("    " + imagePath)

    actionPath = "C:\Path\To\File\Or\Folder"
    fileOrFolder = 0
    while fileOrFolder != 1 and fileOrFolder != 2 and fileOrFolder != 3:
        fileOrFolder = int(input(f"Where should the {str(len(imagePaths) + 1)}. shortcut lead to?:\n  file/program (1)\n  Steam Game (2)\n  folder (3)\n    "))
        
    if fileOrFolder == 1:
        print("Choose a file/program for the " + str(len(imagePaths) + 1) + ". shortcut")
        actionPath = askopenfilename(title = "Select an file/program for the " + str(len(imagePaths) + 1) + ". shortcut")

    if fileOrFolder == 2:
        print("Choose a Steam Game for the " + str(len(imagePaths) + 1) + ". shortcut")
        actionPath = askopenfilename(initialdir = "C:\Program Files (x86)\Steam\steamapps\common",title = "Select an Steam Game for the " + str(len(imagePaths) + 1) + ". shortcut")

    if fileOrFolder == 3:
        print("Choose a folder for the " + str(len(imagePaths) + 1) + ". shortcut")
        actionPath = askdirectory(title = "Select an folder for the " + str(len(imagePaths) + 1) + ". shortcut")
    print("    " + actionPath + "\n")

    eX.append(x)
    eY.append(y)
    imagePaths.append(imagePath)
    actionPaths.append(actionPath)

    
    
    # Input

name = input("Choose a name for the folder\n    ")
scale = input("Choose a scale for the folder (1 is default)\n    ")
if scale == "":
    scale = 1
itemValues()
#grid.resize((math.ceil(eY[0]), math.ceil(eX[0])))
#mask = np.where(grid == "")
#grid[mask] = "o"
#grid[math.ceil(eY[0]) - 1][math.ceil(eX[0]) - 1] = "+"
#print(grid)
grid.loc[math.ceil(eY[0]), math.ceil(eX[0])] = "+"
print(f"Folder Grid:\n{grid}")

while True:
    while option != 1 and option != 2:
        option = int(input("\nDo you want to:\n  add an additional shortcut (1) or\n  finish the folder (2)\n    "))
        
    if option == 1:
        option = 0
        itemValues()
        grid.loc[math.ceil(eY[len(imagePaths) - 1]), math.ceil(eX[len(imagePaths) - 1])] = "+"
        print(f"Folder Grid:\n{grid}")
        #try:
        #    grid[math.ceil(eX[len(imagePaths) - 1]) - 1][math.ceil(eY[len(imagePaths) - 1]) - 1] = "+"
        #except:
        #    print(max(eX) + "," + max(eY))
        #    grid.resize((math.ceil(max(eX)), math.ceil(max(eY))))
        #    mask = np.where(grid == "")
        #    grid[mask] = "o"
        #    grid[math.ceil(eX[len(imagePaths) - 1]) - 1][math.ceil(eY[len(imagePaths) - 1]) - 1] = "+"
        #print(grid)

    if option == 2:
        break



    # File Creation

a = open("./folderLauncher/folderCreator/" + name + "Folder.ini", "w")
b = open("./folderLauncher/@Resources/variables/variables" + name.capitalize() + ".inc", "w")



    # Folder File

# Rainmeter & Metadata
a.write("[Rainmeter]\nUpdate=1000\n\n[Metadata]\nName=" + name + "Folder\nAuthor=Temder\nInformation=A skin to launch any program\nLicense=Creative Commons BY-NC-SA\nVersion=1.3\n\n")
a.close()
a = open("./folderLauncher/folderCreator/" + name + "Folder.ini", "a")

# Variables
a.write("[Variables]\n@Include=#@#variables/variables" + name.capitalize() + ".inc\n; variable path\npX=(50*#scale#+20)*#sidePanel#\npY=0\n\n")

# Panel
a.write("[Panel]\nMeter=Image\nx=#px#\ny=#pY#\nW=(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)\nH=(((#pY#+((50+#spacing#)*(#pLY#-1)+10)*#scale#)-#pY#)+(50*#scale#)+10)\nImageTint=#pImageTint#\nImageName=#@#Images\panel.png\nHidden=1\n\n")

# Text
a.write("[Name]\nMeter=String\nX=(50/2*#scale#+10)+(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)*#sideOpen#\nY=(60*#scale#+10)\nW=(75*#scale#)\nH=100\nStringAlign=Center\nFontColor=255,255,255,255\nFontSize=(11*#scale#)\nClipString=1\nAntiAlias=1\nText=#nText#\n\n\n")

# Line
a.write("; ---------------------------------------- Open And Close Folder\n\n")

# Overlay
a.write("[Overlay]\nMeter=Image\nx=(10+(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)*#sideOpen#)\ny=10\nW=(50*#scale#)\nH=(50*#scale#)\nImageTint=#pImageTint#\nImageName=#@#images\circle.png\nLeftMouseUpAction=[!RainmeterToggleMeter Panel][!RainmeterToggleMeter closeLauncher][!RainmeterToggleMeter openLauncherImage1][!RainmeterToggleMeter openLauncherImage2][!RainmeterToggleMeter openLauncherImage3][!RainmeterToggleMeter openLauncherImage4][!RainmeterToggleMeter openItem1][!RainmeterToggleMeter openItem2][!RainmeterToggleMeter openItem3][!RainmeterToggleMeter openItem4][!RainmeterToggleMeter openItem5][!RainmeterToggleMeter openItem6][!RainmeterToggleMeter openItem7][!Update]\nMouseActionCursor=0\n\n")

# MeterCircle
a.write("[MeterCircle]\nMeter=Roundline\nx=(10+(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)*#sideOpen#)\ny=10\nW=(50*#scale#)\nH=(50*#scale#)\nStartAngle=(Rad(270))\nRotationAngle=(Rad(360))\nLineStart=(23*#scale#)\nLineLength=(25*#scale#)\nLineColor=255,255,255,200\nSolid=1\nAntiAlias=1\n\n")

# openLauncherImage1-4
openLauncher = [1, 5, 1, 5, 1, 1, 5, 5]
for i in range(1, 5):
    a.write("[openLauncherImage" + str(i) + "]\nMeter=Image\nx=(" + str(openLauncher[i - 1]) + "*(5*#scale#)+10)+(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)*#sideOpen#\ny=(" + str(openLauncher[i + 3]) + "*(5*#scale#)+10)\nH=(20*#scale#)\nSolidColor=0,0,0,1\nImageName=#e" + str(i) + "Image#\n\n")

# closeLauncher
a.write("[closeLauncher]\nMeter=Image\nx=((5*#scale#)+10)+(((#pX#+((50+#spacing#)*(#pLX#-1)+10)*#scale#)-#pX#)+(50*#scale#)+10)*#sideOpen#\ny=((5*#scale#)+10)\nH=(40*#scale#)\nImageTint=255,255,255,255\nImageName=#@#Images/arrow.png\nMouseActionCursor=0\nHidden=1\n\n")

# Launcher Items
a.write("; ---------------------------------------- Launcher Items\n\n")

# openItemN
for i in range(len(imagePaths)):
    a.write("[openItem" + str(i + 1) + "]\nMeter=Image\nx=(#pX#+((50+#spacing#)*(#e" + str(i + 1) + "X#-1)+10)*#scale#)\ny=(#pY#+((50+#spacing#)*(#e" + str(i + 1) + "Y#-1)+10)*#scale#)\nH=(50*#scale#)\nSolidColor=0,0,0,1\nImageName=#e" + str(i + 1) + "Image#\nLeftMouseUpAction=#e" + str(i + 1) + "Action#\nMouseActionCursor=0\nHidden=1\n\n")



    # Variable File

# Variables
b.write("[Variables]\n\n; ---------------------------------------- Launcher\n\nscale=" + str(scale) + "\nspacing=10\n\n")

# Item N
for i in range(len(imagePaths)):
    b.write(';           Item ' + str(i + 1) + '\ne' + str(i + 1) + 'X=' + str(eX[i]) + '\ne' + str(i + 1) + 'Y=' + str(eY[i]) + '\ne' + str(i + 1) + 'Image="' + imagePaths[i] + '"\ne' + str(i + 1) + 'Action=["' + actionPaths[i] + '"]\n\n')




# Panel
b.write("pLX=" + str(max(eX)) + "\npLY=" + str(max(eY)) + "\npImageTint=60,60,60,200\n\nnText=" + name.capitalize() + "\n\nsideOpen=0\nsidePanel=1")

a.close()
b.close()