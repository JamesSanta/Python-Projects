
import sqlite3
#Connect to files database
conn = sqlite3.connect('files.db')

#create table filename and columns
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileName(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT)")
    conn.commit()
conn.close()

conn = sqlite3.connect('files.db')

#List of files to be entered into the files database
fileList = ('information.docx','Hello.txt', 'myImage.png', 'myMovie.MPG', 'World.txt', 'data.pdf', 'myPhoto.JPG')

#A loop to cycle through each object in fileList to find the files that end withtxt
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
            #Each row will be a name from fileList, (x.) will indicatea sigle element
            #tuple for each name ending in txt.
            cur.execute("INSERT INTO tbl_fileName (col_fname) VALUES (?)", (x,))
            print(x)
conn.close()


