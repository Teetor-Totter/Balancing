import pygame
pygame.init()

size= width, height = 1200,900

blue=(0,0,250)
green=(0,250,0)
black=(0,0,0)
speed=25

win=pygame.display.set_mode((size))

a1=pygame.Rect(200,200,50,50)#mavi.küp

a1=[pygame.image.load("deneme3.png")]
drm=True
while drm:
	
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key== pygame.K_d:
				a1.x+=speed
		if event.type==pygame.KEYDOWN:
			if event.key== pygame.K_a:
				a1.x-=speed
		if event.type==pygame.KEYDOWN:
			if event.key== pygame.K_w:
				a1.y-=speed
		if event.type==pygame.KEYDOWN:
			if event.key== pygame.K_s:
				a1.y+=speed
		
				
	win.fill((black))#yeşil.küp
	pygame.draw.rect(win,blue,a1)#mavi.küp
	pygame.display.update()