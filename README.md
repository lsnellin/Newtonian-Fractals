# Newtonian Fractal Rendering Engine
This project creates videos zooming in on dynamic Newtonian Fractals. Newtonian Fractals are generated by given a polynomial using Newton's method to find the roots of the polynomial. 

## Newtonian Fractal Background
- Newton's method for finding roots of the polynomial involves using a starting value, and following the tanget line at that point to the x-axis. The x value where the tangent line intersects the x-axis is the new x value. This process is repeated until the x value is arbitrarily close to a given root
- Interestingly, this process does not always have well defined behaviour. Points that start very close together can diverge far apart, then converge on different roots. In fact, if you examine the boundary in space where starting points converge to different roots, you'll find that it is not smooth for polynomials of degree > 2.
- Using complex numbers as starting points, we can plot the real component on the x-axis, and the imaginary component on the y-axis. We then color each point by the root that it converges to under some number of iterations. The resulting color map will be a fractal
- For more information visit : https://en.wikipedia.org/wiki/Newton_fractal

## Program Function


## Inputs + Dynamic Generation
The user may define the following parameters for their fractal:
- Polynomial of degree $k$
- $k$ colors corresponding to each root of the polynomial
- Fractal zoom-in speed
- Video length
- Shading parameter, $s$ which determines the smoothness of the texture of the fractal

## Outputs
- A %fractalname.mp4 file of the specified length which zooms in on the newtonian fractal generated by the given polynomial.

