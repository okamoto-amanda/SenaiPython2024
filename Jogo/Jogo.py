import pygame
from pygame.locals import *
from sys import *

from random import *


pygame.init()

altura = 480
largura = 640
pos_x = largura / 2
pos_y = altura /2
largura_retangulo = 30
altura_retangulo = 40
#Definindo tamanho e posicao do circulo

posXCirculo = 40
posYCirculo = 10
raioCirculo = 10

#criando a janela
tela = pygame.display.set_mode((largura, altura))

#Definir titulo da janela
pygame.display.set_caption("Criando Jogos")

#Modificar a taxa de pixel por segundo
relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    #tela.fill((0,0,0))
    mensagem = f'pontos: {pontos}'
    textoFormatado = fonte.render(mensagem, True,(255,255,255))
    #colocando eventos
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN:
            if  event.key == K_UP:
                pos_y += 10
            
            if event.key == K_DOWN:
                pos_y -= 10
                
            if event.key == K_LEFT:
                pos_x -= 10
            
            if event.key == K_RIGHT:
                pos_x += 10
    
    if pygame.key.get_pressed()[K_UP]:    
        pos_y += 10
    elif pygame.key.get_pressed()[K_DOWN]:    
        pos_y -= 10
    elif pygame.key.get_pressed()[K_RIGHT]:    
        pos_x += 10
    elif pygame.key.get_pressed()[K_LEFT]:    
        pos_x -= 10
            
    
    #Atualizar o jogo a cada interação
    pygame.display.update()
    
    retangulo = pygame.draw.rect(tela, (0,255,0),(pos_x, pos_y,largura_retangulo, altura_retangulo))
    
    circulo = pygame.draw.circle(tela, (255,0,255),(posXCirculo, posYCirculo), raioCirculo)
    
    if retangulo.colliderect(circulo):
        posXCirculo = randint(40,60)
        posYCirculo = randint(50,430)
        raioCirculo = 10
    
    tela.blit(textoFormatado, (400,40))
    #Definindo fonte    
    
    fonte = pygame.font.sysfont("Arial", 20, True)