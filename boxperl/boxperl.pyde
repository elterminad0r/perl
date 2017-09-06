def setup():
    global t_a1, t_a2, t_a3, t_a4, t_x, t_y, t_z
    size(800, 800, P3D)
    t_a1, t_a2, t_a3, t_a4, t_x, t_y, t_z = (random(1) for _ in range(7))

def draw():
    global t_a1, t_a2, t_a3, t_a4, t_x, t_y, t_z
    t_a1 += 0.003
    t_a2 += 0.003
    t_a3 += 0.003
    t_a4 += 0.003
    t_x += 0.003
    t_y += 0.003
    t_z += 0.003

    background(0)
    lights()
    translate(noise(t_x) * 800, noise(t_y) * 800, noise(t_z) * 800)
    rotate(noise(t_a1) * TWO_PI, noise(t_a2) * TWO_PI, noise(t_a3) * TWO_PI, noise(t_a4) * TWO_PI)
    box(50)
