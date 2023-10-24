import sys, pygame
import Dot

#Colors:
darkPurple = pygame.Color('#160F29')
caribbeanCurrent = pygame.Color('#246A73')
darkCyan = pygame.Color('#368F8B')
champagne = pygame.Color('#F3DFC1')
desertSand = pygame.Color('#DDBEA8')

#Simulation Parameters:
numDots = 50
arrowBounce = 50
gravity = 100
friction = 0.001

def drawCircle(offsetX, offsetY, dotIndex):
    dotX = dots[dotIndex].location[0]
    dotY = dots[dotIndex].location[1]
    
    newX = dotX + offsetX
    newY = dotY + offsetY
    
    radius = 20
    pygame.draw.circle(screen, champagne, [newX, newY], radius)
    
    dots[dotIndex].location = (newX, newY)
    

def calculateOffset(dotIndex, target):
    
    (dotPosX, dotPosY)  = (dots[dotIndex].location[0], dots[dotIndex].location[1])
    (dotVelX, dotVelY)= (dots[dotIndex].velocity[0], dots[dotIndex].velocity[1])
    (targetX, targetY)  = (target[0], target[1])
    
    #Calculate Offset
    deltaVX = gravity * (targetX - dotPosX)
    deltaVY = gravity * (targetY - dotPosY)
    
    offsetX = (deltaVX + dotVelX) * friction
    offsetY = (deltaVY + dotVelY) * friction
    
    #Update Velocity 
    dots[dotIndex].velocity = (offsetX, offsetY)
    
    return dots[dotIndex].velocity




pygame.init()
size = width, height = 1280, 720
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)


#Define Data structure with all dot locations:
dots = list()
for i in range(numDots):
    dots.append(Dot.Dot((0,0), (0,0)))
    
targetPos = (0, 0)
targetVelocity = (0,0)


while True:
    #Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if pygame.mouse.get_pressed()[0]:
        targetPos = pygame.mouse.get_pos()
    if keys[pygame.K_RIGHT]:
        dots[0].velocity = (dots[0].velocity[0] + arrowBounce, dots[0].velocity[1])
    if keys[pygame.K_LEFT]:
        dots[0].velocity = (dots[0].velocity[0] - arrowBounce, dots[0].velocity[1])
    if keys[pygame.K_DOWN]:
        dots[0].velocity = (dots[0].velocity[0], dots[0].velocity[1] + arrowBounce)
    if keys[pygame.K_UP]:
        dots[0].velocity = (dots[0].velocity[0], dots[0].velocity[1] - arrowBounce)

    for i in range(numDots):
        if i == 0:
            offset = calculateOffset(0, targetPos)
            drawCircle(offset[0], offset[1], 0)
        else:    
            offset = calculateOffset(i, dots[i - 1].location)
            drawCircle(offset[0], offset[1], i)
    
    
    pygame.display.flip()
    screen.fill(darkPurple)
    clock.tick(60)
    