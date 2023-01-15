from tkinter import*
import tkinter as tk
import pygame
import os 

def hesaplama():
    veri1=float(nesne1entr.get())
    veri2=float(nesne2entr.get())
    veri3=float(nesne1metreentr.get())
    veri4=float(nesne2metreentr.get())
    tork=(veri1*veri2)-(veri3*veri4)

    veriler.config(text=tork)

 
pencere =tk.Tk()
pencere.config(background="") 
pencere.title("BALANCİNG",)
pencere.attributes('-fullscreen',True)
pencere.state("normal")

nesne1=tk.Label(text="Nesne1 kütlesi",fg="white",bg="black",font="Times 25 bold")
nesne1.place(x=10,y=50)
nesne2=tk.Label(text="Nesne2 kütlesi",fg="white",bg="black",font="Times 25 bold")
nesne2.place(x=10,y=110)
nesne1metre=tk.Label(text="Nesne1 referans\nnoktasına uzaklığı",fg="white",bg="black",font="Times 20 bold")
nesne1metre.place(x=1360,y=40)
nesne2metre=tk.Label(text="Nesne2 referans\nnoktasına uzaklığı",fg="white",bg="black",font="Times 20 bold")
nesne2metre.place(x=1360,y=115)

nesne1entr=tk.Entry(width=5,font="Times 25 bold")
nesne1entr.place(x=240,y=52)

nesne2entr=tk.Entry(width=5 ,font="Times 25 bold")
nesne2entr.place(x=240,y=110)

nesne1metreentr=tk.Entry(width=5,font="Times 35 bold")
nesne1metreentr.place(x=1590,y=45)

nesne2metreentr=tk.Entry(width=5 ,font="Times 35 bold")
nesne2metreentr.place(x=1590,y=120)


etiket =tk.Label(text="Balancing/Tork" , font = " Verdana 22 bold",fg="white")
etiket.pack()

veriler=tk.Label(text="DEĞER",fg="white",bg="black",font="Times 60 bold")
veriler.pack()

os.environ['SDL_WINDOWID'] = str(pencere.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
buton=tk.Button(pencere,text="Hesapla",fg="white",bg="black",command=hesaplama ,font="Verdana 32 bold")
buton.pack(side=tk.BOTTOM,fill=tk.X)
butonç=tk.Button(pencere,text="Exit",fg="Red",bg="black",command=exit,font="Verdana 12 bold",width=8, height=2)
butonç.pack(anchor="ne")

pygame.display.init()
ekran=pygame.display.set_mode((1980,1200))
park=pygame.image.load("deneme3.png")

x=500
y=50
button1 =buton


while True:
    ekran.blit(park,(0,0))
    
    pygame.display.update()


    pencere.mainloop()