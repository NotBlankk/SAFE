# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

pic2=PhotoImage(master=root,file='image.png')
pic2_label=Label(root, image= pic2).grid(column=0,row=0,columnspan=5, rowspan=10)

# Progress bar widget
progress = Progressbar(root, orient = HORIZONTAL,
			length = 150, mode = 'determinate')

# Function responsible for the updation
# of the progress bar value
def bar():
    
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    
    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()

    progress['value'] = 70
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100

    import dti
    root.destroy()
progress.grid(column=0,row=5,columnspan=5, rowspan=10)

# This button will initialize
# the progress bar
Button(root, text = 'Start', command = bar).grid(column=0,row=6,columnspan=5, rowspan=10)

# infinite loop
mainloop()