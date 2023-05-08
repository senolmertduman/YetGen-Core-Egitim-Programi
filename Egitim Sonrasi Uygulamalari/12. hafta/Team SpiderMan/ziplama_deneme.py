import pygame
pygame.init()

pencere = pygame.display.set_mode((1000,600))
asker = pygame.image.load('asker.png')
asker_coordinate = asker.get_rect()
asker_coordinate.topleft = (100,300)

dog = pygame.image.load("dog.png")
dog_coordinate = dog.get_rect()
dog_coordinate.topleft = (900,300)
dog_direction = "left"
saat = pygame.time.Clock()
fps = 60
#ziplama algoritmasi icin sayac olusturduk
count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    
    tus = pygame.key.get_pressed()
    if tus[pygame.K_SPACE]:
        while count < 15:
            asker_coordinate.x += 5
            asker_coordinate.y -= 5
            count += 1
            pencere.fill((0,0,0)) 
            pencere.blit(asker,asker_coordinate)

            # köpek hareketi
            if dog_direction == "left":
                dog_coordinate.x -= 20
                pygame.time.delay(75)
            if dog_coordinate.x < 600:
                dog_direction = "right"
                dog = pygame.image.load("dog2.png")
                pygame.time.delay(75)
            if dog_direction == "right":
                dog_coordinate.x += 20
                pygame.time.delay(75)
            if dog_coordinate.x > 900:
                dog_direction = "left"
                dog = pygame.image.load("dog.png")
                pygame.time.delay(75)

            pencere.blit(dog,dog_coordinate)
            saat.tick(fps)
            pygame.display.update()
        while count > 0:
            asker_coordinate.x += 5
            asker_coordinate.y += 5
            count -= 1
            pencere.fill((0,0,0)) 
            pencere.blit(asker,asker_coordinate)
            # köpek hareketi
            if dog_direction == "left":
                dog_coordinate.x -= 20
                pygame.time.delay(50)
            if dog_coordinate.x < 600:
                dog_direction = "right"
                dog = pygame.image.load("dog2.png")
                pygame.time.delay(50)
            if dog_direction == "right":
                dog_coordinate.x += 20
                pygame.time.delay(50)
            if dog_coordinate.x > 900:
                dog_direction = "left"
                dog = pygame.image.load("dog.png")
                pygame.time.delay(50)

            pencere.blit(dog,dog_coordinate)
            saat.tick(fps)
            pygame.display.update()
    pencere.fill((0,0,0)) 
    pencere.blit(asker,asker_coordinate)

    #köpek hareketi

    if dog_direction == "left":
        dog_coordinate.x -= 20
        pygame.time.delay(75)
        if dog_coordinate.x < 600:
            dog_direction = "right"
            dog = pygame.image.load("dog2.png")
            pygame.time.delay(75)
    if dog_direction == "right":
        dog_coordinate.x += 20
        pygame.time.delay(75)
        if dog_coordinate.x > 900:
            dog_direction = "left"
            dog = pygame.image.load("dog.png")
            pygame.time.delay(75)

    pencere.blit(dog,dog_coordinate)

    pygame.display.update()
    saat.tick(fps)
pygame.quit()
