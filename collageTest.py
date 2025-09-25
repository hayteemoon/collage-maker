# importing modules lets me create and modify...
# Tkinter BitmapImage and PhotoImage objects...
# from PIL images
import tkinter as tk
from PIL import Image, ImageTk

# filedialog opens dialog box to open/save file
from tkinter import filedialog
from tkinter import Label

# create a window
# root is the first window when Tkinter application starts
root = tk.Tk()

# Set Title
root.title("Collage Basic")

# make window fullscreen
# use width and height of desktop screen
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# make Window resizable
root.resizable(width = True, height = True)

# def upload():
#    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
#    path = tk.filedialog.askopenfilename(filetypes=fileTypes)
#    if len(path):
#       img = Image.open(path)
#       img = img.resize((500, 500), Image.LANCZOS)
#       pic = ImageTk.PhotoImage(img)
#        tk.Label.image = pic
#    else:
#        print("No file is chosen !! Please choose a file.")

# uploadBtn = tk.Button(root, text="+", command=upload)
# uploadBtn.pack()

image = Image.open("Screenshot 2025-06-23 202003.png")
image = image.resize((500, 500), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()


root.mainloop()
