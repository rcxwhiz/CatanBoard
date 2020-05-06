import pygame
import hex
import button

screen_size = (1600, 900)
tile_image_size = (170, 148)


def get_hex_positions():
	positions = []
	x = tile_image_size[0] / 2 + 10
	y_offset = tile_image_size[1] / 2
	while (x + tile_image_size[0] / 2) < screen_size[0] * 0.65:
		y = tile_image_size[1] / 2 + y_offset + 10
		while (y + tile_image_size[1] / 2) < screen_size[1]:
			positions.append((x, y))
			y += tile_image_size[1]
		x += tile_image_size[0] * 0.75
		if y_offset == 0:
			y_offset = tile_image_size[1] / 2
		else:
			y_offset = 0
	return positions


def main():
	pygame.init()

	game_font = pygame.font.SysFont('arial', 38)

	screen = pygame.display.set_mode(screen_size)

	hexes = pygame.sprite.Group()
	hex_positions = get_hex_positions()
	for position in hex_positions:
		new_hex = hex.Hex('add')
		new_hex.position(position[0], position[1])
		hexes.add(new_hex)
	hexes.sprites()[18].cycle_type(True)

	buttons_x = 990
	buttons_y = 70

	buttons = {}
	loop_x = 0
	for button_item in ['add-piece', 'edit-tiles', 'view-map', 'view-resources']:
		buttons[button_item] = button.Button(button_item, loop_x + buttons_x, buttons_y)
		loop_x += 170

	current_mode = 'view-map'
	while current_mode != 'quit':
		screen.fill((255, 255, 255))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				current_mode = 'quit'
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos

				for tile in hexes:
					if abs(x - tile.x) < 65 and abs(y - tile.y) < 70:
						if current_mode == 'edit-tiles' and tile.should_draw(current_mode):
							if event.button == 1:
								tile.cycle_type(True)
							elif event.button == 3:
								tile.cycle_type(False)
							elif event.button == 4:
								tile.increase_value()
							elif event.button == 5:
								tile.decrease_value()

				for button_item in buttons.keys():
					if buttons[button_item].rect.collidepoint(x, y):
						current_mode = button_item

		for tile in hexes:
			if tile.should_draw(current_mode):
				screen.blit(tile.surf, tile.rect)
				if tile.token != 0:
					if tile.token == 6 or tile.token == 8:
						text_surf = game_font.render(str(tile.token), True, (255, 0, 0))
					else:
						text_surf = game_font.render(str(tile.token), True, (0, 0, 0))
					text_rect = text_surf.get_rect()
					text_rect.center = (tile.x, tile.y)
					pygame.draw.circle(screen, (255, 255, 255), (round(tile.x), round(tile.y)), 35)
					screen.blit(text_surf, text_rect)

		for butt in buttons.values():
			screen.blit(butt.surf, butt.rect)
		pygame.display.flip()

	pygame.quit()


if __name__ == '__main__':
	main()
