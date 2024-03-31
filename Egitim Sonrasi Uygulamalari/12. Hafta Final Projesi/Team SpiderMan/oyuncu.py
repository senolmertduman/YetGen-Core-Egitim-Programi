import pygame
from pygame.locals import *

class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('images/hayriyesag.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = 520
        self.rect.centerx = 350
        self.hiz = 10
        self.jump = False
        self.jumpC = 10  
        self.adim = False
    def update(self):
        tus = pygame.key.get_pressed()
#saga,sola,yukari ve asagi hareket
        if tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
            self.image = pygame.image.load('images/hayriyesol.png')
            if self.adim == False:
                self.image = pygame.image.load('images/hayriyesol.png')
                self.adim = True
            elif self.adim == True:
                self.image = pygame.image.load('images/hayriyesol1.png')
                self.adim = False
        elif tus[pygame.K_RIGHT] and self.rect.right < 1000:
            self.rect.x += self.hiz
            if self.adim == False:
                self.image = pygame.image.load('images/hayriyesag.png')
                self.adim = True
            elif self.adim == True:
                self.image = pygame.image.load('images/hayriyesag1.png')
                self.adim = False
        elif tus[pygame.K_UP] and self.rect.bottom > 400:
            self.rect.y -= self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.hiz
#ziplama fonksiyonu
        if self.jump == False:
            if tus[pygame.K_SPACE]:
                self.jump = True
        else:
            oyuncu = Oyuncu()
            oyuncu.image = pygame.image.load('images/hayriyezipla.png')
            if self.jumpC >= -10:
                self.rect.y -= (self.jumpC * abs(self.jumpC)) * 0.5
                self.jumpC -= 1
            else:
                self.jump = False
                oyuncu.image = pygame.image.load('images/hayriyesag.png')
                self.jumpC = 10
                self.rect.bottom = 520