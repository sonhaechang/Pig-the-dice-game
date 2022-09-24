from pygame.locals import *
import pygame
import random


pygame.init()
pygame.display.set_caption('Pig the dice game')

PLAYER_COUNT = 4

TOTOAL_SCORE = [0] * PLAYER_COUNT
COMPUTER_ROLL_COUNT = 0
PLAYER = 0
ROLLED
ROLLED = 0
MAX_SCORE = 100

IS_ACTIVE = True
IS_CLICK = False

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
THROW_START_Y = SCREEN_HEIGHT - 150

THROW_END_Y = 100
Y_CURR = SCREEN_HEIGHT / 2
DICE_CURR = 0

CLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def event_process():
	global IS_CLICK, IS_ACTIVE, DICE_CURR, ROLLED

	for event in pygame.event.get():
		if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or event.type == QUIT:
			IS_ACTIVE = False

		if (event.type == pygame.KEYDOWN and event.key == pygame.K_y):
			DICE_CURR = random.randint(0, len(dices)-1)
			ROLLED = DICE_CURR + 1
			score_count()

			if IS_CLICK == 0:
				IS_CLICK = 1

		if (event.type == pygame.KEYDOWN and event.key == pygame.K_n):
			change_turn()

def click_process():
	global IS_CLICK, DICE_CURR, Y_CURR

	if IS_CLICK == 1: # space bar & 위로 던질때
		Y_CURR -= 1
		if Y_CURR <= THROW_END_Y:
			IS_CLICK = 2
	elif IS_CLICK == 2: # 떨어질때
		Y_CURR += 1
		if Y_CURR >= THROW_START_Y:
			IS_CLICK = 0
	else: # 완료 및 아무것도 안할때
		set_text()
		Y_CURR = THROW_START_Y
		dices[DICE_CURR].rotate(angle=0)
		dices[DICE_CURR].draw()

	if IS_CLICK: # 던져지고 있을때
		dice_cur = random.randint(0, len(dices)-1)
		dices[dice_cur].y = Y_CURR
		dices[dice_cur].rotate()
		dices[dice_cur].draw()

def computer_process():
	global IS_CLICK

	if IS_CLICK == 0:
		IS_CLICK = 1

def change_turn():
	global PLAYER, PLAYER_COUNT
	PLAYER = (PLAYER + 1) % PLAYER_COUNT

def score_count():
	global IS_ACTIVE, MAX_SCORE, TOTOAL_SCORE, PLAYER, ROLLED

	if ROLLED == 1:
		# print('Result is 1, the turn passes to the next player.')
		TOTOAL_SCORE[PLAYER] = 0
		score = 0
		change_turn()
		# COMPUTER_ROLL_COUNT = 0
	else:
		score = TOTOAL_SCORE[PLAYER]
		score += ROLLED
		TOTOAL_SCORE[PLAYER] = score
		if TOTOAL_SCORE[PLAYER] >= MAX_SCORE:
			IS_ACTIVE = False

def set_text():
	global PLAYER, ROLLED, TOTOAL_SCORE

	m_font = pygame.font.SysFont('arial', 18)
	m_text = m_font.render(f'player {PLAYER+1}: your total_score is {TOTOAL_SCORE[PLAYER]} Rolling?', True, 'white')
	t_rec = m_text.get_rect()
	t_rec.centerx = SCREEN_WIDTH / 2
	t_rec.centery = t_rec.height + 40
	SCREEN.blit(m_text, t_rec)
	

class Dice():
	def __init__(self, idx, y):
		self.image = pygame.image.load(f'image/{idx}.png')
		self.image = pygame.transform.scale(self.image, (80, 80))
		self.x = (SCREEN_WIDTH / 2) - (self.image.get_width() / 2)
		self.y = y
		self.angle = 0
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)

	def rotate(self, angle=None):
		self.angle = 0 if angle != None else random.randint(0, 360)
		self.rotated_image = pygame.transform.rotate(self.image, self.angle)

	def draw(self):
		SCREEN.blit(self.rotated_image, (self.x, self.y))

dices = [Dice(i, THROW_START_Y) for i in range(1, 6+1)]

def main():
	bg = pygame.image.load('image/bg.png')
	bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

	while(IS_ACTIVE):
		SCREEN.fill((255, 255, 255))
		SCREEN.blit(bg, (10, 0))

		event_process()
		click_process()

		pygame.display.update()
		CLOCK.tick(100)

if __name__ == "__main__":
	main()