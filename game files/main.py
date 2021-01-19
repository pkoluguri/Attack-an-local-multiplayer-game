import pygame
from pygame.locals import *
import math
import sys
import time
import os
pygame.init()
WIDTH = 800
HIEGHT = 650
MAX = 7
m = 10
FPS = 64
running = True
exits = 0
existss=0
bullet_movement = 15

screen = pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption("Attack!")
spaceship_1_img = pygame.image.load("spaceship.png")
spaceship_1_img = pygame.transform.rotate(spaceship_1_img,270)
spaceship_1_x = WIDTH/2-300
spaceship_1_y = HIEGHT/2
spaceship_1_health = 10
spaceship_2_health = 10
background_img = pygame.image.load("background.png")
font = pygame.font.Font('freesansbold.ttf',12)
spaceship_2_img = pygame.image.load("spaceship-2.png")
spaceship_2_img = pygame.transform.rotate(spaceship_2_img,90)
laser_img = pygame.image.load("laser.png")
laser_1_img = pygame.transform.rotate(laser_img,270)
laser_2_img = pygame.transform.rotate(laser_img,90)
spaceship_2_x = WIDTH/2+300
spaceship_2_y = HIEGHT/2
spaceship1_bullets_x = []
spaceship1_bullets_y = []
spaceship2_bullets_x = []
spaceship2_bullets_y = []
running1 = True

def draw_screen():
  global spaceship_1_x
  global spaceship_1_y
  global spaceship_2_x
  global spaceship_2_y
  screen.blit(background_img,(0,0))
  screen.blit(spaceship_1_img,(spaceship_1_x,spaceship_1_y))
  screen.blit(spaceship_2_img,(spaceship_2_x,spaceship_2_y))
  if len(spaceship1_bullets_x) > 0:
        for i in range(len(spaceship1_bullets_x)):
            screen.blit(laser_1_img,(spaceship1_bullets_x[i],spaceship1_bullets_y[i]))
  if len(spaceship2_bullets_x) > 0:
        for i in range(len(spaceship2_bullets_x)):
            screen.blit(laser_2_img,(spaceship2_bullets_x[i],spaceship2_bullets_y[i]))
  spaceship_1_text_health = font.render(f"Health:{spaceship_1_health}",True,(255,255,255)) 
  spaceship_1_name_text = font.render(f"{name1}",True,(255,255,255)) 
  screen.blit(spaceship_1_text_health,(spaceship_1_x,spaceship_1_y-40))
  screen.blit(spaceship_1_name_text,(spaceship_1_x,spaceship_1_y-20))
  spaceship_2_text_health = font.render(f"Health:{spaceship_2_health}",True,(255,255,255)) 
  spaceship_2_name_text = font.render(f"{name2}",True,(255,255,255))
  screen.blit(spaceship_2_text_health,(spaceship_2_x,spaceship_2_y-40))
  screen.blit(spaceship_2_name_text,(spaceship_2_x,spaceship_2_y-20))
  pygame.display.update()
def handle_spaceship_1_movement(key_pressed):
    global spaceship_1_y
    global spaceship_1_x
    if key_pressed[K_w] and spaceship_1_y-m > 0:
        spaceship_1_y -=  m
    if key_pressed[K_s] and spaceship_1_y+m < HIEGHT-60:
        spaceship_1_y += m
    if key_pressed[K_a] and spaceship_1_x-m > 0:
        spaceship_1_x -= m
    if key_pressed[K_d] and spaceship_1_x+m + 100 < WIDTH/2:
        spaceship_1_x += m
def handle_spaceship_2_movement(key_pressed):
    global spaceship_2_y
    global spaceship_2_x
    if key_pressed[K_UP] and spaceship_2_y-m > 0:
        spaceship_2_y -=  m
    if key_pressed[K_DOWN] and spaceship_2_y+m < HIEGHT-60:
        spaceship_2_y += m
    if key_pressed[K_LEFT] and spaceship_2_x-m > WIDTH/2:
        spaceship_2_x -= m
    if key_pressed[K_RIGHT] and spaceship_2_x+m+63 < WIDTH:
        spaceship_2_x += m
def is_collide(spaceship_bullet_x,spaceship_bullet_y,spaceship):
    if spaceship == 1:
        global spaceship_1_x
        global spaceship_1_y
        distance = math.sqrt(math.pow(spaceship_bullet_x-spaceship_1_x,2)+math.pow(spaceship_bullet_y-spaceship_1_y,2))
        if distance < 43:
            return True
        else:
            return False
    elif spaceship == 2:
        global spaceship_2_x
        global spaceship_2_y
        distance = math.sqrt(math.pow(spaceship_bullet_x-spaceship_2_x,2)+math.pow(spaceship_bullet_y-spaceship_2_y,2))
        if distance <= 40:
            return True
        else:
            return False

name1 = input("enter spacehip1's name (left spaceship):")
name2 = input("enter spaceship2's name (right spaceship):")
if os.name == "posix":
    print("left spaceship controls:\nmoving:w,a,s,d keys\nshooting:the left shift key")
    print("press enter to continue..")
    input()
    print("right spaceship controls:\nmoving:up,left,right and down arrows\nshooting:the right shift key")
    print("press enter to continue..")
    input()
    print("the game has started..")
