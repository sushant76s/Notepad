from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save file as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # save file as a new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad by Sushant")

if __name__ == '__main__':

    # basic tkinter setup
    root = Tk()
    root.title("Untitled-Notepad")
    root.wm_iconbitmap("notepad_icon.png")
    root.geometry("644x788")
    # root.mainloop()

    # adding the text area
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    # creating a menubar
    Menubar = Menu(root)
    FileMenu = Menu(Menubar, tearoff = 0)

    # To open a new file
    FileMenu.add_command(label = "New", command = newFile)

    # To open already existing file
    FileMenu.add_command(label = "Open ", command = openFile)

    # To save the corrent file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    Menubar.add_cascade(label = "File", menu = FileMenu)

    # edit menu
    EditMenu = Menu(Menubar, tearoff = 0)
    # to give a feature of cut copy and paste
    EditMenu.add_command(label = "Cut", command = cut)
    EditMenu.add_command(label = "Copy", command = copy)
    EditMenu.add_command(label = "Paste", command = paste)
    Menubar.add_cascade(label = "Edit", menu = EditMenu)

    # help menu
    HelpMenu = Menu(Menubar, tearoff = 0)
    HelpMenu.add_command(label = "About Notepad", command = about)
    Menubar.add_cascade(label = "Help", menu = HelpMenu)

    root.config(menu = Menubar)

    # adding scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT, fill = Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)
    root.mainloop()