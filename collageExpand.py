import tkinter as tk
from PIL import Image, ImageTk

main = tk.Tk()
main.title("Collage Expand")

width = main.winfo_screenwidth()
height = main.winfo_screenheight()
main.geometry("%dx%d" % (width, height))
main.resizable(width = True, height = True)

canvas = tk.Canvas(main, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

imgPath = "Screenshot 2025-06-23 202003.png"
orgImg = Image.open(imgPath)

# resize image to fit canvas dimensions

sizeImg = orgImg.resize((200, 200))
newImg = ImageTk.PhotoImage(sizeImg)


img = canvas.create_image(0, 0, image = newImg, anchor="nw")
canvas.image = newImg

last_x, last_y = 0, 0

def start_drag(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def do_drag(event):
    global last_x, last_y
    dx = event.x - last_x
    dy = event.y - last_y
    canvas.move(img, dx, dy)
    last_x, last_y = event.x, event.y

canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", do_drag)



main.mainloop()
