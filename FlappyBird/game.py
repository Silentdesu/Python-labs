import pygame, random
from pygame.locals import *
import os

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 600
BACKGROUND_IMAGE = pygame.image.load("images/Background.png")
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))
SPEED = 10
GAME_SPEED = 10
GRAVITY_SCALE = 1

GROUND_WIDTH = 2 * WINDOW_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDTH = 120
PIPE_HEIGHT = 500
PIPE_GAP = 200

#Bird sprite
class Bird(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		self.speed = SPEED

		#Load and scale first sprite
		self.up_flap = pygame.image.load("images/UpFlap.png")
		self.up_flap = pygame.transform.scale(self.up_flap, (30, 21))

		#Load and scale second sprite
		self.mid_flap = pygame.image.load("images/MiddleFlap.png")
		self.mid_flap = pygame.transform.scale(self.mid_flap, (30, 21))

		#Load and scale third sprite
		self.down_flap = pygame.image.load("images/DownFlap.png")
		self.down_flap = pygame.transform.scale(self.down_flap, (30, 21))

		#List of sprites
		self.images = [self.up_flap,
					   self.mid_flap,
					   self.down_flap]


		self.current_image = 0

		self.image = self.up_flap
		self.mask = pygame.mask.from_surface(self.image)

		self.rect = self.image.get_rect()
		self.rect[0] = WINDOW_WIDTH / 2
		self.rect[1] = WINDOW_HEIGHT / 2

	def update(self):
		self.current_image = (self.current_image + 1) % 3
		self.image = self.images[self.current_image]
		
		self.speed += GRAVITY_SCALE

		#Update height
		self.rect[1] += self.speed

	def jump(self):
		self.speed = -SPEED

#Pipe sprite
class Pipe(pygame.sprite.Sprite):

	def __init__(self, inverted, xpos, ysize):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("images/Pipe.png")
		self.image = pygame.transform.scale(self.image, (PIPE_WIDTH, PIPE_HEIGHT))

		self.rect = self.image.get_rect()
		self.rect[0] = xpos

		if inverted:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect[1] = (self.rect[3] - ysize)
		else:
			self.rect[1] = WINDOW_HEIGHT - ysize
		
		self.mask = pygame.mask.from_surface(self.image)
	
	def update(self):
		self.rect[0] -= GAME_SPEED


#Ground sprite
class Ground(pygame.sprite.Sprite):

	def __init__(self, xpos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load("images/Ground.png")
		self.image = pygame.transform.scale(self.image, (GROUND_WIDTH, GROUND_HEIGHT))
		self.mask = pygame.mask.from_surface(self.image)
		
		self.rect = self.image.get_rect()
		self.rect[0] = xpos
		self.rect[1] = WINDOW_HEIGHT - GROUND_HEIGHT

	def update(self):
		self.rect[0] -= GAME_SPEED

def is_off_screen(sprite):
	return sprite.rect[0] < -(sprite.rect[2])

def get_random_spawn_pipes(xpos):
	size = random.randint(100, 300)
	pipe = Pipe(False, xpos, size)
	pipe_inverted = Pipe(True, xpos, WINDOW_HEIGHT - size - PIPE_GAP)
	return (pipe, pipe_inverted)

bird_group = pygame.sprite.Group()
ground_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()


bird = Bird()

for x in range(2):
	ground = Ground(GROUND_WIDTH * x)
	ground_group.add(ground)

for x in range(2):
	pipes = get_random_spawn_pipes(WINDOW_WIDTH * x + 600)
	pipe_group.add(pipes[0])
	pipe_group.add(pipes[1])

bird_group.add(bird)

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
	clock.tick(30)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()

		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				bird.jump()
	screen.blit(BACKGROUND_IMAGE, (0, 0))

	if is_off_screen(ground_group.sprites()[0]):
		ground_group.remove(ground_group.sprites()[0])

		nground = Ground(GROUND_WIDTH - 20)
		ground_group.add(nground)

	bird_group.update()
	ground_group.update()
	pipe_group.update()

	bird_group.draw(screen)
	ground_group.draw(screen)
	pipe_group.draw(screen)

	pygame.display.update()

	if pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask):
		input()
		break