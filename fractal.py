import sys, pygame, numpy, math
from ComplexNumber import ComplexNumber
from point import pixel
from tqdm import tqdm

#Colors:
darkPurple = pygame.Color('#160F29')
caribbeanCurrent = pygame.Color('#246A73')
darkCyan = pygame.Color('#368F8B')
champagne = pygame.Color('#F3DFC1')
desertSand = pygame.Color('#DDBEA8')

rootColor = [caribbeanCurrent, champagne, desertSand]

#Simulation Parameters:
size = width, height = 1920, 1080
iterations = 100
tolerance = 0.0001

#Polynomial Function Definitions:
a = ComplexNumber(1, 0)
b = ComplexNumber(0, 0)
c = ComplexNumber(0, 0)
d = ComplexNumber(-1, 0)

roots = [ComplexNumber(1, 0), ComplexNumber(-0.5, math.sqrt(3) / 2), ComplexNumber(-0.5, -1 * math.sqrt(3) / 2)]

def f(_a):
    return (a * _a * _a * _a) + (b * _a * _a ) + (c * _a) + d
    
def f_prime(_a):
    return (ComplexNumber(3,0) * a * _a * _a) + (ComplexNumber(2,0) * b * _a) + c

def drawPixels():
    for i in range(width):
        for j in range(height):
            pixel = points[i][j]
            screen.set_at(pixel.pixelXY, pixel.color)

def calculatePixel(pixel):
    location = pixel.location
    for i in range(iterations):
        derivative = f_prime(location)
        if derivative.real != 0 or derivative.imag != 0:
            location -= f(location) / f_prime(location)
        else:
            break
        
        for i in range(len(roots)):
            difference = location - roots[i]
            if difference.real <= tolerance and difference.imag <= tolerance:
                pixel.color = rootColor[i]
                
def initializePixels():
    points = list()

    for i in tqdm (range (width), desc="Loading..."):
        print("X: ", i)
        row = list()
        for j in range(height):
            point = pixel(ComplexNumber(i - width / 2, j - height / 2), (i, j))
            calculatePixel(point)
            row.append(point)
        points.append(row)

    return points
        

#Initialize Game:
points = initializePixels()



pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)


while True:
    #Poll for events
    for event in pygame.event.get():
        #Click X
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.display.flip()
    
    #Draw the screen
    screen.fill(darkPurple)
    drawPixels()

    
    clock.tick(1)
    