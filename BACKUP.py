import pygame
import random, math 
from pygame import mixer
pygame.init()

screen = pygame.display.set_mode((800,600))

        #Load images
icon = pygame.image.load("icon.png")
bg = pygame.image.load("bg2.png")
playerimage = pygame.image.load("player.png")
enemyimage = pygame.image.load("enemy.png")
strongenemyimage = pygame.image.load("strongenemy.png")
explosionimage = pygame.image.load("explosion.png")
menuimage = pygame.image.load("menu.png")
promptimage = pygame.image.load("promt.png")
endimage = pygame.image.load("end.png")
endscrbt = pygame.image.load("endscrbt.png")
healthimage = pygame.image.load("health.png")

# Load sound
explosionsound = mixer.Sound("explosion.wav")
bulletsound =mixer.Sound("bullet1.wav")
collisionsound =mixer.Sound("explosion.wav")
healthup = mixer.Sound("healthup.wav")
healthdown = mixer.Sound("healthdown.wav")
gameover = mixer.Sound("gameover.wav")

        # create player :
playerx = 340
playery = 540
playerchange = 0
playerlevelspeed = 0.3
playerhealth = 100
playerhealthx = 470
playerhealthy = 10
def playerhealthview(x,y) :
    playerhealthv = font.render("Player Health : " + str(playerhealth) + "%" ,True,(255,255,255))
    screen.blit(playerhealthv,(x,y))


        # create diffrent enemies                   
#noraml enemy : 
numofnormalenemy = 3   
normalenemyx =[]
normalenemyy =[]
normalenemychange = 0.1                     #for bg(0.1)  for bg1(0.5)
def changenumofnorene() :
    for i in range(numofnormalenemy) :
        normalenemyx.append(random.randint(0,740))
        normalenemyy.append(-60)
changenumofnorene()
    
    # creating health recovey 
#heath spawning 
healthx = random.randint(0,740)
healthy = -10
healthspawn = False

def checkhealthspawn() :
    global healthspawn
    if playerhealth < 100 and healthspawn == False :
        chance = random.randint(0,15000)
        if chance == 599 :
            healthspawn = True
            

def healthspawnob(x,y) :
    if healthspawn == True :
        screen.blit(healthimage,(x,y))

#collisoion for health and player :
def healthplayercollision() :
    global playerhealth
    global healthspawn
    global healthx
    global healthy
    playerhealth = 100
    healthspawn = False
    healthx = random.randint(0,740)
    healthy = -10
    mixer.Sound.play(healthup)

# creating enemy object :
def normalenemy(x,y) :
    screen.blit(enemyimage,(x,y))


#strong enemy
strongenemyx = random.randint(0,740)
strongenemyy = -60
strongenemychange = 0.15
strongenemyhealth = 20
willstrong = False

def strongenemy(x,y) :
    screen.blit(strongenemyimage,(x,y))



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
 
        # collison for every type of enemy with bullet
# collision for bullet and normal enemy
def normalenemycollision(xaxis,yaxis,i,j) :
    screen.blit(explosionimage,(xaxis,yaxis))
    mixer.Sound.play(explosionsound)
    global normalenemyx
    global normalenemyy
    normalenemyx[j] = random.randint(0,740)
    normalenemyy[j] = -60
    global bulletstate
    bulletstate[i] = "ready"
    global score
    score += 1


#collision for bullet and strong enemy
def strongenemycollision(xaxis,yaxis,i) :
    screen.blit(explosionimage,(xaxis,yaxis))
    global strongenemyhealth
    strongenemyhealth -= 10
    mixer.Sound.play(explosionsound)

    if strongenemyhealth < 1 :
        global strongenemyx
        global strongenemyy
        strongenemyx = random.randint(0,740)
        strongenemyy = -60
        
        strongenemyhealth = 20
        global willstrong
        willstrong = False
        
    global bulletstate
    bulletstate[i] = "ready"

    global score
    score += 1.5
  
    

        # creating score system 
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
endfont = pygame.font.Font("freesansbold.ttf",70)
scorex = 10
scorey = 10

def scoreview(x,y) :
    global score
    score = round(score)
    scorevalue = font.render("Score : " + str(score),True,(255,255,255))
    screen.blit(scorevalue,(x,y))

       #collison between enemy and player :
# Noramal enemy and player
def normalplayercollision(j) :
    mixer.Sound.play(healthdown)
    global playerhealth
    playerhealth -= 20
    global normalenemyx
    global normalenemyy
    normalenemyx[j] = random.randint(0,740)
    normalenemyy[j] = -60



# Strong enemy and player :
def strongplayercollision() :
    mixer.Sound.play(healthdown)
    global playerhealth
    playerhealth -= 30
    global strongenemyx
    global strongenemyy
    strongenemyx = random.randint(0,740)
    strongenemyy = -60

