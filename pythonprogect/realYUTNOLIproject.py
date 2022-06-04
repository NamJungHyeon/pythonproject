import pygame as pg
import random as rd
import sys
from pygame.locals import *
from pygame.rect import *
from main import *
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

window = Tk()
window.geometry("1000x500")
window.title("YUT NOLI")
fontStyle = tkFont.Font(size=40)

def startYut():
    window.destroy()

def quit():
    sys.exit()

def GameRool():
    rool = Tk()
    rool.geometry("450x600")
    rool.title("YUT NOLI ROOL")
    lb1 = Label(rool,text="""윷놀이 규칙

    ① 윷이나 모가 나오면 한 번 더 던진다.

    ② 앞서가는 말을 잡을 수 있으며, 상대편 말을 잡으면 한 번 더 던진다.

    ③ 윷이나 모로 잡을 땐 두 번 던지지 않는다. 단, 윷이나 모가 나왔으므로 한 번 더 던진다.

    ④ 말은 두 동, 세 동, 네 동으로 동무하여 함께 갈 수 있다.

    ⑤ 윷을 위로 던지지 않고 굴리면 규칙에 어긋나며, 일정한 곳(예：멍석, 돗자리)을 벗어나면 무효이다.

    ⑥ 윷가락 하나에 표시를 하여 이것이 나오면 말밭을 물러나게 하는 등의 재미를 곁들일 수 있다.""",wraplength=300,font=fontStyle)
    lb1.pack()  
HwangTo = "C0A55A"

img =Image.open('Backgroundpicture.png')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x = -2,y = -2)
lb = Label(window,text="윷놀이 게임",font=("궁서체",80),background='#F0E68C')
lb.pack(anchor=CENTER)
btn1 = Button(window,command=startYut)
btn2 = Button(window,command=GameRool)
btn3 = Button(window,command=quit)

btn1.config(text="시작하기",width=30,height=3,bg="gray",fg="white")
btn2.config(text="게임 규칙",width=30,height=3,bg="gray",fg="white")
btn3.config(text="끝내기",width=30,height=3,bg="gray",fg="white")
btn1.place(x=390,y=250)
btn2.place(x=390,y=320)
btn3.place(x=390,y=390)
window.mainloop()

pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
SKIN = (235,200,160)

size = [1000,550]
screen = pg.display.set_mode(size)

BP = pg.image.load('Backgroundpicture.png')
pg.display.set_caption("YUT NOLi")
done = False
clock = pg.time.Clock()
Board = pg.image.load('Board.png')
ty = pg.image.load('throwyut.png')
LW= pg.image.load('lightwood.png')
bluechip1 = pg.image.load('bluechip.png')
bluechip2 = pg.image.load('bluechip.png')
bluechip3 = pg.image.load('bluechip.png')
redchip1 = pg.image.load('redchip.png')
redchip2 = pg.image.load('redchip.png')
redchip3 = pg.image.load('redchip.png')
yut = pg.image.load('yutnone.png')
onemore = pg.image.load('onemore.png')          
oneMore = 0
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
        fo3 = pg.font.SysFont('arial', 40, True, True)

        text1 = fo1.render("P1",False,BLACK)
        text2 = fo2.render("P2",False,BLUE)
        scme = fo3.render("게임을 시작합니다.",False,BLACK)

        screen.blit(text1,(630,10))  
        screen.blit(text2,(630,65))
        screen.blit(scme,(15,420))
        pg.draw.rect(screen,BLACK,[610,5,380,120],5)
        pg.draw.rect(screen,WHITE,[5,410,600,130])
        #pg.draw.rect(sex,BLACK,pg.Rect(610,430,CELL_SIZE1,CELL_SIZE2), 5)
        "pg.draw.rect(screen,BLACK,[610,430,380,110],5)"

        screen.blit(Board, (Board_x, Board_y))  #!#!#!# 추가 코드 #!#!#!#
        screen.blit(redchip1, (redchip1_x, redchip1_y))
        screen.blit(redchip2, (redchip2_x, redchip2_y))
        screen.blit(redchip3, (redchip3_x, redchip3_y))
        screen.blit(bluechip1,(bluechip1_x, bluechip1_y))
        screen.blit(bluechip2,(bluechip2_x, bluechip2_y))
        screen.blit(bluechip3,(bluechip3_x, bluechip3_y))
        screen.blit(ty,(610,430))
        screen.blit(LW,(610,125))
        
        event = pg.event.poll() #이벤트 처리


        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 698<x<739 and 19<y<58:
                        redchip1_x = 497
                        redchip1_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 761<x<798 and 19<y<58:
                        redchip2_x = 497
                        redchip2_y = 333
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 821<x<861 and 19<y<58:
                        redchip3_x = 497
                        redchip3_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 698<x<739 and 73<y<109:
                        bluechip1_x = 497
                        bluechip1_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 761<x<798 and 73<y<109:
                        bluechip2_x = 497
                        bluechip2_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 821<x<861 and 73<y<109:
                        bluechip3_x = 497
                        bluechip3_y = 333

        if event.type == pg.QUIT:
            break
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x = event.pos[0]
            y = event.pos[1]
            global yut,oneMore
            print(pg.mouse.get_pos())
            oneMore = 0
            if 610<x<990 and 430<y<540:
                cam = yutNol()
                if(cam=='모')or(cam=='윷'):
                    if(cam=='모'):
                        yut = pg.image.load('yutmo.png')
                        oneMore = 1
                    elif(cam=='윷'):
                        yut = pg.image.load('yutyut.png')
                        oneMore = 1

                elif(cam=='도'):
                    yut = pg.image.load('yutdo.png')

                elif(cam=='개'):
                    yut = pg.image.load('yutge.png')

                elif(cam=='걸'):
                    yut = pg.image.load('yutgirl.png')

                elif(cam=='빽도'):
                    yut = pg.image.load('yutbackdo.png')

                elif(cam=='낙'):
                    yut = pg.image.load('yutnone.png')
        
        screen.blit(yut,(720,210))
        if oneMore >= 1:
            screen.blit(onemore,(610,430))       
        else:
            screen.blit(ty,(610,430))
        pg.display.update()

runGame()
pg.quit()
