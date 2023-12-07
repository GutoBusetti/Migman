import pygame
import random
from pygame.locals import *
from sys import exit

pygame.init()

x = 980
y = 500

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Migman')

icone = pygame.image.load('imagens/app.ico')
pygame.display.set_icon(icone)

saida = pygame.image.load('portas/saida.jpg').convert()
saida = pygame.transform.scale(saida, (x, y))

principal = pygame.image.load('portas/principal.jpg').convert()
principal = pygame.transform.scale(principal, (x, y))

init = pygame.image.load('imagens/init.jpg').convert()
init = pygame.transform.scale(init, (x, y))

configs = pygame.image.load('imagens/configs.jpg').convert()
configs = pygame.transform.scale(configs, (x, y))

susto0 = pygame.image.load('imagens/jumpscare/1.jpg').convert()
susto0 = pygame.transform.scale(susto0, (x, y))

susto2 = pygame.image.load('imagens/jumpscare/1.png').convert()
susto2 = pygame.transform.scale(susto2, (x, y))

susto3 = pygame.image.load('imagens/jumpscare/2.png').convert()
susto3 = pygame.transform.scale(susto3, (x, y))

vol = 0.8
pygame.mixer.music.set_volume(vol)
musica = pygame.mixer.music.load('audios/musica.mp3')
click = pygame.mixer.Sound('audios/click.wav')
jump = pygame.mixer.Sound('audios/jump.wav')
pygame.mixer.music.play(-1)

pp = tela.blit(init, (0,0))
pygame.display.flip()

pp = True

while True:
    for event in pygame.event.get():
     if event.type == QUIT:
      pygame.quit()
      exit()

    if event.type == KEYDOWN:
     if event.key == K_ESCAPE:
      pygame.quit()
      exit()

     if event.key == K_RETURN:
        pp = False
        click.play()
        pygame.mixer.music.stop()
        tela.blit(principal, (0,0))
        pygame.display.update()
      
     # if event.key == K_LCTRL:
      # if pp == False:
       #  jump.play()
        # tela.blit(susto, (0,0))
         # pygame.display.update()

     if pygame.mouse.get_pressed()[BUTTON_LEFT]:
       if pp == False:
        click.play()
        pr = tela.blit(principal, (0,0))
        pygame.display.flip()
        njump = random.randint(1, 50)
        if njump == 1:
          jump.play()
          pr == False
          tela.blit(susto2, (0,0))
          pygame.display.update()
        elif njump == 5:
          pr == False
          tela.blit(susto3, (0,0))
          pygame.display.update()
        else:
          print('none')
     if pygame.key.get_pressed()[K_RIGHT]:
       if pp == False:
        click.play()
        tela.blit(saida, (0,0))
        pygame.display.update()

     if event.key == K_TAB:
       if pp == True:
        tela.blit(configs, (0,0))
        pygame.display.update()
     if event.key == K_BACKSPACE:
      pp = True
      pygame.mixer.music.play()
      click.play()
      tela.blit(init, (0,0))
      pygame.display.update()
