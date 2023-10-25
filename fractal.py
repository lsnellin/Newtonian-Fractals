import sys, pygame, numpy, math, os
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

def calculatePixelColor(pixel):
    
    stable = False
    location = pixel.location
    for i in range(iterations):
        derivative = f_prime(location)
        if derivative.real != 0 or derivative.imag != 0:
            location -= f(location) / f_prime(location)
        else:
            break
        
        for i in range(len(roots)):
            difference = location - roots[i]
            if abs(difference.real) <= tolerance and abs(difference.imag) <= tolerance:
                pixel.color = i
                stable = True
                break
        if stable: 
            break
                
def computeFractal():
    out = open("Fractals/" + fractalNumber + ".txt", "w")
    for i in tqdm (range (height), desc="Loading..."):
        for j in range(width):
            point = pixel(ComplexNumber(i - width / 2, j - height / 2), (i, j))
            calculatePixelColor(point)
            out.write('{}'.format(point.color))
        out.write("\n")

    out.close()

def drawFractal():
    out = open("Fractals/" + fractalNumber + ".txt", "r")
    lines = out.read().split("\n")
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            color = rootColor[int(lines[i][j])]
            screen.set_at((i, j), color)
            
    
    out.close()
    
#Ask for filename
fractalNumber = input("Enter the fractal number: ")

#If file doesn't exist, compute the fractal
if not os.path.exists("./Fractals/" + fractalNumber + ".txt"):
    computeFractal()
    

#Initialize pygame
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
    drawFractal()

    
    clock.tick(1)
    