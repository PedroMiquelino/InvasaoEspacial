import pygame
import random

pygame.init()

x=1280
y=700

screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('SpaceInvaders')

#carregar e reajustar a imagem 
sp = pygame.image.load('images/petpet.jpg').convert_alpha()
sp = pygame.transform.scale(sp, (x, y))

alien = pygame.image.load('images/dog.png').convert_alpha()
alien = pygame.transform.scale(alien, (97,97))#converte o tamanho dos aliens

pImg = pygame.image.load('images/gaga.png').convert_alpha()
pImg = pygame.transform.scale(pImg, (100,100)) #converte o tamanho da nave


missil = pygame.image.load('images/osso.png').convert_alpha()
missil = pygame.transform.scale(missil, (25,25)) #converte o tamanho do missil



pos_alien_x= 500
pos_alien_y= 360

pos_pImg_x= 200
pos_pImg_y= 300

vel_x_missil = 0
pos_missil_x = 200
pos_missil_y = 300

pontos = 10

triggered = False

rodando = True 

font = pygame.font.SysFont('fonts/game.ttf', 35)

player_rect = pImg.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()

#funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]
    
def respawn_missil():
   triggered = False
   respawn_missil_x = pos_pImg_x
   respawn_missil_y = pos_pImg_y
   vel_x_missil = 0
   return [respawn_missil_x, respawn_missil_y, triggered, vel_x_missil]
   
def colisão():
   global pontos
   if player_rect.colliderect(alien_rect) or alien_rect.x == 60:
      pontos -=1
      return True
   elif missil_rect.colliderect(alien_rect):
      pontos +=1
      return True
   else:
      return False
   


while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

#controle de fundo
    screen.blit(sp, (0,0))

    rel_x = x % sp.get_rect().width
    screen.blit(sp, (rel_x - sp.get_rect().width,0))
    if rel_x < 1280:
        screen.blit(sp, (rel_x,0))

#teclas    
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_pImg_y > 1:
        pos_pImg_y -= 1
        if not triggered:
         pos_missil_y -= 1


    if tecla[pygame.K_DOWN] and pos_pImg_y < 665:
        pos_pImg_y += 1

        if not triggered:
         pos_missil_y += 1

    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_missil = 2
#respawn
    if pos_alien_x == 50 or colisão():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x == 1300:
       pos_missil_x, pos_missil_y, triggered, vel_x_missil = respawn_missil()

    player_rect.y = pos_pImg_y
    player_rect.x = pos_pImg_x

    missil_rect.x = pos_missil_x
    missil_rect.y = pos_missil_y

    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y

#movimento
    x-=4
    pos_alien_x -=1   

    pos_missil_x += vel_x_missil 

    pygame.draw.rect(screen, (1, 0, 0), player_rect, 1)
    pygame.draw.rect(screen, (1, 0, 0), missil_rect, 1)
    pygame.draw.rect(screen, (1, 0, 0), alien_rect, 1)

    score = font.render(f' Pontos: {int(pontos)}', True, (0,0,0))
    screen.blit(score, (35,35))

#criar imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(pImg, (pos_pImg_x, pos_pImg_y))
    
    print(pontos)


    pygame.display.update()
