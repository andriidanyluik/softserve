from random import randint
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)# раз в 2 сек
W = 959
H = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HEIGTH_ROCKET = 100
 
sc = pygame.display.set_mode((W, H))
fireboll=('C:/Users/Andrii/Desktop/softserve/lecture8/homework/fireboll.png')
bg = pygame.image.load('C:/Users/Andrii/Desktop/softserve/lecture8/homework/bg2.png')
METEORS=('C:/Users/Andrii/Desktop/softserve/lecture8/homework/meteor2.png', 'C:/Users/Andrii/Desktop/softserve/lecture8/homework/meteor.png', 'C:/Users/Andrii/Desktop/softserve/lecture8/homework/meteor8.png')#список изображений
METEORS_SURF=[]
PILOTS =('C:/Users/Andrii/Desktop/softserve/lecture8/homework/fly.png','C:/Users/Andrii/Desktop/softserve/lecture8/homework/fly.png','C:/Users/Andrii/Desktop/softserve/lecture8/homework/fly.png')
PILOTS_SURF = []
bullets=[]
font = pygame.font.Font(pygame.font.match_font('dejavusans'), 36)
text1 = font.render('Game over', 1, (180,0,0))
for i in range(len(METEORS)):
    METEORS_SURF.append(pygame.image.load(METEORS[i]).convert())
for i in range(len(PILOTS)):
    PILOTS_SURF.append(pygame.image.load(PILOTS[i]).convert())


def drawing():
    '''function drowing window meteors and rocket'''
    sc.fill(BLACK)
    sc.blit(bg,(0,0))
    meteors.draw(sc)#вималювати поверх
    sc.blit(fly.image, fly.rect)#вималювати поверх
    pygame.display.update()#оновити
    pygame.time.delay(20)
    meteors.update()

class Meteor(pygame.sprite.Sprite):#класс метеоритів 
    def __init__(self, x, surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.add(group)
        self.speed=(randint(1,10))
        self.image.set_colorkey((0,0,0))
    def update(self):#оновлення властивостей класу за його межами
        if self.rect.y < W:
            self.rect.y += self.speed
        else:
            self.kill
    

meteors = pygame.sprite.Group()

Meteor(randint(25,W-25), METEORS_SURF[0],meteors)#створення першого метеориту,спрайту
 
class Fly(pygame.sprite.Sprite):#Клас гравця, що оминає метеорити
    
    def __init__(self,x,surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, H - 50))
        self.image.set_colorkey((255,255,255))
 
fly=Fly(200, PILOTS_SURF[1])#створення спрайту ракети
sc.blit(fly.image, fly.rect)#

# class Fire(pygame.sprite.Sprite):
#     def __init__(self,x,y,radius,color):
#         self.x=x
#         self.y=y
#         self.radius=radius
#         self.color=color
#         #self.facing=facing
#         self.speed = 8
#     def draw(self,sc):
#         pygame.draw.circle(sc, self.color, (self.x, self.y, self.radius))

while 1:
    a=pygame.event.get()
    for i in a:#вихід
        if i.type == pygame.QUIT:#вихід
            pygame.quit()

        elif i.type== pygame.USEREVENT:#        
            Meteor(randint(25,W-25), METEORS_SURF[randint(0, 2)],meteors)#создание новой машины
 
        for bullet in bullets:
            if bullet.y > 0 and bullet.y < 700:
                bullet.y += bullet.speed
            else:
                bullet.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()#Відслідклвує чи зажата кнопка

    if keys[pygame.K_RIGHT]:#рух вправо
        fly.rect.x+=5
    elif keys[pygame.K_LEFT]:#рух вліво
        fly.rect.x-=5
 
    if pygame.sprite.spritecollide(fly,meteors,False):#якщо був додит з метеорами виводить Game Over
        sc.fill(BLACK)
        sc.blit(text1, (W//2,H//2))
        pygame.display.update()
        break
    
    drawing()

