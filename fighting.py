import pygame
import random

pygame.init()

myFont = pygame.font.SysFont("Times New Roman", 18)

display_width=800
display_height=600

points = 0

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (128,128,128)


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Fighting')
clock = pygame.time.Clock()

Stick = pygame.image.load('Stick.png')
StickWalk1 = pygame.image.load('StickWalk1.png')
StickWalk2 = pygame.image.load('StickWalk2.png')
StickWalk3 = pygame.image.load('StickWalk3.png')
StickWalk4 = pygame.image.load('StickWalk4.png')
StickWalk5 = pygame.image.load('StickWalk5.png')
StickPunch1 = pygame.image.load('StickPunch1.png')
StickPunch2 = pygame.image.load('StickPunch2.png')
StickPunch3 = pygame.image.load('StickPunch3.png')
StickPunch4 = pygame.image.load('StickPunch4.png')
StickPunch5 = pygame.image.load('StickPunch5.png')
StickPunch6 = pygame.image.load('StickPunch6.png')



class human:
    def __init__(self):
        self.health = 100
        self.weapon = "Hands"
        self.armour = "None"
        self.xStick = 10
        self.yStick = 160
        self.xStickChange = 0
        self.yStickChange = 0
        self.stickLeft = False
        self.stickRight = False
        self.stickStance = "R"
        self.stickPunch = False
        self.stickPunchLatch = False
        self.frame = 1

def score(points,health):
    pointsDisplay = myFont.render(str(points), 1, black)
    healthDisplay = myFont.render(str(health), 1, red)
    gameDisplay.blit(pointsDisplay, (display_width * 0.9,display_height * 0.9))
    gameDisplay.blit(healthDisplay, (display_width * 0.9,display_height * 0.1))

#def enemy(x1,y1):
#    gameDisplay.blit(enemy1, (x1,y1))

def walkRight(xStick,yStick,frame):
    xStickChange = +10
    xStick = xStick + xStickChange
    if frame == 1:
        gameDisplay.blit(StickWalk1, (xStick,yStick))
    elif frame == 2:
        gameDisplay.blit(StickWalk2, (xStick,yStick))
    elif frame == 3:
        gameDisplay.blit(StickWalk3, (xStick,yStick))
    elif frame == 4:
        gameDisplay.blit(StickWalk4, (xStick,yStick))
    elif frame == 5:
        gameDisplay.blit(StickWalk5, (xStick,yStick))
    frame = frame + 1
    if frame > 5:
        frame = 1
    return xStick,yStick,frame

def walkLeft(xStick,yStick,frame):
    xStickChange = -10
    xStick = xStick + xStickChange
    if frame == 1:
        gameDisplay.blit(pygame.transform.flip(StickWalk1, True, False), (xStick,yStick))
    elif frame == 2:
        gameDisplay.blit(pygame.transform.flip(StickWalk2, True, False), (xStick,yStick))
    elif frame == 3:
        gameDisplay.blit(pygame.transform.flip(StickWalk3, True, False), (xStick,yStick))
    elif frame == 4:
        gameDisplay.blit(pygame.transform.flip(StickWalk4, True, False), (xStick,yStick))
    elif frame == 5:
        gameDisplay.blit(pygame.transform.flip(StickWalk5, True, False), (xStick,yStick))
    frame = frame + 1
    if frame > 5:
        frame = 1
    return xStick,yStick,frame

def punch(xStick,yStick,frame,stickPunch,stickPunchLatch, stickStance):
    if stickStance == "R":
        if frame == 1:
            gameDisplay.blit(StickPunch1, (xStick,yStick))
        elif frame == 2:
            gameDisplay.blit(StickPunch2, (xStick,yStick))
        elif frame == 3:
            gameDisplay.blit(StickPunch3, (xStick,yStick))
            hitCheck(stickStance,xStick,yStick,20,100)
        elif frame == 4:
            gameDisplay.blit(StickPunch4, (xStick,yStick))
            hitCheck(stickStance,xStick,yStick,20,120)
        elif frame == 5:
            gameDisplay.blit(StickPunch5, (xStick,yStick))
        elif frame == 6:
            gameDisplay.blit(StickPunch6, (xStick,yStick))
        frame = frame + 1
        if frame > 6:
            stickPunch = False
            stickPunchLatch = True
            frame = 1
    elif stickStance == "L":
        if frame == 1:
            gameDisplay.blit(pygame.transform.flip(StickPunch1, True, False), (xStick,yStick))
        elif frame == 2:
            gameDisplay.blit(pygame.transform.flip(StickPunch2, True, False), (xStick,yStick))
        elif frame == 3:
            gameDisplay.blit(pygame.transform.flip(StickPunch3, True, False), (xStick,yStick))
            hitCheck(stickStance,xStick,yStick,20,100)
        elif frame == 4:
            gameDisplay.blit(pygame.transform.flip(StickPunch4, True, False), (xStick,yStick))
            hitCheck(stickStance,xStick,yStick,20,120)
        elif frame == 5:
            gameDisplay.blit(pygame.transform.flip(StickPunch5, True, False), (xStick,yStick))
        elif frame == 6:
            gameDisplay.blit(pygame.transform.flip(StickPunch6, True, False), (xStick,yStick))
        frame = frame + 1
        if frame > 6:
            stickPunch = False
            stickPunchLatch = True
            frame = 1
    return frame,stickPunch,stickPunchLatch


