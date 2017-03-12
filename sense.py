from sense_hat import SenseHat
import time
import random
from random import randint
from time import sleep
import pygame
from pygame.locals import *
sense = SenseHat()
pygame.init()
pygame.display.set_mode((50,50))
running = True
EggRun = False
Selecting = True
SelectC = 255
FadeStage = 0
Choice = 0
def reset():
    global AA,BA,CA,AB,BB,CB,AC,BC,CC,MouseX,MouseY,Player,Direction,Egg1,Egg2,Egg3
    AA = 0
    BA = 0
    CA = 0
    AB = 0
    BB = 0
    CB = 0
    AC = 0
    BC = 0
    CC = 0
    MouseX = 1
    MouseY = 1
    Player = 1
    Direction = 2
    Egg1 = 1
    Egg2 = 0
    Egg3 = 0
def AllOn(R,G,B):
    X = (R,G,B)
    AllOn=[
      X, X, X, X, X, X, X, X, 
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      X, X, X, X, X, X, X, X,
      ]
    sense.set_pixels(AllOn)
def AllOff():
    AllOn(0,0,0)
def Column(X):
    A = 8
    while(A >= 1):
        A = A-1
        sense.set_pixel(X,A,[60,60,60])
def Row(Y):
    A = 8
    while(A >= 1):
        A = A-1
        sense.set_pixel(A,Y,[60,60,60])
def Bars():
    AllOff()
    Column(2)
    Column(5)
    Row(2)
    Row(5)
def Flash(R,G,B,T):
    AllOn(R,G,B)
    sleep(T)
    AllOff()
def Box(X,Y,C):
    sense.set_pixel(X*3,Y*3,C)
    sense.set_pixel(X*3+1,Y*3,C)
    sense.set_pixel(X*3,Y*3+1,C)
    sense.set_pixel(X*3+1,Y*3+1,C)
def ThreeText(A,B,C,TColour,BColour,Wait):
    sense.show_letter(A, text_colour=TColour, back_colour=BColour)
    sleep(Wait)
    sense.show_letter(B, text_colour=TColour, back_colour=BColour)
    sleep(Wait)
    sense.show_letter(C, text_colour=TColour, back_colour=BColour)
    sleep(Wait)
#C is colour. 1 is red 2 is green and 3 is blue 0 is fade off.
def Select(X,Y,C,Fade):
    A = 0
    if(C == 0):
        A = 255
        while(A >= 0):
            Box(X,Y,[A,A,A])
            sleep(0.0005)
            A = A-1
    if(C == 1):
        while(A <= 255):
            Box(X,Y,[A,0,0])
            sleep(0.0005)
            A = A+1
        if(Fade == True):
            A = 255
            while(A >= 0):
                Box(X,Y,[A,0,0])
                sleep(0.0005)
                A = A-1
    if(C == 2):
        while(A <= 255):
            Box(X,Y,[0,A,0])
            sleep(0.0005)
            A = A+1
        if(Fade == True):
            A = 255
            while(A >= 0):
                Box(X,Y,[0,A,0])
                sleep(0.0005)
                A = A-1
    if(C == 3):
        while(A <= 255):
            Box(X,Y,[0,0,A])
            sleep(0.0005)
            A = A+1
        if(Fade == True):
            A = 255
            while(A >= 0):
                Box(X,Y,[0,0,A])
                sleep(0.0005)
                A = A-1
def MouseBlink():
    A = 0
    while(A <= 255):
        Box(MouseX,MouseY,[0,A,0])
        sleep(0.001)
        A = A+1
    A = 255
    while(A >= 0):
        Box(MouseX,MouseY,[0,A,0])
        sleep(0.001)
        A = A-1
def Sweep(Tf):
    X = 0
    Y = 0
    while(Y <= 2):
        while(X <= 2):
            Select(X,Y,0,0)
            sleep(0.025)
            X = X+1
        X = 0
        Y = Y+1
    if(Tf):
        reset()
