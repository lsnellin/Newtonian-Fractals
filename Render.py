import numpy as np
import pygame as pg
import sys
from NFractal import Fractal


def main():
    f = Fractal(
        poly = np.array([1, 0, 0, 5]), # x^4 + 2x + 5
        colors = np.array([
            pg.Color('#00635D'),
            pg.Color('#01172F'),
            pg.Color('#AF125A'),
            pg.Color('#C09BD8')
        ]),
        shades = 10,
        size = (400,400)
    )
    
    f.generate()
    
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((f.size[1], f.size[0]))

    while True:
        #Poll for events
        for event in pg.event.get():
            #Click X
            if event.type == pg.QUIT:
                sys.exit()
        
        pg.display.flip()
        
        #Draw the screen
        screen.fill(pg.Color('#fafafa'))
        renderFractal(screen, f)
        pg.image.save(screen, 'screenshot.png')
        break

        
        clock.tick(1)
    
def renderFractal(screen : pg.Surface, f : Fractal):
    for i, row in enumerate(f.pixel_colors):
        for j, color in enumerate(row):
            screen.set_at((i, j), color)
    
if __name__ == '__main__':
    main()