from .. components import info
import pygame

class Load_Screen:
    def __init__(self):
        self.finshed = False
        self.next = 'level'
        self.timer = 0
        self.info = info.Info('load_screen')

    def update(self, surface, keys):
        self.draw(surface)
        if self.timer == 0:
            self.timer = pygame.time.get_ticks()
        elif pygame.time.get_ticks() - self.timer > 2000:
            self.finshed = True
            self.timer = 0

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.info.draw(surface)