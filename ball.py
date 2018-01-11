import pygame


class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        """
        This function creates the ball.
        :param color: The color of the ball.
        :param windowWidth: Gets where the ball will spawn width wise.
        :param windowHeight: Gets where the ball will spawn height wise.
        """
        super().__init__()
        self.RADIUS = 10
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.color = color
        self.image = pygame.Surface((self.RADIUS, self.RADIUS))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.vx = 5
        self.vy = 9
        pygame.mixer.music.load("punch.mp3")

    def move(self):
        """
        This function reflects the ball off of the walls.
        """
        self.rect.top = self.rect.top + self.vy
        self.rect.left = self.rect.left + self.vx
        if self.rect.bottom < 0:
            self.vy = -self.vy
        if self.rect.left < 0:
            self.vx = -self.vx
        if self.rect.right > self.windowWidth:
            self.vx = -self.vx

    def collide_Bricks(self, spriteGroup):
        """
        This function bounces the ball back off of the brick after colliding with a brick.
        """
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.vy = -self.vy
            pygame.mixer.music.play()

    def collide_Ball(self, spriteGroup):
        """
        This function bounces the ball back off of the brick after colliding with a brick.
        """
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.vy = -self.vy
