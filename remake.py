import pygame
import random, math

pygame.init()

screen = pygame.display.set_mode((800,600))

        #Load images
icon = pygame.image.load("icon.png")
bg = pygame.image.load("bg.png")
playerimage = pygame.image.load("player.png")
enemyimage = pygame.image.load("enemy.png")
strongenemyimage = pygame.image.load("strongenemy.png")
explosionimage = pygame.image.load("explosion.png")


        # create player :
playerx = 340
playery = 540
playerchange = 0
playerhealth = 100


        # create diffrent enemies                   
#noraml enemy :                                     
normalenemyx = random.randint(0,740)
normalenemyy = -60
normalenemychange = 0.1

# creating enemy object :
def normalenemy(x,y) :
    screen.blit(enemyimage,(x,y))


#strong enemy
strongenemyx = random.randint(0,740)
strongenemyy = -60
strongenemyhealth = 20


        #set caption and icon 
pygame.display.set_icon(icon)
pygame.display.set_caption("MY Space Game")


        #create bullet
bulletx = []
bullety = []
bulletstate = []
bulletimage = []
numberofbullets = 5 
bulletchange = -0.5
for i in range(numberofbullets) :
    bulletx.append(-100)
    bullety.append(550)
    bulletstate.append("ready")
    bulletimage.append(pygame.image.load("bullet.png"))

        # collison
def collision(x,y,i) :
    screen.blit(explosionimage,(x,y))
    global normalenemyx
    global normalenemyy
    normalenemyx = random.randint(0,740)
    normalenemyy = -60
    global bulletstate
    bulletstate[i] = "ready"

    global score
    score += 1
    
        # creating score system 
score = 0



running = True 
while running :
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    # i = 0         # bullet number
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT:
                playerchange = 0.4
            if event.key == pygame.K_LEFT:
                playerchange = -0.4
            if event.key == pygame.K_SPACE :
                for i in range(numberofbullets) :
                    if bulletstate[i] == "ready" :
                        bulletstate[i] = "fire"
                        bulletx[i] = playerx
                        bullety[i] = playery
                        break
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                playerchange = 0

    # Enemy spawning 
    normalenemy(normalenemyx,normalenemyy)
    normalenemyy += normalenemychange

    #firing bullet
    for i in range(numberofbullets) :
        if bulletstate[i] == "fire" :
            screen.blit(bulletimage[i],(bulletx[i],bullety[i]))
            bullety[i] += bulletchange
        if bullety[i] < 0 :
            bulletstate[i] = "ready"

        if bulletstate[i] == "ready" :
            bulletx[i] = -100 
            #collison between bullet and enemy 
        distance = math.sqrt(math.pow(bulletx[i] - normalenemyx ,2) + math.pow(bullety[i]-normalenemyy ,2 ))
        if distance < 40 :
            collision(bulletx[i],bullety[i],i)
            # bulletstate[i] = "ready"
        

    playerx += playerchange
    screen.blit(playerimage,(playerx,playery))
    pygame.display.update()
