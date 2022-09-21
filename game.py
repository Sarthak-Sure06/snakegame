from tarfile import LENGTH_LINK
from tkinter import font
from turtle import width
import pygame
import random

pygame.init()
width = 600
height = 400
dis = pygame.display.set_mode((width,height))
pygame.display.update()
red = (128,0,0)
black = (0,0,0)
white = (255,255,255)
dis.fill(white)
game_over = False
x1 = 300
y1 = 200
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
game_close = False

font_style = pygame.font.SysFont("freesans",30)
lost = font_style.render("you lost",True,red)


def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,red,(x[0],x[1],snake_block,snake_block))


def thescore(score):
    value = font_style.render("your score" + " " + str(score) ,True , red)
    dis.blit(value,[0,0])

def game_loop():
    game_over = False
    game_close = False
    x1 = int(width/2)
    y1 = int(height/2)
    x1_change = 0
    y1_change = 0
    eatx = 10*random.randint(0,59)
    eaty = 10*random.randint(0,39)

    snake_list = []
    length_of_snake = 1

    while(game_over == False):
        
        while(game_close == True):
            dis.fill(white)
            dis.blit(lost,[250,100])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False 
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False 

                    if event.key == pygame.K_p:
                        game_loop()    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -10

                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = 10

                elif event.key == pygame.K_d:
                    x1_change = 10
                    y1_change = 0

                elif event.key == pygame.K_a:  
                    x1_change = -10
                    y1_change = 0      

        
        if x1>=width or x1<0 or y1>=height or y1<0:
            game_close = True
        x1 = x1+x1_change
        y1 = y1+y1_change
        dis.fill(white)   

        #pygame.draw.rect(dis,red,(x,y,15,15)) 
        pygame.draw.rect(dis,black,(eatx,eaty,15,15))
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>length_of_snake:
            del snake_list[0]

        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True

        our_snake(15,snake_list)
        if x1 == eatx and y1 == eaty:
            length_of_snake += 1
            eatx = 10*random.randint(0,59)
            eaty = 10*random.randint(0,39)
        thescore(length_of_snake - 1)
        pygame.display.update() 
        clock.tick(20)  

    pygame.quit() 
game_loop()       