import tkinter as tk 
from tkinter import filedialog as fd
import ctypes

def change():
    file_path = fd.askopenfilename(filetypes=[("Image files", "*.jpg; *.jpeg;*png")])
    if file_path:
        

        ctypes.windll.user32.SystemParametersInfoW(20,0,file_path,3)        
root = tk.Tk()
root.title('Сменика фон')
root.geometry('300x150')
root['background']='pink'
root.resizable(False, False)

btn = tk.Button(root, text='Change background', command=change)
btn.place(x= 90, y=60)

root.mainloop()
