#By: Magnus Crooke, Date Last Modified: 1-11-2018, File Name: unit11, This programs runs breakout
import ball
import paddle
import brick
import pygame
import time
import sys
from pygame.locals import *


def main():
    """
    This Function runs the breakout program as a whole.
    """
    FPS = 120
    fpsClock = pygame.time.Clock()
    pygame.init()
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    BRICK_HEIGHT = 8

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    paddleGroup = pygame.sprite.Group()
    bricksGroup = pygame.sprite.Group()
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("BREAKOUT")
    mainSurface.fill(WHITE)
    brick_x = 0
    brick_y = BRICK_Y_OFFSET
    color_list = (RED, ORANGE, YELLOW, GREEN, CYAN)
    draw_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    draw_ball.rect.x = 200
    draw_ball.rect.y = 350
    mainSurface.blit(draw_ball.image, draw_ball.rect)

    for color in color_list:
        for y in range(2):
            for x in range(BRICKS_PER_ROW):
                first_ROW = brick.Brick(BRICK_WIDTH, color)
                bricksGroup.add(first_ROW)
                first_ROW.rect.x = brick_x
                first_ROW.rect.y = brick_y
                mainSurface.blit(first_ROW.image, first_ROW.rect)
                brick_x = brick_x + (BRICK_SEP + BRICK_WIDTH)
            brick_x = 0
            brick_y = brick_y + BRICK_SEP + BRICK_HEIGHT
    paddle_pad = paddle.Paddle(BLACK)
    paddle_pad.rect.centerx = APPLICATION_WIDTH / 2
    paddle_pad.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(paddle_pad.image, paddle_pad.rect)
    paddleGroup.add(paddle_pad)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(WHITE)
        paddle_pad.move(pygame.mouse.get_pos())
        mainSurface.blit(paddle_pad.image, paddle_pad.rect)
        mainSurface.blit(draw_ball.image, draw_ball.rect)
        draw_ball.move()
        if draw_ball.rect.y > APPLICATION_HEIGHT:
            draw_ball.rect.y = APPLICATION_HEIGHT / 2
            draw_ball.rect.x = APPLICATION_WIDTH / 2
            mainSurface.blit(draw_ball.image, draw_ball.rect)
            pygame.time.wait(200)
            NUM_TURNS = NUM_TURNS - 1
        if NUM_TURNS == 0:
            pygame.mixer.music.load("Monster.mp3")
            mainSurface.fill(WHITE)
            pygame.mixer.music.play()
            myfont = pygame.font.SysFont('Helvetica', 30)
            textsurface = myfont.render("You Lose Bih!", False, BLACK)
            Textx = (APPLICATION_WIDTH / 2) - 60
            Texty = (APPLICATION_HEIGHT / 2) - 60
            mainSurface.blit(textsurface, (Textx, Texty))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        bricksprites = bricksGroup.sprites()
        if len(bricksGroup) == 0:
            pygame.mixer.music.load("horn.mp3")
            mainSurface.fill(WHITE)
            pygame.mixer.music.play()
            myfont = pygame.font.SysFont('Helvetica', 30)
            textsurface = myfont.render("You Win!", False, BLACK)
            Textx = (APPLICATION_WIDTH / 2) - 60
            Texty = (APPLICATION_HEIGHT / 2) - 60
            mainSurface.blit(textsurface, (Textx, Texty))
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit()
        draw_ball.collide_Ball(paddleGroup)
        draw_ball.collide_Bricks(bricksGroup)

        for blocks in bricksGroup:
            mainSurface.blit(blocks.image, blocks.rect)
        pygame.display.update()
        fpsClock.tick(FPS)

main()
