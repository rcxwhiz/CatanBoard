import pygame
import os

types = ['add', 'brick', 'desert', 'forest', 'gold', 'ocean', 'ore', 'sheep', 'wheat']
# excluded: blank, mystery

token_values = [0, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
token_weights = {0: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}


class Hex(pygame.sprite.Sprite):
	def __init__(self, hex_type):
		super(Hex, self).__init__()
		self.x = 0
		self.y = 0
		self.type = hex_type
		self.token = 0
		self.update_type()

	def update_type(self):
		self.surf = pygame.image.load(f'assets{os.sep}{self.type}-hex.png')
		self.rect = self.surf.get_rect()
		self.rect.center = (self.x, self.y)
		if self.type == 'add':
			self.token = 0

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
			if current_mode == 'edit-tiles':
				mouse_cords = pygame.mouse.get_pos()
				return abs(self.x - mouse_cords[0]) < 65 and abs(self.y - mouse_cords[1]) < 70
			else:
				return False
		else:
			return True

	def increase_value(self):
		self.token = token_values[(token_values.index(self.token) + 1) % len(token_values)]

	def decrease_value(self):
		self.token = token_values[token_values.index(self.token) - 1]
