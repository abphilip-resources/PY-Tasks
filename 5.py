import sys
from PIL import Image

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'

    def __str__(self):
        return repr(self)

class bp:
    def __init__(self, energy, prev=None):
        self.energy = energy
        self.prev = prev

def vertical(data):
    g = [[None for _ in row] for row in data]
    h = len(data)
    w = len(data[0])
    for x in range(w):
        g[0][x] = bp(data[0][x])

    for y in range(1, h):
        for x in range(w):
            a = x - 1 if x > 0 else 0
            b = x + 1 if x < w - 1 else w - 1
            p = min(range(a, b + 1), key=lambda x: g[y - 1][x].energy)
            g[y][x] = bp(data[y][x] + g[y - 1][p].energy, p)

    m = min(enumerate(g[h - 1]), key=lambda m: m[1].energy)[0]
    xs, lx = [], m
    for y in range(h - 1, -1, -1):
        xs.append(lx)
        lx = g[y][lx].prev
    xs.reverse()
    return (xs, g[-1][m].energy)

def read(file):
    img = Image.open(file, 'r')
    w, h = img.size
    px = list(Color(*pixel) for pixel in img.getdata())
    return [px[n:(n + w)] for n in range(0, w * h, w)]

def write(px, file):
    h = len(px)
    w = len(px[0])
    img = Image.new('RGB', (w, h))
    o = img.load()
    for y, row in enumerate(px):
        for x, color in enumerate(row):
            o[x, y] = (color.r, color.g, color.b)
    img.save(file)

def at(px, x, y):
    h = len(px)
    w = len(px[0])

    x0 = x if x == 0 else x - 1
    x1 = x if x == w - 1 else x + 1
    dxr = px[y][x0].r - px[y][x1].r
    dxg = px[y][x0].g - px[y][x1].g
    dxb = px[y][x0].b - px[y][x1].b

    y0 = y if y == 0 else y - 1
    y1 = y if y == h - 1 else y + 1
    dyr = px[y0][x].r - px[y1][x].r
    dyg = px[y0][x].g - px[y1][x].g
    dyb = px[y0][x].b - px[y1][x].b

    dx = dxr * dxr + dxg * dxg + dxb * dxb
    dy = dyr * dyr + dyg * dyg + dyb * dyb
    return dx + dy

def calculate(px):
    e = [[0 for _ in row] for row in px]
    for y, row in enumerate(px):
        for x, _ in enumerate(row):
            e[y][x] = at(px, x, y)
    return e

def rm(img, n):
    for i in range(n):
        print(f'Removing seam {i + 1}/{n}')
        xs, _ = vertical(calculate(img))
        img = [[p for x, p in enumerate(row) if x != xs[y]] 
                  for y, row in enumerate(img)]
    return img

if len(sys.argv) != 4:
    print(f'USAGE: {__file__} <input> <num-seams-to-remove> <output>')
    sys.exit(1) 
write(rm(read(sys.argv[1]), int(sys.argv[2])), sys.argv[3])