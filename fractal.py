import sys, pygame, numpy, math, os, multiprocessing, random
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


#Simulation Parameters:
size = width, height = 1000, 1000
iterations = 100
tolerance = 0.0001
polynomialDef = [1,0,0,0,0,0,0,0,0,0,0,0,-1]
rootColor = list()

for i in range(len(polynomialDef) - 1):
    color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    rootColor.append(color)

def findRoots(coeff):
    return numpy.roots(coeff)

def calculatePixelColor(args):
    i, j, width, height, polynomial, roots, tolerance, iterations = args
    location = complex(i - width / 2, j - height / 2)
    color = 0
    shade = 10
    
    stable = False
    for it in range(iterations):
        derivative = polynomial.deriv(location)
        if derivative.real != 0 or derivative.imag != 0:
            location -= polynomial.val(location) / derivative
        else:
            break
        
        for r, root in enumerate(roots):
            difference = location - root
            if abs(difference.real) <= tolerance and abs(difference.imag) <= tolerance:
                color = r
                shade =  it
                stable = True
                break
        if stable: 
            break
        
    return f"{color}:{shade}"
                
def computeFractal(width, height, iterations, tolerance, polynomialDef, fractalNumber):
    polynomial = poly(polynomialDef)
    roots = findRoots(polynomialDef)
    pool = multiprocessing.Pool(processes=1)
    
    with open(f"Fractals/{fractalNumber}.txt", "w") as out:
        pixel_args = [(i, j, width, height, polynomial, roots, tolerance, iterations) for i in range(height) for j in range(width)]
        results = pool.map(calculatePixelColor, pixel_args)
        pixels = numpy.array(results).reshape(height, width)
        numpy.savetxt(out, pixels, fmt="%s", delimiter=",")

def drawFractal(screen, fractalNumber):
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

def main() :
    #Ask for filename
    fractalNumber = input("Enter the fractal number: ")

    #If file doesn't exist, compute the fractal
    if not os.path.exists("./Fractals/" + fractalNumber + ".txt"):
        computeFractal(width, height, iterations, tolerance, polynomialDef, fractalNumber)
        

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
        drawFractal(screen, fractalNumber)

        
        clock.tick(1)

if __name__ == "__main__":
    main()