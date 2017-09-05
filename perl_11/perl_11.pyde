def setup():
    global t0, t1
    size(800, 800)
    t0 = 0
    t1 = random(500)

def draw():
    global t0, t1
    background(0)
    t0 += 0.003
    t1 += 0.003
    ellipse(noise(t0) * width, noise(t1) * height, 100, 100)