"""
===========================================================================
Last Modified: 4-11-2024
By : Logan Snelling
Description : Contains classes for generating and storing fractals
===========================================================================
"""

import numpy as np
import pygame as pg
from numba import jit
from tqdm import tqdm

class Fractal:
    # ===========================================================================
    # Constructor :
    # poly : array of coefficients for polynomial
    # colors : array of pygame colors -> must be same length as poly
    # shading : Number of shades to texture the fractal with
    # size : tuple of ints -> (width, height)
    # iterations : number of times to iterate before stopping Newton's method
    # tolerance : Minimum distance from root before method stops iterating
    # ===========================================================================
    def __init__(self, poly : np.ndarray, colors : np.ndarray, shades : int, size : tuple, iterations = 25, tolerance = 0.1) -> None:
        # Ensure that there is a color for each root :
        assert len(poly) == len(colors) , "Degree of polynomial doesn't match the number of colors!"
        assert len(size) == 2, "Size must be 2-dimensional!"
        
        # Initialize parameters
        self.roots = np.roots(poly)
        self.poly = poly
        self.derivative = np.polyder(poly)
        self.colors = colors
        self.shades = shades
        self.iterations = iterations
        self.tolerance = tolerance
        
        # Create an empty (width * height) array to store pixel data and another similar array to hold color values
        self.size = size
        self.generate_starting_points()
        
        self.pixel_colors = np.array([[None for i in range(size[0])] for j in range(size[1])])
    
    # ===========================================================================
    # Method : generate starting points
    # Generates a 2D array of complex numbers representing positions each pixel of the fractal scene
    # Formula:
    # Real = pixel_x - width  / 2
    # Imag = pixel_y - height / 2  
    #
    # Returns nothing
    # ===========================================================================
    def generate_starting_points(self) -> None:
        # Generate a 2D array of 
        x_offset = self.size[0] / 2
        y_offset = self.size[1] / 2
        self.positions = np.array([[[x - x_offset + 0j]for x in range(self.size[0])] for y in range(self.size[1])])
        self.positions.imag = np.array([[[y - y_offset]for x in range(self.size[0])] for y in range(self.size[1])])
        
    # ===========================================================================
    # Method : calculate_color
    # Given a location in the complex space, generate a color based off:
    # 1. Root Convergence -> Defines the RGB of the color
    # 2. Number of iterations until convergence -> scaling factor for RGB between 0.5 <-> 1.0
    #
    # Returns pygame Color object
    # ===========================================================================
    def calculate_color(self, position) -> pg.Color :
        for it in range(self.iterations):
            derivative = np.polyval(self.derivative, position)
            
            # Perform one iteration of Newton's method
            if derivative.real != 0 or derivative.imag != 0:
                position -= np.polyval(self.poly, position) / derivative
            else:
                break
            
            # Check for convergence
            for i, root in enumerate(self.roots):
                offset = position - root
                if abs(offset.real) <= self.tolerance and abs(offset.imag) <= self.tolerance:
                    # Calculate based off root and # iterations
                    s = 0.5 + (it % self.shades) / (self.shades * 2)
                    return pg.Color(
                       int(self.colors[i][0] * s),
                       int(self.colors[i][1] * s),
                       int(self.colors[i][2] * s)
                    )
        
        # If the position didn't converge after given number of iterations, return color white
        return pg.Color('#ffffff')
    
    # ===========================================================================
    # Method : generate
    # Generates the color map of the fractal
    # ===========================================================================
    #@jit(nopython = True)
    def generate(self):
        for i in tqdm(range(len(self.positions))):
            for j, position in enumerate(self.positions[i]):
                self.pixel_colors[i][j] = self.calculate_color(position)
    
                      



