from tkinter import *
from PIL import ImageTk,Image
from os import listdir

root = Tk()
root.title("ArtProjekt")
root.iconbitmap('uus_ikoon.ico')

samples = []
folder_name = 'samples'
path = r'C:\Users\Laptop\Dropbox\ProgeArtProjekt\GUI\versioon 2\\' + folder_name + '\\'
files = listdir(path)
for file in files:
    samples.append(ImageTk.PhotoImage(Image.open(path + file)))
status = Label(root, text = "Image 1 of " + str(len(samples)), bd = 1, relief = SUNKEN, anchor = E)

my_label = Label(image = samples[0])
my_label.grid(row = 0, column = 1)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=samples[image_number - 1])
    button_forward = Button(root, text = ">", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<", command = lambda: back(image_number - 1))
    
    if image_number == len(samples) - 1:
        button_forward = Button(root, text = ">", command = lambda: forward(0))

    my_label.grid(row = 0, column = 1)
    button_back.grid(row = 0, column = 0)
    button_forward.grid(row = 0, column = 2)
    
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(samples)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=samples[image_number-1])
    button_forward = Button(root, text = ">", command = lambda: forward(image_number + 1))
    button_back = Button(root, text = "<", command = lambda: back(image_number - 1))
    
    if image_number == 0:
        button_back = Button(root, text = "<", command = lambda: back(len(samples) - 1))

    my_label.grid(row = 0, column = 1)
    button_back.grid(row = 0, column = 0)
    button_forward.grid(row = 0, column = 2)
    status = Label(root, text = "Image " + str(image_number) + " of " + str(len(samples)), bd = 1, relief = SUNKEN, anchor = E)
    status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

button_back = Button(root, text = "<", command = lambda: back(len(samples)))
button_exit = Button(root, text = "exit", command = root.destroy)
button_forward = Button(root, text = ">", command = lambda: forward(2))

button_back.grid(row = 0, column = 0)
button_exit.grid(row = 1, column = 1, pady = 10)
button_forward.grid(row = 0, column = 2)
status.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)

root.mainloop()
