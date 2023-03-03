#!/usr/bin/env python
import pgzrun

WIDTH = 1000
HEIGHT = 500
TITLE = "郝芸霏"

c = 0


def draw():
    screen.fill((c, c, 0))


def update(dt):
    global c, HEIGHT
    c = (c + 1) % 256
    if c == 255:
        HEIGHT += 10


def on_mouse_down(button, pos):
    print("Mouse button", button, "clicked at", pos)


pgzrun.go()