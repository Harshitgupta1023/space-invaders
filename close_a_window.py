import pygame

#intialise the game
pygame.init()

#make the screen
screeen = pygame.display.set_mode((800,600))

#game loop
running = True
while running:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			running = False
