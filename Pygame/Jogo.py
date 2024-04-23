import pygame
from pygame.locals import *
from sys import *

pygame.init()

altura = 480
largura = 640

#criando a janela
tela = pygame.display.set_mode((largura, altura))

#Definir titulo da janela
pygame.display.set_caption("Criando Jogos")

while True:
    
    #colocando eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    #Atualizar o jogo a cada interação
    pygame.display.update()
    
    pygame.draw.rect(tela)