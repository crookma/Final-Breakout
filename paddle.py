import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        """
        This function creates a paddle for the ball to bounce off of.
        """
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.rectcolor = color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()

    def move(self, mouse):
        """
        This function moves the pabble with the mouse.
        :param mouse: uses the mouse to move the paddle.
        """
        self.rect.centerx = mouse[0]
