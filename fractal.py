import sys, pygame, numpy, math, os
from ComplexNumber import ComplexNumber
from point import pixel
from tqdm import tqdm
from polynomial import poly


#Colors:
darkPurple = pygame.Color('#160F29')
caribbeanCurrent = pygame.Color('#246A73')
darkCyan = pygame.Color('#368F8B')
champagne = pygame.Color('#F3DFC1')
desertSand = pygame.Color('#DDBEA8')
blue = pygame.Color('#084887')
orange = pygame.Color('#F58A07')
green = pygame.Color('#03CEA4')

rootColor = [blue, orange, green]

#Simulation Parameters:
size = width, height = 1920, 1080
iterations = 100
tolerance = 0.0001


def findRoots(coeff):
    return numpy.roots(coeff)

def calculatePixelColor(pixel, polynomial, roots):
    
    stable = False
    location = pixel.location
    for i in range(iterations):
        derivative = polynomial.deriv(location)
        if derivative.real != 0 or derivative.imag != 0:
            location -= polynomial.val(location) / derivative
        else:
            break
        
        for j in range(len(roots)):
            difference = location - roots[j]
            if abs(difference.real) <= tolerance and abs(difference.imag) <= tolerance:
                pixel.color = j
                pixel.shade =  i
                stable = True
                break
        if stable: 
            break
                
def computeFractal():
    out = open("Fractals/" + fractalNumber + ".txt", "w")
    polynomial = poly(polynomialDef)
    roots = findRoots(polynomialDef)
    contents = ""
    for i in tqdm(range (height), desc="Loading..."):
        for j in range(width):
            location = complex(i - width / 2, j - height / 2)
            px = pixel(location, (i, j))
            calculatePixelColor(px, polynomial, roots)
            ''.join((contents, '{}{}'.format(px.color, px.shade)))
        ''.join((contents,"\n"))

    out.write(contents)
    out.close()

def drawFractal():
    out = open("Fractals/" + fractalNumber + ".txt", "r")
    lines = out.read().split("\n")
    for i in range(len(lines)):
        j = 1
        line = lines[i]
        pixels = line.split(',')
        for p in pixels:
            if not (p == ''):
                pArr = p.split(':')
                c = int(pArr[0])
                s = int(pArr[1])
            
                numShades = 10
                shade = (s % numShades) / (numShades * 2) + 0.5
                
                color = rootColor[c]
                shadedColor = pygame.Color(int(color.r * shade), int(color.g * shade), int(color.b * shade))
                
                """Draw from top to bottom (Each line represents a row of pixels, i = height, j = width"""
                screen.set_at((j, i), shadedColor) 
                                                                           
            j = j+1
            
    
    out.close()


#Polynomial Function Definitions:
polynomialDef = [5,3,27,1,26,3,8,10,2]
    
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
    