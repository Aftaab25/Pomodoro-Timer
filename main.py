# Importing Libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font
import tkinter.messagebox as tmsg
import time


# the countdown function
def countdown():
    t_ = T.get(1.0, END)
    t = int(t_)
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        # timer = timer_ 
        # TODO: Change it to Label
        tmsg.showinfo(timer)
        time.sleep(1)
        t -= 1
    tmsg.showwarning("Hey time to get up and take a break!")


# input time (in seconds)
# t = input("Enter the time in seconds: ")

# countdown(int(t))


if __name__ == '__main__':
    # root/window of the App
    root = Tk()
    root.title("POMODORO TIMER")
    root.geometry("450x450")
    
    T = Text(root, height = 2, width = 10)
    T.pack()

    B = Button(root, text ="Hello", command = countdown)
    B.pack()

    # MenuBar
    # mymenu = Menu(root) # Creating a menubar (Main Menu)
    
    # # ==========================================================================
    # m1 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    # m1.add_command(label="New", command=newFile)    # Submenu under File Section to create a new file.
    # m1.add_command(label="Open", command=openFile)  # Submenu under File Section to Open a file.
    # m1.add_command(label="Save", command=saveFile)  # Submenu under File Section to Save (Save as) a new file.
    # root.config(menu=mymenu)
    # mymenu.add_cascade(label="File", menu=m1)
    
    # # ==========================================================================
    # m2 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    # m2.add_command(label="Cut", command=cut)    # Submenu under File Section to create a new file.
    # m2.add_command(label="Copy", command=copy)  # Submenu under File Section to Open a file.
    # m2.add_command(label="Paste", command=paste)  # Submenu under File Section to Save (Save as) a new file.
    # root.config(menu=mymenu)
    # mymenu.add_cascade(label="Edit", menu=m2)
    
    # # ==========================================================================
    # # The details can be shown using submenus for each category of intstructions
    # m3 = Menu(mymenu, tearoff=0) # tearoff = 0, as tearoff is not needed
    # m3.add_command(label="Brach Instructions", command=branchInstr)    # Submenu under File Section to create a new file.
    # m3.add_command(label="Stack Operations", command=stackInstr)  # Submenu under File Section to Open a file.
    # m3.add_command(label="Load & Store", command=loadStoreInstr)  # Submenu under File Section to Save (Save as) a new file.
    # m3.add_command(label="MOV & Arithmetic", command=movArithmeticInstr)  # Submenu under File Section to Save (Save as) a new file.
    # m3.add_command(label="Logical Instructions", command=logicalInstr)  # Submenu under File Section to Save (Save as) a new file.
    # m3.add_command(label="Multiply Instructions", command=mulInstr)  # Submenu under File Section to Save (Save as) a new file.
    # m3.add_command(label="Flag Instructions", command=flagInstr)  # Submenu under File Section to Save (Save as) a new file.
    # root.config(menu=mymenu)
    # mymenu.add_cascade(label="Instruction Set", menu=m3)
    
    # # Adding the remaining menus directly as they dont have any submenu
    # mymenu.add_command(label="Assemble", command=assemble)
    # mymenu.add_command(label="About", command=about)
    # mymenu.add_command(label="Quit", command=quit)
    # root.config(menu=mymenu)

    # # Adding a scrollbar
    # scroll = Scrollbar(textArea)
    # scroll.pack(side=RIGHT, fill=Y)
    # scroll.config(command=textArea.yview)
    # textArea.config(yscrollcommand=scroll.set, relief="raised")

    root.mainloop()
