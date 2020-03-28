import pygame

#intialise the game
pygame.init()

#make the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("flower.jpg")
pygame.display.set_icon(icon)

#player 
playerimg = pygame.image.load("spaceinvaders.png")
playerx  = 370
playery = 480
#use to show player on screen
def player(x,y):
	screen.blit(playerimg,(x,y)) 
#game loop
running = True
while running:
	#RGB-Red Green Blue ,,COLOUR THE BACKGROOUND
	screen.fill((255,255,120))
	playerx+=0.1
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	player(playerx,playery)
	pygame.display.update()	

