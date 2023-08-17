#
#Python Version: 3.11.4
#
#Coder: James Santa

import tkinter as tk
from tkinter import*
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta



class ParentWindow(Frame):
    def __init__(self, master):
        
        Frame.__init__(self)
        #Title of GUI window
        self.master.title("File Transfer")

        #Button to select file from source
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Button position using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #Entry box for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry box using grid
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #Button for destination directory selection
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Button position under source using grid
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #Entry box for destination selection
        self.destination_dir = Entry(width=75)
        #Entry box position using grid
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #Button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))


        #Exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Button position
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))
        
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #.delete will clear inserted in entry widget allowing path to be inserted properly
        self.source_dir.delete(0, END)
        #.insert will insert user selecetion into source entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        #.delete will clear inserted in entry widget allowing path to be inserted properly
        self.destination_dir.delete(0, END)
        #.insert will insert user selecetion into destination entry
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        #gets source
        source = self.source_dir.get()
        #gets destination
        destination = self.destination_dir.get()
        #gets list of files from source dir
        source_files = os.listdir(source)

        #Runs through each file in dir
        for i in source_files:
            dir_source = os.path.join(source, i)
            dir_destination = os.path.join(destination, i)

            #Check if file has been modified within the last 24 hours
            current_time = datetime.now() # Current time
            last_mod_time = datetime.fromtimestamp(os.path.getmtime(dir_source)) #File timestamp
            time_difference = current_time - last_mod_time

            #If file has been modified in the past 24 hours, transfer the file
            if time_difference < timedelta(days=1):
                #Moves files from source to destination
                shutil.move(dir_source, dir_destination)
                print(i + ' was successfully transferred.')
        print("File transfer completed.")
            
    def exit_program(self):
        #root is the main GUI window, destroy tells python to close the window
        root.destroy()

         
        
        
                              
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

        
        
