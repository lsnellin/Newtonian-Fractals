"""
===========================================================================
Last Modified: 4-11-2024
By : Logan Snelling
Description : Contains classes for generating and storing fractals
===========================================================================
"""

import numpy as np
import pygame as pg

class NFractal:
    # Constructor :
    # poly : array of coefficients for polynomial
    # colors : array of pygame colors -> must be same length as poly
    # shading : Number of shades to texture the fractal with
    def __init__(self, poly : np.ndarray, colors : np.ndarray, shading : int, size : tuple) -> None:
        # Ensure that there is a color for each root :
        assert len(poly) == len(colors) , "Degree of polynomial doesn't match the number of colors!"
        assert len(size) == 2, "Size must be 2-dimensional!"
        
        # Initialize parameters
        self.roots = np.roots(poly)
        self.colors = colors
        self.shading = shading
        
        # Create an empty (width * height) array to store pixel data
        self.pixels = np.array([[None for i in range(size[0])] for j in range(size[1])])
    


def main():
    f = NFractal(
        poly = np.array([1,0,0,2,5]), # x^4 + 2x + 5
        colors = np.array([
            pg.Color('#D5B0AC'),
            pg.Color('#CEA0AE'),
            pg.Color('#684551'),
            pg.Color('#402E2A'),
            pg.Color('#9CD08F')
        ]),
        shading = 10,
        size = (3,2)
    )
    
    

if __name__ == '__main__':
    main()
