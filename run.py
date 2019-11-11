import pygame
from pygame.constants import *
from Boi import Boi
from DebugText import DebugText


settings = {
    "width": 800,
    "height": 450,
    "max_frame_rate": 60
}


def get_screen_size():
    return settings["width"], settings["height"]


pygame.init()
if not pygame.display.get_init():
    raise SystemError("Couldn't initialize the display")

background = pygame.display.set_mode(get_screen_size())

max_frame_rate = settings["max_frame_rate"]
boi = Boi()
debug_text = DebugText()
clock = pygame.time.Clock()
going = True
while going:
    dt = clock.tick(max_frame_rate)
    events = pygame.event.get()

    for e in events:
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            going = False

    pressed = pygame.key.get_pressed()
    if pressed[K_DOWN]:
        boi.move_down(dt)
    if pressed[K_UP] or pressed[K_SPACE]:
        boi.move_up(dt)
    if pressed[K_LEFT]:
        boi.move_left(dt)
    if pressed[K_RIGHT]:
        boi.move_right(dt)

    fps = 1000 / dt
    text = "FPS " + str(fps)
    debug_text.write(text)

    background.fill((0, 0, 0))
    boi.draw(background, dt)
    debug_text.write("X: " + str(boi.x))
    debug_text.write("sX: " + str(boi.speed_x))
    debug_text.write("Y: " + str(boi.y))
    debug_text.write("sY: " + str(boi.speed_y))

    debug_text.draw(background, dt)
    pygame.display.flip()
