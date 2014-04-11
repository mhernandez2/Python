import pygame
from pygame.draw import *
pygame.init()
x=int(raw_input("x ? "))
y=int(raw_input("y ? "))
tamanio = width, height = 400, 600
pantalla = pygame.display.set_mode(tamanio)
lado = 20


red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255, 200, 200)
lblue = (0, 255, 255)
yellow = (255, 255, 0)

#TETRAMINIOS

#Dibju de I
rect(pantalla, blue,[x+(lado*2),y,lado,lado])
rect(pantalla, blue,[x+(lado*2),y+(lado),lado,lado])
rect(pantalla, blue,[x+(lado*2),y+(lado*2),lado,lado])
rect(pantalla, blue,[x+(lado*2),y+(lado*3),lado,lado])

#Dibujo de O
rect(pantalla, red,[x+0,y+0,lado+lado,lado+lado])

#dibujo de Z
rect(pantalla, white,[x+(lado*3),y,lado,lado])
rect(pantalla, white,[x+(lado*4),y,lado,lado])
rect(pantalla, white,[x+(lado*4),y+lado,lado,lado])
rect(pantalla, white,[x+(lado*5),y+lado,lado,lado])

#dibujo de J
rect(pantalla, green,[x+(lado*6),y,lado,lado])
rect(pantalla, green,[x+(lado*6),y+lado,lado,lado])
rect(pantalla, green,[x+(lado*7),y+lado,lado,lado])
rect(pantalla, green,[x+(lado*8),y+lado,lado,lado])

#dibujo de L
rect(pantalla, pink,[x+(lado*9),y,lado,lado])
rect(pantalla, pink,[x+(lado*9),y+lado,lado,lado])
rect(pantalla, pink,[x+(lado*10),y,lado,lado])
rect(pantalla, pink,[x+(lado*11),y,lado,lado])

#dibujo de S
rect(pantalla, lblue,[x+(lado*13),y,lado,lado])
rect(pantalla, lblue,[x+(lado*14),y,lado,lado])
rect(pantalla, lblue,[x+(lado*13),y+lado,lado,lado])
rect(pantalla, lblue,[x+(lado*12),y+lado,lado,lado])

#dibujo de T
rect(pantalla, yellow,[x+(lado*16),y,lado,lado])
rect(pantalla, yellow,[x+(lado*15),y+lado,lado,lado])
rect(pantalla, yellow,[x+(lado*16),y+lado,lado,lado])
rect(pantalla, yellow,[x+(lado*17),y+lado,lado,lado])








pygame.display.flip()
raw_input("Press Enter to continue...")
