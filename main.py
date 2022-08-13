import pygame

from pygame.locals import*


pygame.init()
screen_width =3000
screen_height =3000
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Waste Segregation")


bg_img = pygame.image.load("litter_bug_bg.png")
dustbin = pygame.image.load("dustbin.png")
dustbin2 = pygame.image.load("dustbin2.png")
dustbin3 = pygame.image.load("dustbin3.png")
apple = pygame.image.load("apple4.png")
banana = pygame.image.load("bananpeel.png")
plastic = pygame.image.load("Plastic.png")
can = pygame.image.load("can.png")
chocolate = pygame.image.load("chocolatewrapper.png")

game = True
while game:
    screen.blit(bg_img ,(0,0))
    screen.blit(dustbin , (0,150))
    screen.blit(dustbin2 , (125,150))
    screen.blit(dustbin3,(250,150))
    screen.blit(apple , (0,100))
    screen.blit(banana , (100,70))
    screen.blit(plastic,(100,110))
    screen.blit(can , (200,100))
    screen.blit(chocolate , (280,90))
    
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game = False
    pygame.display.update()      
pygame.quit()
