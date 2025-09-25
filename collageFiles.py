import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

main = tk.Tk()
main.title("Collage Maker")

width = main.winfo_screenwidth()
height = main.winfo_screenheight()
main.geometry("%dx%d" % (width, height))
main.resizable(width = True, height = True)

canvas = tk.Canvas(main, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

loadedImgs = {}

def openImg():
    filePaths = filedialog.askopenfilenames(
        title="Select Image Files",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")]
    )
    for path in filePaths:
        imgPil = Image.open(path)
        imgSize = imgPil.resize((250, 250))
        imgTk = ImageTk.PhotoImage(imgSize)
        item = canvas.create_image(0, 100, image=imgTk, anchor=tk.NW)
        loadedImgs[item] = imgTk

load_button = tk.Button(main, text="Load Images", command=openImg)
canvas.create_window(0,0, window=load_button, anchor=tk.NW)

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


def delete_image(item_id):
    if item_id in loadedImgs:
        canvas.delete(item_id)
        del loadedImgs[item_id]


def show_context_menu(event):                 
    try:
        # Check if an image is under the cursor before showing the menu
        item = canvas.find_closest(event.x, event.y)[0]
        if item in loadedImgs:
            context_menu.entryconfig("Delete", command=lambda i=item: delete_image(i))
            context_menu.tk_popup(event.x_root, event.y_root)
    finally:
        context_menu.grab_release()

context_menu = tk.Menu(main, tearoff=0)
context_menu.add_command(label="Delete")   

canvas.bind("<Button-3>", show_context_menu) # Bind right-click (Button-3)

main.mainloop()