def MoveUp():
    global MouseX,MouseY,Player,Direction
    Direction = 1
    Continue = True
    while(Continue == True):
        MouseY = MouseY-1
        if(MouseY < 0):
            MouseY = 3
            MouseX = MouseX-1
            if(MouseX < 0):
                MouseX = 3
        if(Translate(MouseX,MouseY)):
            Continue = True
        if(Translate(MouseX,MouseY) == 0):
            Continue = False
def MoveRight():
    global MouseX,MouseY,Player,Direction
    Direction = 2
    Continue = True
    while(Continue == True):
        MouseX = MouseX+1
        if(MouseX >= 3):
            MouseX = 0
            MouseY = MouseY+1
            if(MouseY >= 3):
                MouseY = 0
        if(Translate(MouseX,MouseY)):
            Continue = True
        if(Translate(MouseX,MouseY) == 0):
            Continue = False
def MoveDown():
    global MouseX,MouseY,Player,Direction
    Direction = 3
    Continue = True
    while(Continue == True):
        MouseY = MouseY+1
        if(MouseY >= 3):
            MouseY = 0
            MouseX = MouseX+1
            if(MouseX >= 3):
                MouseX = 0
        if(Translate(MouseX,MouseY)):
            Continue = True
        if(Translate(MouseX,MouseY) == 0):
            Continue = False
def MoveLeft():
    global MouseX,MouseY,Player,Direction
    Direction = 4
    Continue = True
    while(Continue == True):
        MouseX = MouseX-1
        if(MouseX < 0):
            MouseX = 3
            MouseY = MouseY-1
            if(MouseY < 0):
                MouseY = 3
        if(Translate(MouseX,MouseY)):
            Continue = True
        if(Translate(MouseX,MouseY) == 0):
            Continue = False
def Translate(X,Y):
    global AA,BA,CA,AB,BB,CB,AC,BC,CC
    if(X == 0):
        if(Y == 0):
            return(AA)
        if(Y == 1):
            return(AB)
        if(Y == 2):
            return(AC)
    if(X == 1):
        if(Y == 0):
            return(BA)
        if(Y == 1):
            return(BB)
        if(Y == 2):
            return(BC)
    if(X == 2):
        if(Y == 0):
            return(CA)
        if(Y == 1):
            return(CB)
        if(Y == 2):
            return(CC)
def SetPlace():
    global MouseX,MouseY,Player,AA,BA,CA,AB,BB,CB,AC,BC,CC,Direction
    Select(MouseX,MouseY,Player,False)
    Ran = False
    if(MouseX == 0):
        if(MouseY == 0):
            AA = Player
        if(MouseY == 1):
            AB = Player
        if(MouseY == 2):
            AC = Player
    if(MouseX == 1):
        if(MouseY == 0):
            BA = Player
        if(MouseY == 1):
            BB = Player
        if(MouseY == 2):
            BC = Player
    if(MouseX == 2):
        if(MouseY == 0):
            CA = Player
        if(MouseY == 1):
            CB = Player
        if(MouseY == 2):
            CC = Player
    if(Direction == 1):
        MoveUp()
    if(Direction == 2):
        MoveRight()
    if(Direction == 3):
        MoveDown()
    if(Direction == 4):
        MoveLeft()            
    if(Player == 1):
        if(Ran == False):
            Player = 3
            Ran = True
    if(Player == 3):
        if(Ran == False):
            Player = 1
            Ran = True
def GameOver(Winner):
          sleep(10)
          Sweep(True)
def Egg():
    global EggRun,Egg1,Egg2,Egg3,Direction,Player
    if(EggRun == False):
        if(((Egg3 == 1) == (Egg2 == 3) == (Egg1 == 4) == (Direction == 2) == True)):
           Sweep(False)
           AllOff()
           A = 255
           while(A >= 0):
               AllOn(A,A,A)
               A = A-1
           if(Player == 1):
               sense.show_message("Made by FurryKitten",scroll_speed=0.05,text_colour=[255,0,0],back_colour=[0,0,0])
           if(Player == 3):
               sense.show_message("Made by FurryKitten",scroll_speed=0.05,text_colour=[0,0,255],back_colour=[0,0,0])               
           EggRun = True
           Bars()
           Repair()
    Egg3 = Egg2
    Egg2 = Egg1
    Egg1 = Direction
