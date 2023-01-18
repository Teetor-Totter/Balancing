from tkinter import*
import tkinter as tk
import pygame
import pymunk

def hesaplama():
    veri1=float(nesne1entr.get())
    veri2=float(nesne2entr.get())
    veri3=float(nesne1metreentr.get())
    veri4=float(nesne2metreentr.get())
    tork=(veri1*veri3)-(veri2*veri4)

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

nesne1entr=(tk.Entry(width=5,font="Times 25 bold"))
nesne1entr.place(x=240,y=52)

nesne2entr=tk.Entry(width=5 ,font="Times 25 bold")
nesne2entr.place(x=240,y=110)

nesne1metreentr=tk.Entry(width=5,font="Times 35 bold")
nesne1metreentr.place(x=1590,y=45)

nesne2metreentr=tk.Entry(width=5 ,font="Times 35 bold")
nesne2metreentr.place(x=1590,y=120)


etiket =tk.Label(text="Balancing/Tork" , font = " Verdana 22 bold",fg="white")
etiket.pack()

veriler=(tk.Label(text="DEĞER",fg="white",bg="black",font="Times 60 bold"))
veriler.pack()

buton=tk.Button(pencere,text="Hesapla",fg="white",bg="black",command=hesaplama ,font="Verdana 32 bold")
buton.pack(side=tk.BOTTOM,fill=tk.X)
butonç=tk.Button(pencere,text="Exit",fg="Red",bg="black",command=exit,font="Verdana 12 bold",width=8, height=2)
butonç.pack(anchor="ne")




pygame.display.init()
ekran=pygame.display.set_mode((1980,1200))
park=pygame.image.load("arkaplan 2.PNG")
denge=pygame.image.load("dengehali1.PNG")
button1 =buton


clock=pygame.time.Clock()
space = pymunk.Space()
body = pymunk.Body()
body.position= 400,400
shape = pymunk.Circle(body,10)
shape.density=1
space.add(body,shape)
space.gravity=0,-1000
ekran.blit(park,(0,0))
run=True
while run:
    
    pygame.draw.rect(ekran, (0,0,0), pygame.Rect(958, 760, 60, 80))
    pygame.draw.rect(ekran, (250,128,144), pygame.Rect(530, 760, 990, 15))
        
    
    
    pygame.display.update()
    clock.tick(60)
    space.step(1/60)
    pencere.mainloop()