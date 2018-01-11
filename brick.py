import pygame


class Block(pygame.sprite.Sprite):
    pygame.init()


class Brick(pygame.sprite.Sprite):
    def __init__(self, width, color):
        """
        This Function creates each brick individually
        :param width: How wide the brick is.
        :param color: The color that the brick is going to be.
        """
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.BRICK_WIDTH = width
        self.BRICK_COLOR = color
        self.image = pygame.Surface((width, self.BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()
