import pygame

# визначаємо константу затримки кадрів
# та інші константи
WIDTH_DISPLAY = 640
HEIGHT_DISPLAY = 560
FPS = 60

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
BLUE = (0, 0, 255)
 
# ініціалізація та створення об'єктів
pygame.init()
# pygame.display.set_mode((600, 400))
#gameDisplay=pygame.display.set_mode((640, 560), pygame.RESIZABLE)
gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
pygame.display.set_caption("My first game")


done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    pygame.draw.rect(gameDisplay, (255,0,0), [55, 50, 80, 55])
    
    
    pygame.display.update()
    clock.tick(FPS)