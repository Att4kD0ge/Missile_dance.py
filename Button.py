import pygame

#Button
class Button:


    def __init__(self, pos, image, screen):
        self.buttonfeedback = 0
        self.buttonimage = image
        self.x, self.y = pos
        self.size = self.buttonimage.get_size()
        self.rect = self.buttonimage.get_rect()
        self.surface = pygame.Surface(self.size)
        self.screen = screen


    def show(self):
        self.screen.blit(self.buttonimage, (self.x, self.y))


    def click(self, event):
        global buttonfeedback
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                print("pressed")
                print(type(self.rect.collidepoint(x, y)))
                print(self.rect.collidepoint(x, y))
                if not self.rect.collidepoint(x, y):
                    print("Clicked")
                    self.set_value()


    def set_value(self):
        self.buttonfeedback = 1

    def get_value(self):
        return self.buttonfeedback





