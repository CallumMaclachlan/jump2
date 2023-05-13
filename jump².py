from tkinter import CENTER
import pygame
import sys
pygame.init()

WIDTH = 1100
HEIGHT = 800

def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score = pixel_font.render(f'Score : {current_time}', False, ("White"))
	score_rect= score.get_rect(center = (550, 50))
	screen.blit(score, score_rect)
	return current_time

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jump²')
screen.fill('Black')
clock = pygame.time.Clock()
pixel_font = pygame.font.Font("C:/Users/varan/Desktop/IT Portfolio/Code/jump2/pixel.ttf", 50)
small_pixel_font = pygame.font.Font("C:/Users/varan/Desktop/IT Portfolio/Code/jump2/pixel.ttf", 20)
big_pixel_font = pygame.font.Font("C:/Users/varan/Desktop/IT Portfolio/Code/jump2/pixel.ttf", 100)
game_active = False
start_time = 0
score = 0

player = pygame.Surface((50,50))
player_rect = player.get_rect(topleft =(100, 700))
player.fill('White')
player_gravity = 0

enemy = pygame.Surface((50,50))
enemy_rect = enemy.get_rect(topleft = (1100, 700))
enemy.fill('White')

bridge = pygame.Surface((1100, 10))
bridge.fill('White')

boarder = pygame.Surface((1100, 800))
boarder_rect = boarder.get_rect(topleft =(0, 0))
boarder.fill('Black')

title_surface = big_pixel_font.render('Jump', False, 'White')
title_rect = title_surface.get_rect(center = (525, 250))
title_squared = pixel_font.render('2', False, 'White')
title_squared_rect = title_squared.get_rect(center = (680, 215))
press_space = pixel_font.render('Press SPACE to Start', False, 'White')
press_space_rect = press_space.get_rect(center = (555, 400))




while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if game_active:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if boarder_rect.collidepoint(event.pos) and player_rect.bottom == 750:
					player_gravity = -20
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				enemy_rect.left = 1100
				start_time = int(pygame.time.get_ticks() / 1000)

	if game_active:
		screen.blit(boarder, boarder_rect)
		screen.blit(bridge, (0, 750))
		#'screen.blit(title_surface, (300,50))
		#screen.blit(score, score_rect)
		score = display_score()

		enemy_rect.x -= 4
		if enemy_rect.right <= 0:
			enemy_rect.left = 1100
		
		player_gravity += 1
		player_rect.y += player_gravity
		if player_rect.bottom >= 750: 
			player_rect.bottom = 750
		screen.blit(player, player_rect)
		screen.blit(enemy, enemy_rect)

		if player_rect.colliderect(enemy_rect):
			game_active = False
	else:
		screen.fill('Black')
		screen.blit(title_surface, title_rect) 
		screen.blit(title_squared, title_squared_rect)
		
		score_message= pixel_font.render(f'Your score: {score}', False, 'White')
		score_message_rect = score_message.get_rect(center = (550, 400))

		if score == 0:
			screen.blit(press_space, press_space_rect)
		else:
			screen.blit(score_message, score_message_rect)

	
	pygame.display.update()
	clock.tick(60)