import pygame as pg
import sys
import random as rd

size_sc = 1366
size_scv = 768
n_pac = 200

size = int(size_sc/(n_pac))

cured = pg.Color("blue")
infected = pg.Color("red")
deceased = pg.Color("black")
normal = pg.Color("gray")

class Circle():

    def __init__(self):
        self.speedx = rd.randint(-7, 7)
        self.speedy  = rd.randint(-4, 4)
        self.x = rd.randint(0 + size, size_sc - size)
        self.y = rd.randint(0 + size, size_scv - size)
        self.color = normal
        self.speed = 1
        self.dead = False
        self.healed = False
        self.sick = False
        self.corona = rd.randint(0, 100)
        if self.corona == 50:
            self.sick = True
            self.coronaframecounter = 1
            self.color = infected
        else:
            self.coronaframecounter = 0


    def update(self):

        if self.speed < 0:
            self.speed = 1

        if self.x < size_sc:
            if self.x < 0:
                self.speedx = -self.speedx
        else:
            self.speedx = -self.speedx
        self.x = self.x + self.speedx

        if self.y < size_scv:
            if self.y < 0:
                self.speedy = -self.speedy
        else:
            self.speedy = - (self.speedy)
        self.y = self.y + self.speedy
        if self.sick == True:
            self.coronaframecounter += 1
            if self.coronaframecounter > 1000:
                self.corona = rd.randint(0, 100)
                if self.corona <= 4:
                    self.dead = True
                    self.color = deceased
                else:
                    self.healed = True
                    self.color = cured






circles = []



def render_circles(surface, circles):
    global size
    for circle in circles:
        circle.update()
        pg.draw.circle(surface, circle.color, (int(circle.x), int(circle.y)), size)

def init_circles(objects):
    global n_pac
    for i in range(n_pac):
        objects.append(Circle())

def main():

    pg.init()
    screen = pg.display.set_mode((size_sc, size_scv))
    clock = pg.time.Clock()
    init_circles(circles)


    while 1:

        pressed = pg.key.get_pressed()

        alt_held = pressed[pg.K_LALT] or pressed[pg.K_RALT]
        ctrl_held = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]

        for event in pg.event.get():

            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and ctrl_held:
                    return
                if event.key == pg.K_F4 and alt_held:
                    return
                if event.key == pg.K_ESCAPE:
                    return


            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click grows radius
                    for circle in circles:
                        circle.speedx = circle.speedx + 0.5
                        circle.speedy = circle.speedy + 0.5

                    #radius = min(200, radius + 1)
                elif event.button == 3:  # right click shrinks radius
                    for circle in circles:
                        circle.speedx = circle.speedx - 0.5
                        circle.speedy = circle.speedy - 0.5
                    #radius = max(1, radius - 1)



        screen.fill((0, 0, 0))

        render_circles(screen, circles)

        pg.display.flip()

        clock.tick(60)


main()
