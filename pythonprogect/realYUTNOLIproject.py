import pygame as pg
import random as rd
import sys
from pygame.locals import *
from pygame.rect import *
import pyc
import time
from main import *

pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
SKIN = (235,200,160)
CELL_SIZE1 = 380
CELL_SIZE2 = 110

size = [1000,550]
screen = pg.display.set_mode(size)

BP = pg.image.load('Backgroundpicture.png')
pg.display.set_caption("YUT NOLi")
done = False
clock = pg.time.Clock()
Board = pg.image.load('Board.png')
LW= pg.image.load('lightwood.png')
bluechip1 = pg.image.load('bluechip.png')
bluechip2 = pg.image.load('bluechip.png')
bluechip3 = pg.image.load('bluechip.png')
redchip1 = pg.image.load('redchip.png')
redchip2 = pg.image.load('redchip.png')
redchip3 = pg.image.load('redchip.png')

yut = pg.image.load('yutmo.png')

def runGame():
    global done, Board, bluechip, redchip #!#!#!# 추가 코드 #!#!#!#
    Board_x = 0        #!#!#!# 추가 코드 #!#!#!#
    Board_y = 0        #!#!#!# 추가 코드 #!#!#!#
    redchip1_x = 700
    redchip1_y = 20
    redchip2_x = 760
    redchip2_y = 20
    redchip3_x = 820
    redchip3_y = 20
    bluechip1_x = 700
    bluechip1_y = 70
    bluechip2_x = 760
    bluechip2_y = 70
    bluechip3_x = 820
    bluechip3_y = 70

    while not done:
        screen.blit(BP,(0,0))
        clock.tick(10)
        fo1 = pg.font.SysFont('arial', 50, True, True)
        fo2 = pg.font.SysFont('arial', 50, True, True)
        text1 = fo1.render("P1",False,BLACK)
        text2 = fo2.render("P2",False,BLUE)
        screen.blit(text1,(630,10))  
        screen.blit(text2,(630,65))
        pg.draw.rect(screen,BLACK,[610,5,380,120],5)
        pg.draw.rect(screen,BLACK,[5,410,600,130],5)
        pg.draw.rect(screen,BLACK,pg.Rect(610,430,CELL_SIZE1,CELL_SIZE2), 5)
        "pg.draw.rect(screen,BLACK,[610,430,380,110],5)"


        for event in pg.event.get():
            if event.type == pg.QUIT:  # 게임 화면 종료
                done = True
        screen.blit(Board, (Board_x, Board_y))  #!#!#!# 추가 코드 #!#!#!#
        screen.blit(redchip1, (redchip1_x, redchip1_y))
        screen.blit(redchip2, (redchip2_x, redchip2_y))
        screen.blit(redchip3, (redchip3_x, redchip3_y))
        screen.blit(bluechip1,(bluechip1_x, bluechip1_y))
        screen.blit(bluechip2,(bluechip2_x, bluechip2_y))
        screen.blit(bluechip3,(bluechip3_x, bluechip3_y))
        screen.blit(LW,(610,125))
        
        event = pg.event.poll() #이벤트 처리
        if event.type == pg.QUIT:
            break
        elif event.type == pg.MOUSEBUTTONDOWN:
            global yut
            column_index = event.pos[0] 
            row_index = event.pos[1]
            cam = mainloop(1)  
            print('{}'.format(cam))
            if(cam=='모'):
                yut = pg.image.load('yutmo.png')

            elif(cam=='도'):
                yut = pg.image.load('yutdo.png')

            elif(cam=='개'):
                yut = pg.image.load('yutge.png')

            elif(cam=='걸'):
                yut = pg.image.load('yutgirl.png')

            elif(cam=='윷'):
                yut = pg.image.load('yutyut.png')

        screen.blit(yut,(720,210))        
        pg.display.update() 
"""
def throwyut(cam):
    if(cam == 0):
        yut1 = pg.image.load('yutmo.png')
        screen.blit(yut1,(630,300))
        pg.display.update()
    elif(cam==1):
        yut2 = pg.image.load('yutdo.png')
        screen.blit(yut2,(700,200))
        pg.display.update()
    elif(cam==2):
        yut3 = pg.image.load('yutge.png')
        screen.blit(yut3,(700,200))
        pg.display.update()
    elif(cam==3):
        yut4 = pg.image.load('yutgirl.png')
        screen.blit(yut4,(700,200))
        pg.display.update()
    elif(cam==4):
        yut5 = pg.image.load('yutyut.png')
        screen.blit(yut5,(700,200))
        pg.display.update()
"""
runGame()
"cam = main(1)"
pg.quit()
sys.exit()
