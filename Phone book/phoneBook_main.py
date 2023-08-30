#!/usr/bin/python
#
#-*- coding: utf-8 -*-
#
#Python Ver: 3.11.4
#
#Coder: James Santa
#
#Python version: 3.1..4

from tkinter import *
import tkinter as tk
from tkinter import messagebox


import phoneBook_gui
import phoneBook_func

# tkinter frame that this class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #Master frame configuration
        self.master = master
        self.master.minsize(500,300) #height and width
        self.master.maxsize(500,300)
        
        # CenterWindow method will center the app window on the screen
        phoneBook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        
        #Catches if the window if the X is clicked on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phoneBook_func.ask_quit(self))
        arg = self.master

        #Load in GUI widgets from a seperate file
        phoneBook_gui.load_gui(self)

        #This is the menu at the top of the window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_seperator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phoneBook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_seperator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_seperator()
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
        
        
