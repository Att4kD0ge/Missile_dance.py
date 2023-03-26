import pygame
#Player

class Player:


    def __init__(self, pos, image, screen):
        global prect
        self.image = image
        self.x, self.y = pos
        self.size = self.image.get_size()
        self.player_rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.screen = screen


    def blitplayer(self):
        mouse_pos = pygame.mouse.get_pos()
        self.player_rect.center = mouse_pos
        self.screen.blit(self.image, self.player_rect)
