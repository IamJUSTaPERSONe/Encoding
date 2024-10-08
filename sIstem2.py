import tkinter as tk
from tkinter import messagebox as mb

root =tk.Tk()
root.title('system options')
root.geometry('300x250')
root.resizable(False,False)

def ch5():
    pass

def ch4():
    pass

def ch3():
    pass

def ch2():
    pass

def ch1():
    if v.get() == 1:
        mb.showinfo(title='df')



v = tk.IntVar()
posa = {"padx":6, "pady":6, "anchor":tk.NW}

chb1 = tk.Checkbutton(text='Запретить запуск панели управления', variable=v, command=ch1)
chb1.pack(**posa)

chb2 = tk.Checkbutton(text='Скрыть диск С из папки мой комп-р', command=ch2)
chb2.pack(**posa)

chb3 = tk.Checkbutton(text='Запретить настройку панели задач', command=ch3)
chb3.pack(**posa)

chb4 = tk.Checkbutton(text='Запретить перемещение панели задач', command=ch4)
chb4.pack(**posa)

chb5 = tk.Checkbutton(text='Заблокировать меню ПКМ',  command=ch5)
chb5.pack(**posa)

root.mainloop()