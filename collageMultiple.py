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

imgPaths = ["Screenshot 2025-06-23 202003.png", "Screenshot 2025-07-03 154517.png"]
loadedImgs = []

for path in imgPaths:
    imgPil = Image.open(path)
    imgSize = imgPil.resize((200, 200))
    imgTk = ImageTk.PhotoImage(imgSize)
    loadedImgs.append(imgTk)


# resize image to fit canvas dimensions

canvas.create_image(0, 0, image = loadedImgs[0], anchor="nw")
canvas.create_image(200, 200, image = loadedImgs[1], anchor="nw")

drag_data = {"item": None, "x": 0, "y": 0}

def on_button_press(event):
    # Find the item closest to the mouse click
    item = canvas.find_closest(event.x, event.y)[0]
    if item:
        drag_data["item"] = item
        # Get current coordinates of the item
        x1, y1, x2, y2 = canvas.bbox(item)
        # Calculate offset from mouse click to item's top-left corner
        drag_data["x"] = event.x - x1
        drag_data["y"] = event.y - y1

def on_mouse_drag(event):
    if drag_data["item"]:
        new_x = event.x - drag_data["x"]
        new_y = event.y - drag_data["y"]
        canvas.coords(drag_data["item"], new_x, new_y)

def on_button_release(event):
    drag_data["item"] = None

canvas.bind("<ButtonPress-1>", on_button_press)
canvas.bind("<B1-Motion>", on_mouse_drag)
canvas.bind("<ButtonRelease-1>", on_button_release)


main.mainloop()
