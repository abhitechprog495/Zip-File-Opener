#Import Necessary Modules
from tkinter import *
from tkinter import filedialog
from zipfile import ZipFile

def OpenFile():
    file_path=filedialog.askopenfilename()
    file=open(file_path,'rb')
    with ZipFile(file,'r') as zip:
        zip.printdir()
        unzip_file=filedialog.askdirectory()
        print("Processing...............")
        zip.extractall(unzip_file)
        print("Process Completed!")

root = Tk()
frame = Frame(root).pack()
root.title("Zip File Opener")
root.geometry('400x200')
button=Button(text="Select Zip File", command=OpenFile).pack()

root.mainloop()