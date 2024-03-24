import pygame
import random
import time
import math
#initilize pygame
pygame.init()



#intiatize game window
screen = pygame.display.set_mode((800,600))



#change icon and title of game window 
pygame.display.set_caption("Project 1","Blaze")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)




#creating player image and positon 
playerimage = pygame.image.load("player.png")
playerx = 370
playery = 535
playerchangex = 0

#creating enemy image and position
enemyimage = pygame.image.load("enemy.png")
enemyx = random.randint(0,740)
enemyy = random.randint(0,50)
enemychange  = 0.2

#creating enemy object 
def enemy(x,y) :
    screen.blit(enemyimage,(x,y))




#create player object
def player(x,y):
    screen.blit(playerimage,(x,y))

#creating score 
    
score = int(0)

#background
bg = pygame.image.load("bg.png")

#create bullete to fire 
bulletimage = pygame.image.load("bullet.png")
bulletx = 0
bullety = 535
bulletchange = -0.5
bulletstate = "ready"
def bullet(x,y) :
    screen.blit(bulletimage,(x,y))
    global bulletstate 
    bulletstate = "fire"


#collision between bullet and enemy

def collison() :
    global score
    score +=10
    
    print(score)
#create loop to endlessly show game window presssed quit 
running = True
while running :
    #fill background with colour
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))

    #check every event type by creating a loop for every event in a endless loop of while loop till game is running
    for event in pygame.event.get() :
        if(event.type==pygame.QUIT) :
            running = False

            #implimenting controls in x axis
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                playerchangex = 0.5
            if event.key == pygame.K_LEFT :
                playerchangex = -0.5
            if event.key == pygame.K_SPACE :
                bulletx = playerx+20
                bullety = playery
                bullet(bulletx,bullety)

        if event.type == pygame.KEYUP :
            playerchangex = 0
        
    #setting score increase condition
    if enemyy > 600 :
            score += 1

    # setting boundries to the game 
    if playerx > 770 :   
        playerx = 770
    if playerx < -40 :
        playerx = -40
    if enemyy > 540 :
        enemyx = random.randint(0,740)
        enemyy = random.randint(0,50) 
        score += 1
        print(score)
            
    diffrence = math.sqrt(math.pow(bulletx - enemyx ,2) + math.pow(bullety-enemyy ,2 ))
    # print(diffrence)
    if diffrence < 50 :
        enemyx = random.randint(0,740)
        enemyy = random.randint(0,50)
        bulletstate = "ready"
        score += 10
        print(score)

    if bulletstate == "fire" :
        bullet(bulletx,bullety)
        bullety += bulletchange
    enemy(enemyx,enemyy)
    enemyy+= enemychange
    playerx += playerchangex
    player(playerx,playery)    
    pygame.display.update()         #update display every time when a fucntion is called in while loop 

    