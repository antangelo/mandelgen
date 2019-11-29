from PIL import Image, ImageColor
from tqdm import trange

def compute_mandelbrot(point, resolution):
    z = 0
    for i in range(0, resolution):
        z = z * z + point
        if abs(z) > 2:
            return False, i

    return True, 0

def get_color(escapeval):
    return ImageColor.getrgb('hsl(%d, 100%%, 50%%)' % (escapeval % 240))

def gen_mandelbrot():
    height = 1000
    width = 1000
    xbound = 2.1
    ybound = 2.1
    xcenter = 0
    ycenter = 0
    resolution = 400

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
