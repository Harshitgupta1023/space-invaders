import pygame
import random
#intialise the game
pygame.init()
#game over
over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over(x,y):
	over_text = over_font.render("GAME OVER",True,(255,255,255))
	screen.blit(over_text,(200,250))

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textx = 10
texty = 10
def showscore(x,y):
	score =  font.render("score:" + str(score_value),True,(255,255,122))
	screen.blit(score,(x,y))
#make the screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("flower.jfif")
pygame.display.set_icon(icon)

#background
background = pygame.image.load("space.jfif")
#player 
playerimg = pygame.image.load("spaceinvaders.png")
playerx  = 370
playery = 480
playerx_change=0
playery_change=0
def player(x,y):
	screen.blit(playerimg,(x,y)) 

#alien 
alienimg = [] 
alienx = [] 
alieny = [] 
alienx_change = [] 
alieny_change = [] 
number = 10 
for i in range(number):
alienimg.append(pygame.image.load("alien.png"))
alienx.append(random.randint(0,600)) alieny.append(random.randint(50,150))
alienx_change.append(1) alieny_change.append(40) def alien(i,x,y):
screen.blit(alienimg[i],(x,y))

#BULLET
bulletimg = pygame.image.load("bullet.png")
bulletx = playerx
bullety = playery
bullety_change = 5
#when to fire it
bullet_state = "ready"
	
def fire_bullet(x,y):
	global bullet_state
	bullet_state="fire"
	screen.blit(bulletimg,(x+16,y+10))
#boundary
def boundaryx(playerx):
	if playerx<=0:
		return 0
	elif playerx>=736:
		return 736
	else:
		return playerx
def boundaryy(playery):
	if playery<=0:
		return 0
	elif playery>=600-64:
		return 600-64
	else:
		return playery

#collision
def iscollision(alienx,alieny,bulletx,bullety):
	distance =  int(((alienx-bulletx)**2) + ((alieny-bullety)**2)**0.5)
	if distance < 100:
		return True
	else:
		return False
co = 0
#game loop
running = True
while running:
	#RGB-Red Green Blue ,,COLOUR THE BACKGROOUND
	screen.fill((255,255,120))
	#background
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# if keystroke is pressed check the movements
		if event.type == pygame.KEYDOWN:
			if co == number:
				running =False
			if event.key == pygame.K_UP:
				playery_change=-2
			if event.key == pygame.K_DOWN:
				playery_change=2
			if event.key == pygame.K_LEFT:
				playerx_change= -2
			if event.key == pygame.K_RIGHT:
				playerx_change= 2
			if event.key == pygame.K_SPACE:
				if bullet_state == "ready":
					bulletx = playerx
					bullety = playery
					fire_bullet(bulletx,bullety)
			
		if event.type == pygame.KEYUP :
			if event.key == pygame.K_LEFT or event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_RIGHT :
				playerx_change =0
				playery_change = 0

	#x axis movement with boundary
	for i in range(number):
		#game over
		if alienx[i]==5000:
			co+=1
			print(co)
		if co == number:
			game_over(5,5)
			break
			



		if alienx[i]>= 736:
			alienx_change[i] = -1
			alieny[i]+=alieny_change[i]
		elif alienx[i]<=0:
			alienx_change[i]=1
			alieny[i]+=alieny_change[i]
		alienx[i]+=alienx_change[i]
		if alieny[i]>=400:
			alieny[i] = 400
#collision
	
		collision = iscollision(alienx[i],alieny[i],bulletx,bullety)

		if collision:
			bullety = playery
			bullet_state = "ready"
			score_value+=1
			alienx[i] = 5000
			alieny[i] = 5000
		alien(i,alienx[i],alieny[i])


	#bullet movement
	if bullet_state == "fire":
		fire_bullet(bulletx,bullety)
		bullety-=bullety_change
	if bullety <=0:
		bullet_state = "ready"
		bullety = 480


	
	# player movements
	playerx+=playerx_change
	playery+=playery_change
	
	# player boundary
	playery = boundaryy(playery)
	playerx = boundaryx(playerx)
	
	showscore(textx,texty)
	player(playerx,playery)
	pygame.display.update()	
