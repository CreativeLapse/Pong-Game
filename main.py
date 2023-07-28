import pygame, sys
from pygame.locals import QUIT
from random import randint

pygame.init()

clock = pygame.time.Clock()
gravity = 0
angle = 0
score = 0

font = pygame.font.Font(None, 50)

paddlesurface = pygame.Surface((120, 10))
paddlesurface.fill('white')
paddlerect = paddlesurface.get_rect()

ballsurface = pygame.Surface((30, 30))
ballsurface.fill('white')
ballrect = ballsurface.get_rect()

backgroundsurface = pygame.Surface((800, 400))
backgroundsurface.fill('black')
backgroundrect = backgroundsurface.get_rect()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('PONG')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(backgroundsurface, ((0, 0)))

    scoresurface = font.render(f'{score}', False, 'white')
    screen.blit(scoresurface, ((100, 100)))
  
    paddlerect.x = (pygame.mouse.get_pos()[0])
    paddlerect.y = 380
    screen.blit(paddlesurface, paddlerect)
  
    gravity += 0.5
    angle = randint(-20, 20)
    if ballrect.x > 350:
      angle = randint(-20, 0)
    if ballrect.x < 50:
      angle = randint(0, 20)
    
    ballrect.x += angle
    ballrect.y += gravity
    
    if ballrect.colliderect(paddlerect):
      gravity = -15
      score += 1

    if not ballrect.colliderect(backgroundrect):
      score = 0
      gravity = 0
      ballrect.x = 400
      ballrect.y = 50
      
      
    screen.blit(ballsurface, ballrect)
  
    pygame.display.update()
    clock.tick(60)
