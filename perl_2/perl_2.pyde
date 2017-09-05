def setup():
    global t
    size(800, 800)
    t = 0

def draw():
    colorMode(HSB)
    global t
    background(0)
    t += 0.003
    loadPixels()
    for x in range(width):
        y = int(noise(float(x) / float(width), t) * height)
        pixels[y * width + x] = color(map(y, 0, height, 0, 255), 255, 255)
    updatePixels()