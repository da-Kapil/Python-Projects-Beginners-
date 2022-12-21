from tkinter import *
from PIL import ImageTk, Image # pillow(pip install) Python imaging library
from tkinter import messagebox

def handle_login(): # Creating function to handle login inputs
    email = email_input.get()
    password = password_input.get()
    
    if email == 'shiva@gmail.com' and password == '1234':
        messagebox.showinfo('Yayyy','Login Successful')
    else:
        messagebox.showerror('Error','Login Failed')

root = Tk() # object of Tk class

root.title('Login Form') # Display login form
# root.iconbitmap('favicon.ico') # for icon/logo of the form
root.geometry('500x300') # minsize and maxsize to set the size of the window

root.configure(background='#0096DC') # window's background color

# Tkinter has geometry manager - It is like a interior designer(it decides whatever UI elements will be set on what place).
# Geometry managers are of 2 types:- pack and grid
img = Image.open(r'C:\Users\kvcha\Desktop\P\Python\Projects\GUI\flipkart-logo.png') # storing flipkart logo in the variable
resized_image = img.resize((70,70)) # resizing the fk logo, otherwise it displays the logo on fullscreen
img = ImageTk.PhotoImage(resized_image) # function for loading fk logo on gui window

img_label = Label(root, image=img)
img_label.pack(pady=(10,10)) # It will know automatically where to place the fk logo
                            # pady - label(fk logo) gap from above 10 and below 10

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24)) # font type and size

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20,5)) # label(Enter Email) gap 20 from above and 5 from below
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50) # to make a enter box. width parameter for input box's width
email_input.pack(ipady=6, pady=(1,15)) # ipady for size on y axis(height of input box)

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20,5)) # label(Enter Email) gap 20 from above and 5 from below
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1,15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login) # login button with command
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana', 10))

root.mainloop() # mainloop keeps the GUI consistently on the screen, otherwise it will display and go