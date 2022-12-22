from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
def hesaplama():
    pass

pencere =tk.Tk() 
pencere.title("BALANCİNG",)
pencere.attributes('-fullscreen', True)
pencere.state("normal")

nesne1=tk.Label(text="Nesne1 kütlesi",fg="white",bg="black",font="Times 25 bold")
nesne1.place(x=10,y=50)
nesne2=tk.Label(text="Nesne2 kütlesi",fg="white",bg="black",font="Times 25 bold")
nesne2.place(x=10,y=110)
nesne1metre=tk.Label(text="Nesne1 referans\nnoktasına uzaklığı",fg="white",bg="black",font="Times 20 bold")
nesne1metre.place(x=10,y=220)
nesne2metre=tk.Label(text="Nesne2 referans\nnoktasına uzaklığı",fg="white",bg="black",font="Times 20 bold")
nesne2metre.place(x=10,y=300)

nesne1entr=tk.Entry(width=5,font="Times 25 bold")
nesne1entr.place(x=240,y=52)
nesne2entr=tk.Entry(width=5 ,font="Times 25 bold")
nesne2entr.place(x=240,y=110)
nesne1metreentr=tk.Entry(width=5,font="Times 35 bold")
nesne1metreentr.place(x=250,y=220)
nesne2metreentr=tk.Entry(width=5 ,font="Times 35 bold")
nesne2metreentr.place(x=250,y=305)


etiket =tk.Label(text="Balancing/Tork" , font = " Verdana 22 bold",fg="white")
etiket.pack()

buton=tk.Button(pencere,text="Hesapla",fg="white",bg="black",command=hesaplama,font="Verdana 32 bold")
buton.pack(side=tk.BOTTOM,fill=tk.X)
butonç=tk.Button(pencere,text="Exit",fg="Red",bg="black",command=exit,font="Verdana 12 bold",width=8, height=2)
butonç.pack(anchor="ne")



pencere.mainloop()