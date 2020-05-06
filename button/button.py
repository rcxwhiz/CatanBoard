import pygame
import os


class Button(pygame.sprite.Sprite):
	def __init__(self, button_type, x, y):
		super(Button, self).__init__()
		self.x = 0
		self.y = 0
		self.button_type = button_type
		self.surf = pygame.image.load(f'assets{os.sep}{self.button_type}.png')
		self.rect = self.surf.get_rect()
		self.x = x
		self.y = y
		self.rect.center = (self.x, self.y)
