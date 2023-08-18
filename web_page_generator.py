#
#Python Version: 3.11.4
#
#Coder: James Santa

import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator") #Title

        #Button for default HTML sizing and location
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=4,column=4, padx=(10, 10) , pady=(10, 10))

        ##Button for custom text HTML sizing and location
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.entryHTML)
        self.btn.grid(row=4,column=6, padx=(10, 10) , pady=(10, 10))

        #Text for location entry box
        self.lbl_entry = tk.Label(self.master,text='Enter custom text or click the Default HTML page button')
        self.lbl_entry.grid(row=0, column=2, padx=(10,10), pady=(10,10), sticky=N+W)

        #Location for entry box
        self.var_entry = tk.StringVar()
        self.txt_entry = tk.Entry(self.master, textvariable=self.var_entry)
        self.txt_entry.grid(row=1,column=0,rowspan=1,columnspan=8,padx=(10,10),pady=(10,10),sticky=N+E+W)
        
        
    #Creates HTML page with premade text
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    #Creates HTML page with custom text
    def entryHTML(self):
        htmlText = self.var_entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
