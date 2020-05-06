import pygame
import os

types = ['add', 'blank', 'brick', 'desert', 'forest', 'gold', 'mystery', 'ocean', 'ore', 'sheep', 'wheat']


class Hex(pygame.sprite.Sprite):
	def __init__(self, hex_type):
		super(Hex, self).__init__()
		self.x = 0
		self.y = 0
		self.type = hex_type
		self.update_type()

	def update_type(self):
		self.surf = pygame.image.load(f'assets{os.sep}{self.type}-hex.png')
		self.rect = self.surf.get_rect()
		self.rect.center = (self.x, self.y)

	def position(self, x, y):
		self.x = x
		self.y = y
		self.rect.center = (self.x, self.y)

	def change_type(self, new_type):
		self.type = new_type
		self.update_type()

	def cycle_type(self, direction):
		if direction:
			self.type = types[(types.index(self.type) + 1) % len(types)]
		else:
			self.type = types[types.index(self.type) - 1]
		self.update_type()

	def should_draw(self, current_mode):
		if self.type == 'add':
			if current_mode == 'add-piece':
				mouse_cords = pygame.mouse.get_pos()
				return abs(self.x - mouse_cords[0]) < 65 and abs(self.y - mouse_cords[1]) < 70
			else:
				return False
		else:
			return True
