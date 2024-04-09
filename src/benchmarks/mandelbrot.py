
def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = range(width)
    r2 = range(height)
    return [[mandelbrot(complex(xmin + (xmax - xmin) * x / width,
                               ymin + (ymax - ymin) * y / height), max_iter)
             for x in r1] for y in r2]

print(mandelbrot_set(-2.0, 1.0, -1.0, 1.0, 80, 24, 30)) 