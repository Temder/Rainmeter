from PIL import Image, ImageTk
from tkinter import Tk, Label, Canvas

root = Tk()

root.geometry("595x397")
root.configure(bg = "black")

canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 397,
    width = 595,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

print(Image.open("folderLauncher/@Resources/icons/access_line.png").mode)

def RBGAImage(path):
    return Image.open(path).convert("RGBA")

face = RBGAImage("folderLauncher/@Resources/icons/access_line.png")

facepic = ImageTk.PhotoImage(face)

label1 = Label(image=facepic)
label1.grid(row = 0, column = 0)

root.mainloop()