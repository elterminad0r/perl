def setup():
    global t
    size(800, 800)
    t = 0
    
BLOCK_SIZE = 8

def draw():
    colorMode(HSB, 255, 255, 255)
    global t
    t += 0.003
    noStroke()
    for x in range(0, width, BLOCK_SIZE):
        for y in range(0, height, BLOCK_SIZE):
            fill(noise(float(x) / float(width), float(y) / float(height), t) * 255, 255, 255)
            rect(x, y, BLOCK_SIZE, BLOCK_SIZE)