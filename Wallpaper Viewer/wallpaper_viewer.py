from tkinter import *
from PIL import ImageTk, Image
import os

def rotate_img():
    global counter
    img_label.config(image = img_array[counter%len(img_array)]) #[counter%len(img_array)]=> to switch from last to first img
    counter += 1

counter = 1
root = Tk()
root.title('Wallpaper Viewer')

root.geometry('650x400')
root.configure(background='black')

files = os.listdir(r'C:\Users\kvcha\Desktop\P\Python\Projects\Wallpaper Viewer\Wallpapers')

img_array = []
for file in files:
    img = Image.open(os.path.join(r'C:\Users\kvcha\Desktop\P\Python\Projects\Wallpaper Viewer\Wallpapers', file))
    resized_image = img.resize((500,300))
    img_array.append(ImageTk.PhotoImage(resized_image))

img_label = Label(root, image = img_array[0])
img_label.pack(pady=(15,10))

next_btn = Button(root, text = 'Next', bg='white', fg='black', width=28, height=2, command = rotate_img)
next_btn.pack()

root.mainloop()