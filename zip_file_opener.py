#Import Necessary Modules
from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

#Function to select files to unzip and also
#select diectory to place unzip file/folder
def OpenFile():
    file_path=filedialog.askopenfilename()
    file=open(file_path,'rb')
    with ZipFile(file,'r') as zip:
        zip.printdir()
        unzip_file=filedialog.askdirectory()
        print("Processing...............")
        zip.extractall(unzip_file)
        print("Process Completed!")

#Set the window of the application
root = Tk()
frame = Frame(root).pack()
root.title("Zip File Opener")
root.geometry('400x200')
button=Button(text="Select Zip File", command=OpenFile).pack()

#Control the window
root.mainloop()
