import pygame, random
 
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SuperSpace")
bg = pygame.image.load('C:/Users/adm.a.danyliuk/Desktop/softserve/lecture8/homework/bg2.png')
bullets = []
clock = pygame.time.Clock()
x = 90
y = 450
width = 20
height = 20
speed = 10
run = True
enemies = [random.randrange(1,50)*10, random.randrange(1,20)*10]
enemiesVisible = True
body = [[x, y], [x + 20,y], [x + 40,y],[x + 20,y-20]] # Структура тела питончика
 
class snaryad():
    def __init__(self, x , y, color, facing):
        self.x = x
        self.y = y
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    def draw(self, win):
        pygame.draw.rect(win, self.color, (pygame.Rect(self.x, self.y, 20 , 20)))   
 
 
while run:
    clock.tick(15)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        body[0][0] -= speed
        body[1][0] -= speed
        body[2][0] -= speed
        body[3][0] -= speed
    if keys[pygame.K_RIGHT] and x < 500 - 3*width:
        x += speed
        body[0][0] += speed
        body[1][0] += speed
        body[2][0] += speed
        body[3][0] += speed
    if keys[pygame.K_f]:
        facing = 1
        if len(bullets) < 100:
            bullets.append(snaryad(round(x + width), round(y - height),(255, 0, 0), facing))
    
 
    for bullet in bullets:
        if bullet.x < enemies[0] < bullet.x + width and bullet.y < enemies[1] < bullet.y + height:
            enemiesVisible = False
 
        if bullet.x < enemies[0] + width < bullet.x + width and  bullet.y < enemies[1] + height  < bullet.y + height:
            enemiesVisible = False
        
 
        if bullet.y < 500 and bullet.y > 0:
            bullet.y -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))  
 
    if enemiesVisible == False:
        enemies = [random.randrange(1, 50)*10, random.randrange(1,20)*10]
        enemiesVisible = True
                    

    win.fill((0,0,255)) 
    win.blit(bg,(0,0))
    pygame.draw.rect(win, (255,255,255), (pygame.Rect(enemies[0],enemies[1], width, height)))
    for element in body:
        pygame.draw.rect(win, (0,255,0), (pygame.Rect(element[0],element[1], width , height)))  
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()
pygame.quit()