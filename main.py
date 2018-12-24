import pygame, sys, random
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Evolution simulator')

creatures = []
children = []
interface = 'generation'
generation = 0
#creatures = pygame.sprite.Group()

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

def generate():
	global creatures
	for creature in range(1):
		new_creature = Creature()
		creatures.append(new_creature)
	global interface
	interface = 'reproduction'

	for creature in creatures:
		print "Creature: " + str(creature)
		print '\n'
		for node in creature.nodes:
			print "Node: " + str(node)
			print "   size: " + str(node.size)
			print "   friction: " + str(node.friction)
		print '\n'
		for muscle in creature.muscles:
			print "Muscle: " + str(muscle)
			print "   extended length: " + str(muscle.extended)
			print "   contracted length: " + str(muscle.contracted)
			print "   strength: " + str(muscle.strength)
		print "\n\n=========================================================================================\n\n"

def reproduce():
	for parent in creatures:
		new_creature = Creature(parent)
		children.append(new_creature)
	global creatures
	creatures = creatures + children
	global interface
	interface = 'watch'
	for creature in children:
		print "Creature: " + str(creature)
		print '\n'
		for node in creature.nodes:
			print "Node: " + str(node)
			print "   size: " + str(node.size)
			print "   friction: " + str(node.friction)
		print '\n'
		for muscle in creature.muscles:
			print "Muscle: " + str(muscle)
			print "   extended length: " + str(muscle.extended)
			print "   contracted length: " + str(muscle.contracted)
			print "   strength: " + str(muscle.strength)
		print "\n\n=========================================================================================\n\n"


class Node:
	def __init__(self, parent=None):
		if not parent:
			self.size = random.uniform(10,50)
			self.friction = random.uniform(0,5)
		else:
			self.size = parent.size + random.uniform(-2, 2)
			self.friction = parent.friction + random.uniform(-2, 2)

class Muscle:
	def __init__(self, parent=None):
		if not parent:		
			self.extended = random.uniform(5,10)
			self.contracted = random.uniform(0,5)
			self.strength = random.uniform(0,5)
			#self.contractedtime = 
			#self.extendedtime = 
		else:
			self.extended = parent.extended + random.uniform(-2,2)
			self.contracted = parent.contracted + random.uniform(-2,2)
			self.strength = parent.strength + random.uniform(-2,2)
			#self.contractedtime = parent.extended + random.uniform(-2,2)
			#self.extendedtime = parent.extended + random.uniform(-2,2)

class Creature:
	def __init__(self, parent=None):
		self.heartbeat = 20
		self.fitness = 0		
		self.nodes = []
		self.muscles = []
		if not parent:
			for node in range(random.randint(2,5)):
				self.nodes.append(Node())
			for muscles in range(random.randint(1,5)):
				self.muscles.append(Muscle())
		else:
			if random.randint(1,100) != 1:
				for node in parent.nodes:
					self.nodes.append(Node(node))
				for muscle in parent.muscles:
					self.muscles.append(Muscle(muscle))
			else:
				if random.randint(1,2) == 2:
					pass # major node mutation
				else:
					pass # major muscle mutation
			
		
while interface == 'generation':
	pygame.draw.rect(screen, (235,240,135), (0, 0, 1200, 700))
	pygame.time.delay(20)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	button("generate", 50, 550, 600, 200, 75, (230,0,0), (255,0,0), generate)
	pygame.display.flip()

while interface == 'reproduction':
	pygame.draw.rect(screen, (235,240,135), (0, 0, 1200, 700))
	pygame.time.delay(20)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	button("Reproduce", 50, 550, 400, 200, 75, (230,0,0), (255,0,0), reproduce)
	
#players.add(player)
	pygame.display.flip()

while interface == 'watch':
	pygame.draw.rect(screen, (235,240,135), (0, 0, 1200, 700))
	pygame.time.delay(20)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	for node in creatures[1].nodes:
		pygame.draw.circle(screen, (255,0,0), (500,500), int(node.size))

	
	pygame.display.flip()