elif os.name == "nt":
    print("left spaceship controls:\nmoving:w,a,s,d keys\nshooting:the left control key")
    print("press enter to continue..")
    input()
    print("right spaceship controls:\nmoving:up,left,right and down arrows\nshooting:the right contol key")
    print("press enter to continue..")
    input()
    print("the game has started..")

#main code here-
while running:
 for event in pygame.event.get():
     if event.type == QUIT:
         running = False
     if event.type == KEYDOWN:  
       if os.name == "posix":
         if event.key == K_LSHIFT and len(spaceship1_bullets_x) < MAX:
            spaceship1_bullets_x.append(spaceship_1_x)
            spaceship1_bullets_y.append(spaceship_1_y)
         if event.key == K_RSHIFT and len(spaceship2_bullets_x) < MAX:
            spaceship2_bullets_x.append(spaceship_2_x)
            spaceship2_bullets_y.append(spaceship_2_y)
       elif os.name == "nt":
           if event.key == K_LCTRL and len(spaceship1_bullets_x) < MAX:
            spaceship1_bullets_x.append(spaceship_1_x)
            spaceship1_bullets_y.append(spaceship_1_y)
           if event.key == K_RCTRL and len(spaceship2_bullets_x) < MAX:
            spaceship2_bullets_x.append(spaceship_2_x)
            spaceship2_bullets_y.append(spaceship_2_y)
 key_pressed = pygame.key.get_pressed()
 handle_spaceship_1_movement(key_pressed)
 handle_spaceship_2_movement(key_pressed)
 if len(spaceship1_bullets_x) > 0:
   try:
    for i in range(len(spaceship1_bullets_x)):
          if spaceship1_bullets_x[i]+1 < WIDTH:
            spaceship1_bullets_x[i] += bullet_movement
          else:
            spaceship1_bullets_x.pop(i)
            spaceship1_bullets_y.pop(i)
   except:
       pass
 if len(spaceship2_bullets_x) > 0:
    for i in range(len(spaceship2_bullets_x)):
        try:
            if spaceship2_bullets_x[i]+1 > 0:
                spaceship2_bullets_x[i] -=  bullet_movement
            else:
                spaceship2_bullets_x.pop(i)
                spaceship2_bullets_y.pop(i)
        except:
            pass
 if len(spaceship2_bullets_x) > 0:
  for i in range(len(spaceship2_bullets_x)):
        try:
            spaceship = 1
            collided = is_collide(spaceship2_bullets_x[i],spaceship2_bullets_y[i],spaceship)
            if spaceship_1_health != 0:
                if collided:
                    spaceship2_bullets_x.pop(i)
                    spaceship2_bullets_y.pop(i)
                    spaceship_1_health -= 1
                    print("spaceship1:",spaceship_1_health)
            else:
                spaceship = 2
                running_2 = True
                while running_2:
                 screen.fill((195, 55, 100))
                 font2 = pygame.font.Font("freesansbold.ttf",32)
                 font3 = pygame.font.Font("freesansbold.ttf",40)
                 game_over_text = font3.render(f"{name2} has won!!",True,(255,255,255))
                 screen.blit(game_over_text,(WIDTH/2-260,HIEGHT/2-100))
                 press_any_key = font2.render(f"press R to play again!!",True,(255,255,255))
                 screen.blit(press_any_key,(WIDTH/2-200,HIEGHT/2-50))
                 pygame.display.update()
                 for event in pygame.event.get():
                    if event.type == QUIT:
                        print("quitting...")
                        running = False
                        running_2 = False
                    if event.type == KEYDOWN:
                      if event.key == K_c or event.key == K_r:
                        spaceship_1_health = 10
                        spaceship_2_health = 10
                        spaceship1_bullets_x = []
                        spaceship1_bullets_y = []
                        spaceship2_bullets_x = []
                        spaceship2_bullets_y = []
                        running_2 = False
        except:
            pass
 clock = pygame.time.Clock()
 clock.tick(FPS)
 if len(spaceship1_bullets_x) > 0:
  try:
   for i in range(len(spaceship1_bullets_x)):
            spaceship = 2
            collided = is_collide(spaceship1_bullets_x[i],spaceship1_bullets_y[i],spaceship)
            if spaceship_2_health != 0:
             if collided:
                spaceship1_bullets_x.pop(i)
                spaceship1_bullets_y.pop(i)
                spaceship_2_health -= 1
                print("spaceship2:",spaceship_2_health)
            else:
                running_2 = True
                while running_2:
                 spaceship = 1
                 screen.fill((23, 241, 252))
                 font2 = pygame.font.Font("freesansbold.ttf",32)
                 game_over_text = font2.render(f"{name1} has won!!",True,(255,255,255))
                 screen.blit(game_over_text,(WIDTH/2-290,HIEGHT/2))
                 press_any_key = font2.render(f"press R to play again!!",True,(255,255,255))
                 screen.blit(press_any_key,(WIDTH/2-200,HIEGHT/2+50))
                 pygame.display.update()
                 for event in pygame.event.get():
                    if event.type == QUIT:
                        print("quitting...")
                        running = False
                        running_2 = False
                    if event.type == KEYDOWN:
                      if event.key == K_c or event.key == K_r:
                        spaceship_1_health = 10
                        spaceship_2_health = 10
                        spaceship1_bullets_x = []
                        spaceship1_bullets_y = []
                        spaceship2_bullets_x = []
                        spaceship2_bullets_y = []
                        running_2 = False
  except:
      pass
 draw_screen()
#finally done!!! took 9 hours!!!