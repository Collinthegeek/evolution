import pygame, sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption('Evolution simulator')

interface = 'main'

def button(msg,fs,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(screen, (230,0,0), (x, y, w, h))
		if click[0] ==1 and action != None:
			action()
	else:
		pygame.draw.rect(screen, (255,0,0), (x, y, w, h))

	label = pygame.font.SysFont("monospace", fs).render(msg, 1, (255,255,255))
	label_rect = label.get_rect()
	label_rect.center = (x+w/2, y+h/2)
	screen.blit(label, label_rect)

def quit():
	sys.exit()

while interface == 'main':
	pygame.draw.rect(screen, (235,240,135), (0, 0, 800, 550))
	pygame.time.delay(20)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	button("text", 50, 100, 100, 100, 50, (230,0,0), (255,0,0), quit)

	pygame.display.flip()