def Repair():
    A = 0
    B = 0
    while(B <= 3):
        while(A <= 3):
            Select(A,B,Translate(A,B),False)
            A = A+1
        B = B+1
        A = 0
def Menu(R,W,B):
    List=[
      R, R, R, R, R, R, R, W, 
      R, R, R, R, R, R, W, B,
      R, R, R, R, R, W, B, B,
      R, R, R, R, W, B, B, B,
      R, R, R, W, B, B, B, B,
      R, R, W, B, B, B, B, B,
      R, W, B, B, B, B, B, B,
      W, B, B, B, B, B, B, B,
      ]
    sense.set_pixels(List)
def Start():
    global Selecting
    if(Selecting == False):
        Flash(255,255,255,0.2)
        Bars()
        Sweep(True)
        Select(1,1,2,1)
    if(Selecting == True):
        Menu([255,0,0],[255,255,255],[0,0,255])
        sleep(0.2)
        Menu([255,0,0],[255,255,255],[0,0,0])
        AllOff()
        sleep(0.1)
        Menu([255,0,0],[255,255,255],[0,0,0])
#Game begins now
AllOn(255,255,255)
sleep(1)
A = 255
while(A >= 0):
    AllOn(255,A,A)
    A = A-1
ThreeText("T","i","c",[255,255,255],[255,0,0],0.5)
A = 255
B = 0
while(A >= 0):
    AllOn(A,B,0)
    A = A-1
    B = B+1
ThreeText("T","a","c",[255,255,255],[0,255,0],0.5)
A = 255
B = 0
while(A >= 0):
    AllOn(0,A,B)
    A = A-1
    B = B+1
ThreeText("T","o","e",[255,255,255],[0,0,255],0.5)
sleep(0.25)
A = 255
while(A >= 0):
    AllOn(0,0,A)
    A = A-1
Start()
while(running == True):
    for event in pygame.event.get():
        print(event)
        if(event.type == QUIT):
            running = False
            print("BYE")
        if(event.type == KEYDOWN):
            if(Selecting == True):
                if(event.key == K_RETURN):
                    print("ENTER")
                    Selecting = False
                    if(Choice == 0):
                        print("Game")
                        Start()
                    if(Choice == 1):
                        print("AI")
                if(event.key != K_RETURN):
                    if(Choice == 0):
                        Choice = 1
                    else:
                        Choice = 0
                    Flash(255,255,255,0.1)
                    SelectC = 255
                    FadeStage = 0
                    if(Choice == 0):
                        Menu([255,0,0],[255,255,255],[0,0,0])
                    if(Choice == 1):
                        Menu([0,0,0],[255,255,255],[0,0,255])
            else:
                if(event.key == K_RIGHT):
                    print("Right")
                    MoveRight()
                if(event.key == K_UP):
                    print("Up")
                    MoveUp()
                if(event.key == K_LEFT):
                    print("Left")
                    MoveLeft()
                if(event.key == K_DOWN):
                    print("Down")
                    MoveDown()
                if(event.key == K_RETURN):
                    print("Return")
                    SetPlace()
                Egg()
    if(Selecting == True):
        if(SelectC >= 255):
            FadeStage = 0
        if(SelectC <= 0):
            FadeStage = 1
        if(FadeStage == 0):
            SelectC = SelectC-1
            sleep(0.001)
        if(FadeStage == 1):
            SelectC = SelectC+1
            sleep(0.001)
        if(Choice == 0):
           Menu([SelectC,0,0],[255,255,255],[0,0,0])
        if(Choice == 1):
           Menu([0,0,0],[255,255,255],[0,0,SelectC])
    if(Selecting == False):
        MouseBlink()