def stick(xStick,yStick,stickLeft,stickRight,frame,stickStance,stickPunch,stickPunchLatch):
    if (stickPunch == True and stickPunchLatch == False):
        print("Punch!")
        frame,stickPunch,stickPunchLatch = punch(xStick,yStick,frame,stickPunch,stickPunchLatch, stickStance)
        

    else:
        if (stickRight == True and stickLeft == False and xStick <= 620):
            # print(xStick)
            xStick,yStick,frame = walkRight(xStick,yStick,frame)

        elif (stickLeft == True and stickRight == False and xStick >= -120):
            # print(xStick)
            xStick,yStick,frame = walkLeft(xStick,yStick,frame)

        else:
            xStickChange = 0
            gameDisplay.blit(Stick, (xStick,yStick))
    return xStick,yStick,stickLeft,stickRight,frame,stickStance,stickPunch,stickPunchLatch

def hitCheck(stickStance,xStick,yStick,minDistance,maxDistance):
    damage = 100
    for enemy in enemies:
        if stickStance == "L" and (xStick-enemy.xStick) < maxDistance and (xStick-enemy.xStick) > minDistance:
            enemy.health = enemy.health - damage
        elif stickStance == "R" and (enemy.xStick-xStick) < maxDistance and (enemy.xStick-xStick) > minDistance:
            enemy.health = enemy.health - damage

def stickEnemy(enemy):
    if enemy.health <= 0:
        del enemies[index]

def stickEnemyInit(enemy):
    enemy.stickLeft = True

your = human()

enemies = []


points = 0
while your.health >= 0:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                your.stickLeft = True
                your.stickStance = "L"
            if event.key == pygame.K_RIGHT:
                your.stickRight = True
                your.stickStance = "R"
            if (event.key == pygame.K_SPACE and your.stickPunchLatch == False):
                your.stickPunch = True
            if event.key == pygame.K_s:
                enemies.append(human())
                stickEnemyInit(enemies[-1])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                your.stickLeft = False
                your.frame = 1
            if event.key == pygame.K_RIGHT:
                your.stickRight = False
                your.frame = 1
            if event.key == pygame.K_SPACE:
                your.stickPunch = False
                your.stickPunchLatch = False
                your.frame = 1

    gameDisplay.fill(white)        
    your.xStick, your.yStick, your.stickLeft, your.stickRight, your.frame, your.stickStance, your.stickPunch, your.stickPunchLatch = stick(
        your.xStick, your.yStick, 
        your.stickLeft, your.stickRight, 
        your.frame, your.stickStance,
        your.stickPunch, your.stickPunchLatch)
    for index, enemy in enumerate(enemies):
        print(enemy.xStick)
        enemy.xStick, enemy.yStick, enemy.stickLeft, enemy.stickRight, enemy.frame, enemy.stickStance, enemy.stickPunch, enemy.stickPunchLatch = stick(
        enemy.xStick, enemy.yStick, 
        enemy.stickLeft, enemy.stickRight, 
        enemy.frame, enemy.stickStance,
        enemy.stickPunch, enemy.stickPunchLatch)
        print(enemy.xStick)
        stickEnemy(enemy)
        print(enemy.xStick)
        if enemy.xStick < -100:
            enemy.stickLeft = False
            enemy.stickRight = True
        if enemy.xStick > 600:
            enemy.stickRight = False
            enemy.stickLeft = True

    score(points,your.health)
    pygame.display.update()
    clock.tick(40)

pygame.quit
quit()