running = True 
menu = True
menumusic = False
bgmmusic = False
while running :
    
    while menu :
        screen.fill((0,0,0))
        screen.blit(menuimage,(0,0))
        screen.blit(promptimage,(0,0))
        if menumusic == False :
            bgmmenusong = mixer.music.load("bgmmenu.wav")
            mixer.music.play(-1)
            menumusic = True
       
        
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                menu = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    menu = False
                    mixer.music.pause() 
                # if event.key == pygame.K_m:
                #     bgmmenus = mixer.music.load("bgmmenu.wav")
                #     mixer.music.play(-1)

        pygame.display.update()

    # bgm = mixer.music.load("bgm.wav")
    # mixer.music.play(-1)

    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    if bgmmusic == False :
        bgm = mixer.music.load("bgm.wav")
        mixer.music.play(-1)
        bgmmusic = True
    # i = 0         # bullet number
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                playerchange = playerlevelspeed                        # for bg(0.3), for bg1(3)
            if event.key == pygame.K_LEFT:
                playerchange = -playerlevelspeed
            if event.key == pygame.K_SPACE :
                for i in range(numberofbullets) :
                    if bulletstate[i] == "ready" :
                        bulletstate[i] = "fire"
                        mixer.Sound.play(bulletsound)
                        bulletx[i] = playerx
                        bullety[i] = playery
                        break
            if event.key == pygame.K_e  :
                # if event.key == pygame.K_x :
                    # if event.key == pygame.K_i :
                    #     if event.key == pygame.K_t :
                            playerhealth = 0
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT :
                playerchange = 0

        #setting game boundries 
    if healthy > 600 :
        healthspawn = False    
        healthx = random.randint(0,740)
        healthy = -10       
    if playerx < 0 :
        playerx = 0
    if playerx > 770 :
        playerx =770
    for i in range(numofnormalenemy) :
        if normalenemyy[i] > 600 :
            normalenemyx[i] = random.randint(0,740)
            normalenemyy[i] = -60
            score += 0.2
    if strongenemyy >600 :
        strongenemyx = random.randint(0,740)
        strongenemyy = -60
        willstrong = False
    checkhealthspawn()
    healthspawnob(healthx,healthy)

    # collision between player and health
    distacehealthplayer = math.sqrt( math.pow((playerx-healthx),2) + math.pow((playery-healthy),2))
    if distacehealthplayer < 40 :
        healthplayercollision()
    # Enemy spawning 
        #noraml enemy
    for i in range(numofnormalenemy) :
        normalenemy(normalenemyx[i],normalenemyy[i])
        normalenemyy[i] += normalenemychange
        #strong enemy
    randomnumber = random.randint(1,5000)
    if randomnumber == 599 :
        willstrong = True

    if score > 10 and willstrong == True :
        strongenemy(strongenemyx,strongenemyy)
        strongenemyy += strongenemychange
    
    #firing bullet
    for i in range(numberofbullets) :
        if bulletstate[i] == "fire" :
            screen.blit(bulletimage[i],(bulletx[i]+15,bullety[i]+20))
            bullety[i] += bulletchange
        if bullety[i] < 0 :
            bulletstate[i] = "ready"

        if bulletstate[i] == "ready" :
            bulletx[i] = -100 

            #collison between bullet and enemy 
                # For normal enemy
            
        for j in range(numofnormalenemy) :
            noramlenemydistance = math.sqrt(math.pow(bulletx[i] - normalenemyx[j] ,2) + math.pow(bullety[i]-normalenemyy[j] ,2 ))
            if noramlenemydistance < 40 and normalenemyx[j] - bulletx[i] <10 :
                screen.blit(explosionimage,(bulletx[i],bullety[i]))
                normalenemycollisionx = bulletx[i]
                normalenemycollisiony = bullety[i]
                normalenemycollision(normalenemycollisionx,normalenemycollisiony,i,j)
            
                ### Player and enemy collision
            playerandnorenemydis = math.sqrt(math.pow(playerx - normalenemyx[j] ,2) + math.pow(playery-normalenemyy[j] ,2 ))
            if playerandnorenemydis < 40 :
                normalplayercollision(j)

            # for strong enenmy
        strongenemydistance = math.sqrt(math.pow(bulletx[i] - strongenemyx ,2) + math.pow(bullety[i]-strongenemyy ,2 ))
        playerandstrenemydis = math.sqrt(math.pow(playerx - strongenemyx ,2) + math.pow(playery-strongenemyy ,2 ))
        # collision between strong enemy and player 
        if playerandstrenemydis < 40 :
            strongplayercollision()

        if strongenemydistance < 40  :
            screen.blit(explosionimage,(bulletx[i],bullety[i]))
            
            strongenemycollisionx = bulletx[i]
            strongenemycollisiony = bullety[i]
            strongenemycollision(strongenemycollisionx,strongenemycollisiony,i)

    if score/200 > 0.1 :
        normalenemychange = score/200
    strongenemychange = 1.2 * normalenemychange

    if normalenemychange > 0.4 :
        playerlevelspeed = 0.5
        if normalenemychange > 0.5 :
            playerlevelspeed = 0.6
    if normalenemychange < 0.4 :
        playerlevelspeed = 0.3
    if score/15 > 3 :
        numofnormalenemy = int(score/15)
        changenumofnorene()
        
    scoreview(scorex,scorey)
    playerhealthview(playerhealthx,playerhealthy)
    if healthspawn == True :
        healthy += 0.1
    playerx += playerchange
    screen.blit(playerimage,(playerx,playery))
    end =False
    if playerhealth < 1 :
        # menu = True
        end = True
        yourscore = score
        score = 0
        playerhealth = 100
        playerlevelspeed = 0.3
        normalenemychange = 0.1
        numofnormalenemy = 3
        normalenemyx.clear()
        normalenemyy.clear()
        changenumofnorene()
        mixer.music.pause()
        mixer.Sound.play(gameover)
        bgmmusic = False
        men = False
        
    
    while end :
        screen.fill((0,0,0))
        currscore = endfont.render("Your Score : " + str(yourscore) ,True,(255,255,255))
        screen.blit(endimage,(0,0))
        screen.blit(endscrbt,(0,0))
        screen.blit(currscore,(200,100))
        if menumusic == False :
            bgmmenusong = mixer.music.load("bgmmenu.wav")
            mixer.music.play(-1)
            menumusic == True
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False
                menu = False
                end = False  
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_r :
                    end = False
                    menumusic = False 
                if event.key == pygame.K_e :
                    running = False
                    menu = False
                    end = False
                    
        pygame.display.update()
   
    pygame.display.update()
