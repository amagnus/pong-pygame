#!/usr/bin/python

import pygame


pygame.init()

display = pygame.display.set_mode((600, 400))

ball = pygame.Surface((10, 10))
ball.fill((255, 255, 255))

ball_rect = ball.get_rect()
ball_rect.center = (display.get_width()/2 - ball.get_width()/2,
					display.get_height()/2 - ball.get_height()/2)


player1 = pygame.Surface((5, 50))
player1.fill((255, 255, 255))

player1_rect = player1.get_rect()
player1_rect.center = (0, display.get_height()/2)


player2 = pygame.Surface((5, 50))
player2.fill((255, 255, 255))

player2_rect = player2.get_rect()
player2_rect.center = (display.get_width(), display.get_height()/2)


mytext = pygame.font.SysFont('verdana', 15)
label = mytext.render("Game over", 1, (255, 255, 0))

SPEED = 2
hei = 1
wid = 1
gameover = 0


while True:
	for x in pygame.event.get():
		if x.type == pygame.QUIT:
			exit()

		if pygame.event.event_name(x.type) == 'KeyDown':
			if x.key == pygame.K_UP:
				player1_rect.top -= 25
			if x.key == pygame.K_DOWN:
				player1_rect.top += 25


		# print pygame.event.event_name(x.type)

	#keys = pygame.key.get_pressed()
	#print keys 

	# if keys[K_UP]:
	#         player1_rect.top += 10

	# if keys[K_DOWN]:  
	#         player1_rect.top -= 10


	ball_rect.top += hei * SPEED
	ball_rect.right += wid * SPEED


	if ball_rect.bottom == display.get_height():
		hei = -1

	if ball_rect.top == 0:
		hei = 1

	if ball_rect.right == display.get_width():
		wid = -1
	#	gameover = 1

	if ball_rect.left == 0:
		gameover = 1

	if ball_rect.colliderect(player1_rect) == True:
		wid = 1
		



	display.fill((0, 0, 0))

	display.blit(ball, ball_rect)
	display.blit(player1, player1_rect)
	display.blit(player2, player2_rect)

	if gameover == 1:
		display.blit(label, (100, 100))

	pygame.display.update()
