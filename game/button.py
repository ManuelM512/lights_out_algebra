import pygame

from game.colors import DARK_GREEN, WHITE


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = DARK_GREEN
        self.font = pygame.font.SysFont(None, 35)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=15)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
