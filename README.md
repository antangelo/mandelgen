# mandelgen

This is a simple program that draws the Mandelbrot set

## Usage

`python3 mandelgen.py [-d width height] [-b xmax ymax] [-c xpos ypos] [-r resolution] [-o filename]`

The arguments, in order, are:

- The dimension of the generated image, in pixels (defaults to 1000x1000)
- The bounds of the complex plane (defaults to 2 by 2)
- The center of the plane (defaults to 0, 0)
- The maximum number of iterations to make on any given point (default 400)
- The output file for the picture. If one is not specified, the picture will be showed after completion
