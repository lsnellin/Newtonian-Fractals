import sys, pygame, numpy, math
from ComplexNumber import ComplexNumber
from point import point

#Colors:
darkPurple = pygame.Color('#160F29')
caribbeanCurrent = pygame.Color('#246A73')
darkCyan = pygame.Color('#368F8B')
champagne = pygame.Color('#F3DFC1')
desertSand = pygame.Color('#DDBEA8')

#Simulation Parameters:
size = width, height = 1000, 1000
graphSize = scaleX, scaleY = (640, 640)
#Graph is n*m, n = real, m = imaginary
xAxis = 4
yAxis = 4

xPoints = 64
yPoints = 64

#Polynomial Function Definitions:
a = ComplexNumber(1, 0)
b = ComplexNumber(0, 0)
c = ComplexNumber(3, 0)
d = ComplexNumber(-1, 0)

def f(_a):
    return (a * _a * _a * _a) + (b * _a * _a ) + (c * _a) + d
    
def f_prime(_a):
    return (ComplexNumber(3,0) * a * _a * _a) + (ComplexNumber(2,0) * b * _a) + c

def updatePoints():
    #Loop through each point, calculate offset, and update location
    for row in points:
        for point in row:
            offset = calculateOffset(point)
            
            pointReal = point.location.real
            pointImag = point.location.imag
            
            newReal = pointReal + offset[0]
            newImag = pointImag + offset[1]
            
            point.location = ComplexNumber(newReal, newImag)
            
            drawCircle(point)

def drawCircle(point):
    (centerX, centerY) = (width / 2, height / 2) 
    pointReal = point.location.real
    pointImag = point.location.imag
    (maxReal, maxImag) = (xAxis / 2, yAxis / 2)
    #scaleX and scaleY are the max true x and y coordinates for drawing purposes

    
    
    pointX = centerX + pointReal * (scaleX / 2) / maxReal
    pointY = centerY + pointImag * (scaleY / 2) / maxImag
    
    radius = 1
    if abs(pointReal) < maxReal and abs(pointImag) < maxImag:
        pygame.draw.circle(screen, champagne, [pointX, pointY], radius)
    return
    

def calculateOffset(point):
    
    pointReal = point.location.real
    pointImag = point.location.imag
    targetReal = point.target.real
    targetImag = point.target.imag
    
    #Calculate Offset
    offsetReal = (targetReal - pointReal) / 10
    offsetImag = (targetImag - pointImag) / 10
    
    return (offsetReal, offsetImag)

def updateTargets():
    for row in points:
        for point in row:
            target = point.target
            derivative = f_prime(target)
            if derivative.real != 0 or derivative.imag != 0:
                target -= f(target) / f_prime(target)
                point.target = target
                
def initializePoints():
    points = list()
    x = numpy.linspace(-0.5, 0.5, xPoints)
    y = numpy.linspace(-0.5, 0.5, yPoints)
    for i in reversed(range(xPoints)):
        row = list()
    
        for j in reversed(range(yPoints)):
            coordinates = ComplexNumber(x[i] * xAxis, y[j] * yAxis)
            newPoint = point(coordinates, coordinates)
            row.append(newPoint)
        
        points.append(row)
    
    return points
        
def drawGraph(screen):
    left = int((width - scaleX) / 2)
    right = int((height - scaleY) / 2)
    pygame.draw.rect(screen, darkCyan, pygame.Rect(left, right, scaleX, scaleY))

def zoom(zoomIn):
    global xAxis, yAxis
    print(xAxis, yAxis)
    if zoomIn:
        xAxis *= 1.1
        yAxis *= 1.1
    else:
        xAxis /= 1.1
        yAxis /= 1.1


#Initialize Game:
points = initializePoints()
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

while True:
    #Poll for events
    for event in pygame.event.get():
        #Click X
        if event.type == pygame.QUIT:
            sys.exit()
        
        #MOUSEDOWN
        if event.type == 1025:
            if event.button == 1:
                #Iterate newton's method and update the points
                updateTargets()
            elif event.button == 3:
                #Reset Points
                points = initializePoints()
        
        #KEYS
        if event.type == 768:
            if event.unicode == '-':
                zoom(False)
            elif event.unicode == '+':
                zoom(True)
    
    #Update point Positions
    updatePoints()
    
    
    pygame.display.flip()
    
    #Draw the screen
    screen.fill(darkPurple)
    drawGraph(screen)
    
    clock.tick(60)
    