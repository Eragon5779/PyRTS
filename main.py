import checkdeps
print('Checking dependencies...')
checkdeps.check()
print('Dependencies good! Running game...')
import pygame as p

width = 800
height = 600
title = 'PyRTS'

gameDisplay = p.display.set_mode((width, height))
p.display.set_caption(title)
clock = p.time.Clock()

def loop() :
	quit = False
	while not quit :
		for event in p.event.get() :
			if event.type == p.QUIT :
				quit = True
			#print(event)
		gameDisplay.fill((255,255,255))
		p.display.update()
		clock.tick(60)

def init() :
	pass # Will be used for loading data files later

init()
loop()
p.quit()
