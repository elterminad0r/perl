def setup():
    global t
    size(800, 800)
    t = 0

def draw():
    global t
    background(0)
    t += 0.003
    ellipse(width / 2, noise(t) * height, 100, 100)
