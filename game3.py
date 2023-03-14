#!/usr/bin/env python
import pgzrun

WIDTH = 1300
HEIGHT = 600
# NUM = 1
# balls = []
# for i in range(NUM):
ball = Actor("ball")
ball.x = 50 + 200
ball.y = 100
ball.dx = 10
ball.dy = 1
#     balls.append(ball)

ball2 = Actor("ball")
ball2.x = 20
ball2.y = 30
ball2.dx = 5
ball2.dy = 5


def draw():
    screen.fill((255, 255, 255))
    ball.draw()
    ball2.draw()
    # for ball in balls:
    #     ball.draw()


def update():
    # for ball in balls:
    ball.x += ball.dx
    ball.y += ball.dy
    if ball.right > WIDTH or ball.left < 0:
        ball.dx = -ball.dx
    if ball.bottom > HEIGHT or ball.top < 0:
        ball.dy = -ball.dy

    ball2.x += ball2.dx
    ball2.y += ball2.dy
    if ball2.right > WIDTH or ball2.left < 0:
        ball2.dx = -ball2.dx
    if ball2.bottom > HEIGHT or ball2.top < 0:
        ball2.dy = -ball2.dy


pgzrun.go()
