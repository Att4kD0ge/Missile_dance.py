import pygame


class Missile:
    def __init__(self, speed, image_path, start_pos):
        self.speed = speed
        self.image = pygame.image.load("Sprites/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.center = start_pos
        self.exploded = False

    def move(self):
        self.rect.move_ip(0, self.speed)

    def follow_player(self, player_pos):
        target_x = player_pos[0]
        current_x = self.rect.centerx
        if current_x < target_x:
            self.rect.move_ip(self.speed, 0)
        elif current_x > target_x:
            self.rect.move_ip(-self.speed, 0)

    def check_collision(self, player_rect):
        if not self.exploded and self.rect.colliderect(player_rect):
            self.exploded = True
            self.image = pygame.image.load("explosion.png")
            self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
