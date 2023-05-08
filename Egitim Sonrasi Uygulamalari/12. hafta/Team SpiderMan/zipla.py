import pygame
pygame.init()

pencere = pygame.display.set_mode((1000,600))
asker = pygame.image.load('asker.png')
askerC = asker.get_rect()
askerC.x = 200
askerC.y = 300
askerC.width = asker.get_width()
askerC.height = asker.get_height()


speed = 5
jump = False
jumpC = 10


dog = pygame.image.load("dog.png")
dog_coordinate = dog.get_rect()
dog_coordinate.topleft = (900,300)
dog_direction = "left"

saat = pygame.time.Clock()
running = True
while running:
    #pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    tus = pygame.key.get_pressed()
    if tus[pygame.K_LEFT] and askerC.x > 0:
        askerC.x -= speed
    if tus[pygame.K_RIGHT]:
        askerC.x += speed
    ###ZIPLAMA####
    if jump == False:
        if tus[pygame.K_SPACE]:
            jump = True
    else:
        if jumpC >= -10:
            askerC.y -= (jumpC * abs(jumpC)) * 0.5
            jumpC -= 1
        else:
            jump = False
            jumpC = 10
    #####KOPEK HAREKETI####
    if dog_direction == "left":
        dog_coordinate.x -= 20
    if dog_coordinate.x < 400:
        dog_direction = "right"
        dog = pygame.image.load("dog2.png")
    if dog_direction == "right":
        dog_coordinate.x += 20
    if dog_coordinate.x > 950:
        dog_direction = "left"
        dog = pygame.image.load("dog.png")
        

    pencere.fill((130,222,134))
    pencere.blit(asker,askerC)
    pencere.blit(dog,dog_coordinate)
    pygame.display.update()
    saat.tick(30)
pygame.quit()