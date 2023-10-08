import numpy as np
import pandas as pd
import re

okuma=pd.read_excel("checklist.xlsx")
print(okuma)

from tkinter import *

master=Tk()
canvas=Canvas(master,height=750,width=750)
canvas.pack()

frame_ust=Frame(master,bg='#add8e6')
frame_ust.place(relx=0,rely=0,relwidth=1,relheight=1)

Label(frame_ust,text="Drone Sorgu",bg="#add8e6",font="Verdana 12 bold").pack(padx=10,pady=10,anchor=NW)

var1=IntVar()
C1=Checkbutton(frame_ust,text='Pervane yönleri doğru mu?',variable=var1,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C1.pack(anchor=NW,pady=5,padx=25)

var2=IntVar()
C2=Checkbutton(frame_ust,text='Bataryanın voltjı tam mı?',variable=var2,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C2.pack(anchor=NW,pady=5,padx=25)

var3=IntVar()
C3=Checkbutton(frame_ust,text='Rüzgar hızı uygun mu?',variable=var3,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C3.pack(anchor=NW,pady=5,padx=25)

var4=IntVar()
C4=Checkbutton(frame_ust,text='Kodlar güncel mi',variable=var4,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C4.pack(anchor=NW,pady=5,padx=25)

var5=IntVar()
C5=Checkbutton(frame_ust,text='Pixhawk bağlantısı başarılı mı?',variable=var5,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C5.pack(anchor=NW,pady=5,padx=25)

var6=IntVar()
C6=Checkbutton(frame_ust,text='Kameradan görüntü alınabiliyor mu?',variable=var6,onvalue=1,offvalue=0,bg='#add8e6',font="Verdana 10")
C6.pack(anchor=NW,pady=5,padx=25)

master.mainloop()