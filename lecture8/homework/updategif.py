from random import randint
import pygame
import random

WIDTH_DISPLAY=900
HEIGHT_DISPLAY=600
WHITE_COLOR = (255, 255, 255)  
ORANGE_COLOR = (255, 150, 100)
BLACK_COLOR = (0,0,0)
 

COORD_X=50
COORD_Y=50
WIDTH_RECTANGLE=150
HEIGHT_RECTANGLE=124
DELTA_STEP=9

width_meteor = 60
height_meteor = 40

screen = pygame.display.set_mode([WIDTH_DISPLAY,HEIGHT_DISPLAY], pygame.RESIZABLE)

pygame.display.set_caption('Fly&Get')
clock = pygame.time.Clock()

pygame.display.update()

background_position = [0,0]
player_image = pygame.image.load(r'C:\Users\adm.a.danyliuk\Desktop\softserve\lecture8\homework\fly.png').convert()
METEORS=('C:/Users/adm.a.danyliuk/Desktop/softserve/lecture8/homework/meteor2.png', 'C:/Users/adm.a.danyliuk/Desktop/softserve/lecture8/homework/meteor.png', 'C:/Users/adm.a.danyliuk/Desktop/softserve/lecture8/homework/meteor8.png')#список изображений
METEORS_SURF=[]
bg = pygame.image.load(r'C:\Users\adm.a.danyliuk\Desktop\softserve\lecture8\homework\bg.jpg')
player_image.set_colorkey(BLACK_COLOR)
#meteor.set_colorkey(BLACK_COLOR)
for i in range(len(METEORS)):
    METEORS_SURF.append(pygame.image.load(METEORS[i]).convert())


def draw_window():
    '''Function draw window and image player'''
    screen.blit(bg, (0, 0))

    screen.blit(player_image, [COORD_X, COORD_Y, WIDTH_RECTANGLE,  HEIGHT_RECTANGLE])
    
    
    meteors.draw(screen)
    #HOMEWORK
    pygame.display.flip()
    
class Meteor(pygame.sprite.Sprite):
     
    def __init__(self,x,surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image=surf
        self.rect=self.image.get_rect(center=(x,0))
        self.add(group)
        self.speed=(randint(4,10))
        self.image.set_colorkey((0,0,0))
    def update(self):
        if self.rect.y < WIDTH_DISPLAY:
            self.rect.y+=self.speed
        else:
            self.kill
meteors = pygame.sprite.Group()
Meteor(randint(25,WIDTH_DISPLAY-25), METEORS_SURF[0],meteors)#створення першого метеориту,спрайту

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and COORD_X>DELTA_STEP:
        COORD_X=COORD_X-DELTA_STEP
    if keys[pygame.K_RIGHT] and COORD_X<WIDTH_DISPLAY-WIDTH_RECTANGLE-DELTA_STEP:
        COORD_X=COORD_X+DELTA_STEP
    if keys[pygame.K_UP] and COORD_Y>DELTA_STEP:
        COORD_Y=COORD_Y-DELTA_STEP
    if keys[pygame.K_DOWN] and COORD_Y<HEIGHT_DISPLAY-HEIGHT_RECTANGLE-DELTA_STEP:
        COORD_Y=COORD_Y+DELTA_STEP

    draw_window()
    clock.tick(60)
    
pygame.quit()