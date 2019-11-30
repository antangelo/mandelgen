from PIL import Image, ImageColor
from tqdm import trange
import argparse

def compute_mandelbrot(point, resolution):
    z = 0
    for i in range(0, resolution):
        z = z * z + point
        if abs(z) > 2:
            return False, i

    return True, 0

def get_color(escapeval):
    return ImageColor.getrgb('hsl(%d, 100%%, 50%%)' % (escapeval % 240))

def get_args():
    parser = argparse.ArgumentParser(description = "Produce image of Mandelbrot set")
    parser.add_argument('-d', '--dimension',dest = 'dim', 
            help = 'Dimension of generated image (width, height)', nargs = 2,
            default = ['1000', '1000'])
    parser.add_argument('-c', '--center', dest = 'center', nargs = 2,
            help = 'The center of the plane to graph (x, y)',
            default = ['0', '0'])
    parser.add_argument('-b', '--bound', dest = 'bound', nargs = 2,
            help = 'Bounds of the graph (x, y)',
            default = ['2', '2'])
    parser.add_argument('-r', '--resolution', dest = 'resolution',
            help = 'Max number of iterations for each point',
            default = '500')

    args = parser.parse_args()
    return int(args.dim[0]), int(args.dim[1]), float(args.center[0]), float(args.center[1]), float(args.bound[0]), float(args.bound[1]), int(args.resolution)

def gen_mandelbrot():
    width, height, xcenter, ycenter, xbound, ybound, resolution = get_args()

    xstep = 2 * xbound / width 
    ystep = 2 * ybound / height

    img = Image.new('RGBA', (width, height), "white")
    
    for x in trange(int(-width / 2), int(width / 2), desc = 'Progress', position=0):
        for y in range(int(-height / 2), int(height / 2)):
            # Must invert the y center to draw properly
            point = (xcenter + xstep * x) + (-ycenter + ystep * y) * 1j
            inset, escape = compute_mandelbrot(point, resolution)
            
            imgpoint = (int(width / 2 + x), int(height / 2 + y))

            if inset:
                img.putpixel(imgpoint, (0, 0, 0))
            else:
                img.putpixel(imgpoint, get_color(escape))

    img.show()

if __name__ == "__main__":
    gen_mandelbrot()
