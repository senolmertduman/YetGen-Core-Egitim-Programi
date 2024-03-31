import pygame
from pygame.locals import *
from oyuncu import Oyuncu

# Pygame modüllerini kullanabilmek icin init() fonksiyonunu yazdik.
pygame.init()
# Pencere boyutunu ayarladik
genislik = 1000
yukseklik = 600
screen = pygame.display.set_mode((genislik, yukseklik))
# Pencere ismi belirledik
pygame.display.set_caption("Team Spiderman Games")
#######RENKLER#######
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)
mavi = (0, 0, 255)
sari = (255, 255, 0)
turuncu = (255, 165, 0)
mor = (128, 0, 128)
pembe = (255, 192, 203)
koyu_portakal = (255, 140, 0)
koyu_turkuaz = (0, 206, 209)
lavanta = (230, 230, 250)
sari_yesil = (173, 255, 47)
sarisin = (255, 255, 240)
orta_mor = (147, 112, 219)
acik_deniz_yesili = (32, 178, 170)
kahverengi = (240, 230, 140)
koyu_portakal_kirmizi = (220, 20, 60)
altin = (255, 215, 0)
acik_yesil = (144, 238, 144)
koyu_zeytin_yesili = (85, 107, 47)
gumus = (192, 192, 192)
orta_deniz_yesili = (60, 179, 113)
koyu_mavi = (0, 0, 139)
######BUTON SINIFI########
class Button:
# butonumuz icin x ekseni, y ekseni, yukseklik, genislik, ana renk, arkaplan rengi, resim ismi ve yazi 
# parametrelerini sinifimiza dahil ettik
    def __init__(self, x, y, width, height, color1, color2, image_name, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color1 = color1
        self.color2 = color2
        self.text = text
        self.image = pygame.image.load(image_name)
# butonumuzu olusturacak ve ana pencereye ekleyecek fonksiyonu yazdik. Burada surface degiskeni ile 
# butonun eklenecegi pencereyi belirtecegiz.
    def draw(self, surface):
        pygame.draw.rect(surface, self.color1, self.rect)
        image_rect = self.image.get_rect(center = self.rect.center)
        
        surface.blit(self.image, image_rect)
        font = pygame.font.SysFont("calibri", 32, True)
        text = font.render(self.text, True, self.color2)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
# ana ekranda oyuna baslayacagimiz play butonunu olusturduk
play_button = Button(250, 250, 500, 100, acik_deniz_yesili, gumus,'images/cloud.png', "PLAY GAME")
#game over ekranindaki oyuna yeniden donus icin replay replay butonunu olusturduk
replay_button = Button(250, 370, 500, 100, kirmizi, gumus,'images/cloud2.png', "REPLAY GAME")
#win ekraninda oyuna donus icin replay butonu olusturduk
replay_button2 = Button(400, 470, 200, 100, beyaz, acik_deniz_yesili,'images/cloud.png', "REPLAY GAME")
###YAZI EKLEME SINIFI###
class YaziEkle:
#bu sinif vasitasi ile ekranda istedigimiz yere kolaylikla yazi ekleyebilecegiz.
    def __init__(self, x, y,  color1, color2, text,bold):
        self.rect = (x,y)
        self.color1 = color1
        self.color2 = color2
        self.text = text
        self.bold = bold
    def draw(self,surface):
        font = pygame.font.SysFont("calibri", self.bold, True)
        text = font.render(self.text, True, self.color1,self.color2)
        text_rect = text.get_rect()
        text_rect.topleft = self.rect
        surface.blit(text, text_rect)

#########OYUNCU SINIFI####

#puanlari saymasi icin bir puan degiskeni olusturduk.
point = 0
#oyuncu sinifimizdan bir karakter olusturduk
oyuncu = Oyuncu()
oyuncu_grup = pygame.sprite.Group()
oyuncu_grup.add(oyuncu)
#oyun hizimizi belirledik
fps = 60
saat = pygame.time.Clock()
#input kutusu olusturduk
font_box = pygame.font.Font(None, 32)
input_box = pygame.Rect(430, 500, 140, 32)
kullanici = ''
#Ana ekrandaki (oyuncu adi: ) yazisini olusturduk.
oyuncu_adi = YaziEkle(400,450,gumus,None,'Oyuncu Adı: ',32)
#ana ekrana oyun tabelasi olusturduk
tabela = pygame.image.load('images/tabela.png')
tabelaC = tabela.get_rect()
tabelaC.center = (genislik/2,100)
############### ANA OYUN DONGUMUZ ###############
running = True
while running:
# bu kod sayesinde eger oyun kapatilirsa dongu sonlanacak ve oyundan cikilacaktir.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                kullanici = ''
            elif event.key == pygame.K_BACKSPACE:
                kullanici = kullanici[:-1]
            else:
                kullanici += event.unicode
# her dongude arka plan yesile boyanacak.
    screen.fill(acik_deniz_yesili)
# play butonunu cizdirdik.
    play_button.draw(screen)
#INPUT KUTUSU
# input kutusu rengini ayarladik.
    pygame.draw.rect(screen, kirmizi, input_box, 2)
# input kutusu içindeki metni olusturduk.
    txt_surface = font_box.render(kullanici, True, gumus)
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
# input kutusunun sınırlarını cizdik.
    pygame.draw.rect(screen, gumus, input_box, 2)
#oyuncu adi yazisini ekrana ekledik.
    oyuncu_adi.draw(screen)
#tabelayi ekrana cizdik
    screen.blit(tabela,tabelaC)
#mouse pozisyonunu ve mouse basilip basilmadigi bilgilerini aldik.
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
# eger mouse play butonunun uzerindeyse ve mousenin sol tusuna iki kere basildiysa bu kod calisacak.
# Amacimiz bu kod blogu calistiginda oyunun ilk penceresi calissin.
    if mouse_pressed[0] and play_button.rect.collidepoint(mouse_pos):
####### 1. PENCERE ##########
        kopek = pygame.image.load('images/dog.png')
        kopekC = kopek.get_rect()
        money = pygame.image.load('images/money.png')
        moneyC = money.get_rect()
        moneyC.bottom = 520
        moneyC.centerx = 650 
        kopekC.bottom = 520
        kopekC.centerx = 550 
        pencere1 = pygame.display.set_mode((genislik,yukseklik))
        arka_plan1 = pygame.image.load('images/pencere1.jpeg')
#kopek hareketi icin yon belirledik
        kopekYon = 'left'
        
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    running1 = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            pencere1.fill(siyah)
            pencere1.blit(arka_plan1,(0,0))
#oyuncunun cidigimiz sinirlarda kalmasi icin
            if oyuncu.rect.x < 300:
                oyuncu.rect.x = 300
            if oyuncu.jump != True:
                if oyuncu.rect.bottom <500:
                    oyuncu.rect.bottom = 500
                if oyuncu.rect.bottom >580:
                    oyuncu.rect.bottom = 580
#kopek hareketi
            if kopekYon == 'right' and kopekC.x < 650:
                kopekC.x += 1
                if kopekC.x == 650:
                    kopekYon = 'left'
                    kopek = pygame.image.load('images/dog.png')
            elif kopekYon == 'left' and kopekC.x > 400:
                kopekC.x-= 1
                if kopekC.x == 400:
                    kopekYon = 'right'
                    kopek = pygame.image.load('images/dog2.png')
#Oyuncu kopege temas ederse game over penceresi acilacak
            if oyuncu.rect.colliderect(kopekC):
                pygame.mixer.music.load("audios/gameoverses.wav")
                pygame.mixer.music.play(1,0.0)
                point = 0
                yazi = YaziEkle(300,200,siyah,None,'GAME OVER!',64)
                pencere_go = pygame.display.set_mode((genislik,yukseklik))
                running_kopek = True
                while running_kopek:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            running1 = False
                            running_kopek = False
                    pencere_go.fill(kirmizi)
                    replay_button.draw(pencere_go)
                    yazi.draw(pencere_go)
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    
                    if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                        oyuncu.rect.bottom = 520
                        oyuncu.rect.centerx = 350 
                        running1 = False
                        running_kopek = False
                    pygame.display.update()
#oyuncu paraya temas ederse puan 1 artacak   
            if oyuncu.rect.colliderect(moneyC):
                pygame.mixer.music.load("audios/odulses.wav")
                pygame.mixer.music.play(1,0.0)
                point += 1
                moneyC.topleft = (1100,700)
#skor yazisini ekrana ekledik    
            skor = YaziEkle(0,0,siyah,gumus,f'Skor: {point}',32)
            skor.draw(pencere1)
            pencere1.blit(money,moneyC)
            pencere1.blit(kopek, kopekC)
            oyuncu_grup.draw(pencere1)
            oyuncu_grup.update()
            pygame.display.update()
            saat.tick(fps)
            if oyuncu.rect.x > 700:
############2. PENCERE KODLARI #######
                oyuncu.rect.bottom = 520
                oyuncu.rect.centerx = 100
                pencere2 = pygame.display.set_mode((genislik,yukseklik))
                arka_plan2 = pygame.image.load('images/pencere2.jpeg')
                temizlikci = pygame.image.load('images/temizlikcisol.png')
                temizlikciC = temizlikci.get_rect()
                temizlikciC.topleft = (700,400) 
                money2 = pygame.image.load('images/money.png')
                money2C = money2.get_rect()
                money2C.topleft = (360,400)
                money3 = pygame.image.load('images/money.png')
                money3C = money3.get_rect()
                money3C.topleft = (700,400)
#temizlikci hareketi icin yon belirledik
                temizliciYon = 'left'

                anahtar1 = pygame.image.load('images/key.png')
                anahtar2 = pygame.image.load('images/key.png')
                anahtar3 = pygame.image.load('images/key.png')
                anahtar1C = anahtar1.get_rect()
                anahtar1C.topleft = (100,300)
                anahtar2C = anahtar2.get_rect()
                anahtar2C.topleft = (360,300)
                anahtar3C = anahtar3.get_rect()
                anahtar3C.topleft = (700,300)
#gorev yazisini ekrana ekledik
                gorev = YaziEkle(650,10,siyah,None,'Oda numaranı bul!',32)

                running2 = True
                while running2:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            running1 = False
                            running2 = False
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    pencere2.fill(siyah)
                    pencere2.blit(arka_plan2,(0,0))
#paraya temas
                    if oyuncu.rect.colliderect(money2C):
                        pygame.mixer.music.load("audios/odulses.wav")
                        pygame.mixer.music.play(1,0.0)
                        point += 1
                        money2C.topleft = (1100,700)
                    if oyuncu.rect.colliderect(money3C):
                        pygame.mixer.music.load("audios/odulses.wav")
                        pygame.mixer.music.play(1,0.0)
                        point += 1
                        money3C.topleft = (1100,700)
#temizlikci hareketi
                    if temizliciYon == 'right' and temizlikciC.x < 800:
                        temizlikciC.x += 1
                        if temizlikciC.x == 800:
                            temizliciYon = 'left'
                            temizlikci = pygame.image.load('images/temizlikcisol.png')
                    elif temizliciYon == 'left' and temizlikciC.x > 600:
                        temizlikciC.x-= 1
                        if temizlikciC.x == 600:
                            temizliciYon = 'right'
                            temizlikci = pygame.image.load('images/temizlikcisag.png')
#Oyuncu temizlikciye temas ederse game over penceresi acilacak
                    if oyuncu.rect.colliderect(temizlikciC):
                        pygame.mixer.music.load("audios/gameoverses.wav")
                        pygame.mixer.music.play(1,0.0)
                        point = 0
                        yazi = YaziEkle(300,200,siyah,None,'GAME OVER!',64)
                        pencere_go = pygame.display.set_mode((genislik,yukseklik))
                        running_temizlikci = True
                        while running_temizlikci:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    running1 = False
                                    running2 = False
                                    running_temizlikci = False
                            pencere_go.fill(kirmizi)
                            replay_button.draw(pencere_go)
                            mouse_pos = pygame.mouse.get_pos()
                            mouse_pressed = pygame.mouse.get_pressed()
                            yazi.draw(pencere_go)
                            if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                                oyuncu.rect.bottom = 520
                                oyuncu.rect.centerx = 350 
                                running1 = False
                                running2 = False
                                running_temizlikci = False
                            pygame.display.update()
#sifreyi bulmak icin anahtara temas edecek
                    if oyuncu.rect.colliderect(anahtar3C):
                        pygame.mixer.music.load("audios/keyses.wav")
                        pygame.mixer.music.play(1,0.0)
                        sifre = YaziEkle(650,100,kirmizi,None,'Oda numaran 103',32)
                        sifre.draw(pencere2)
                    skor = YaziEkle(0,0,siyah,gumus,f'Skor: {point}',32)
                    pencere2.blit(money2,money2C)
                    pencere2.blit(money3,money3C)
                    pencere2.blit(temizlikci,temizlikciC)
                    gorev.draw(pencere2)
                    pencere2.blit(anahtar1,anahtar1C)
                    pencere2.blit(anahtar2,anahtar2C)
                    pencere2.blit(anahtar3,anahtar3C)
                    skor.draw(pencere2)
                    oyuncu_grup.draw(pencere2)
                    oyuncu_grup.update()
                    pygame.display.update()
                    saat.tick(fps)
                    if oyuncu.rect.x > 900:
############ 3. PENCERE KODLARI #######
                        oyuncu.rect.bottom = 520
                        oyuncu.rect.centerx = 100
                        pencere3 = pygame.display.set_mode((genislik,yukseklik))
                        arka_plan3 = pygame.image.load('images/pencere3.jpeg')
                        muz = pygame.image.load('images/banana.png')
                        muzC = muz.get_rect()
                        muzC.topleft = (200,400)
                        orumcek = pygame.image.load('images/spider.png')
                        orumcekC = orumcek.get_rect()
                        orumcekC.topleft = (300,400)
#orumcek hareketi icin yon belirledik
                        orumcekYon = 'up' 
                        su_birikintisi = pygame.image.load('images/puddle.png')
                        su_birikintisiC = su_birikintisi.get_rect()
                        su_birikintisiC.topleft = (600,500)
                        money4 = pygame.image.load('images/money.png')
                        money4C = money2.get_rect()
                        money4C.topleft = (700,500)
                        running3 = True
                        while running3:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    running1 = False
                                    running2 = False
                                    running3 = False
                            mouse_pos = pygame.mouse.get_pos()
                            mouse_pressed = pygame.mouse.get_pressed()
                            pencere3.fill(siyah)
                            pencere3.blit(arka_plan3,(0,0))
#oyuncu paraya temas ederse
                            if oyuncu.rect.colliderect(money4C):
                                pygame.mixer.music.load("audios/odulses.wav")
                                pygame.mixer.music.play(1,0.0)
                                point += 1
                                money4C.topleft = (1100,700)
#oyuncu muza temas ederse 100 pixel ileri kayacak
                            if oyuncu.rect.colliderect(muzC):
                                oyuncu.rect.x +=100
#orumcek hareketi
                            if orumcekYon == 'up' and orumcekC.y > 350:
                                orumcekC.y -= 1
                                if orumcekC.y == 350:
                                    orumcekYon = 'down'
                                    orumcek = pygame.image.load('images/spider2.png')
                            elif orumcekYon == 'down' and orumcekC.y < 600:
                                orumcekC.y += 1
                                if orumcekC.y == 550:
                                    orumcekYon = 'up'
                                    orumcek = pygame.image.load('images/spider.png')
# oyuncu orumcege temas ederse
                            if oyuncu.rect.colliderect(orumcekC):
                                pygame.mixer.music.load("audios/gameoverses.wav")
                                pygame.mixer.music.play(1,0.0)
                                point = 0
                                yazi = YaziEkle(300,200,siyah,None,'GAME OVER!',64)
                                pencere_go = pygame.display.set_mode((genislik,yukseklik))
                                running_orumcek = True
                                while running_orumcek:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False
                                            running1 = False
                                            running2 = False
                                            running3 = False
                                            running_orumcek = False
                                    pencere_go.fill(kirmizi)
                                    replay_button.draw(pencere_go)
                                    mouse_pos = pygame.mouse.get_pos()
                                    mouse_pressed = pygame.mouse.get_pressed()
                                    yazi.draw(pencere_go)
                                    if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                                        oyuncu.rect.bottom = 520
                                        oyuncu.rect.centerx = 350 
                                        running1 = False
                                        running2 = False
                                        running3 = False
                                        running_orumcek = False
                                    pygame.display.update()
                            skor = YaziEkle(0,0,siyah,gumus,f'Skor: {point}',32)
                            pencere3.blit(su_birikintisi,su_birikintisiC)
                            pencere3.blit(muz,muzC)
                            pencere3.blit(orumcek,orumcekC)
                            pencere3.blit(money4,money4C)
                            skor.draw(pencere3)
                            oyuncu_grup.draw(pencere3)
                            oyuncu_grup.update()
                            pygame.display.update()
                            saat.tick(fps)
                            if oyuncu.rect.x > 900:
############4. PENCERE KODLARI ##########
                                oyuncu.rect.bottom = 520
                                oyuncu.rect.centerx = 100
                                pencere4 = pygame.display.set_mode((genislik,yukseklik))
                                arka_plan4 = pygame.image.load('images/pencere4.jpeg')
                                money5 = pygame.image.load('images/money.png')
                                money5C = money2.get_rect()
                                money5C.topleft = (700,500)

# hosgeldin yazisi
                                hosgeldin_yazi = YaziEkle(450,100,koyu_mavi,None,f'Odana Hosgeldin {kullanici.capitalize()}',32)
                                goblin = pygame.image.load('images/goblinsag.png')
                                goblinC= goblin.get_rect()
                                goblinC.bottomright = (610,600)
                                goblinYon = 'right'
                                running4 = True
                                while running4:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False
                                            running1 = False
                                            running2 = False
                                            running3 = False
                                            running4 = False
                                    mouse_pos = pygame.mouse.get_pos()
                                    mouse_pressed = pygame.mouse.get_pressed()
                                    pencere4.fill(siyah)
                                    pencere4.blit(arka_plan4,(0,0))
#goblin hareketi
                                    if goblinYon == 'right' and goblinC.x < 1000:
                                        goblinC.x += 1
                                        if goblinC.x == 1000:
                                            goblinYon = 'left'
                                            goblin = pygame.image.load('images/goblinsol.png')
                                    elif goblinYon == 'left' and goblinC.x > 500:
                                        goblinC.x-= 1
                                        if goblinC.x == 500:
                                            goblinYon = 'right'
                                            goblin = pygame.image.load('images/goblinsag.png')
#oyuncu paraya temas ederse
                                    if oyuncu.rect.colliderect(money5C):
                                        pygame.mixer.music.load("audios/odulses.wav")
                                        pygame.mixer.music.play(1,0.0)
                                        point += 1
                                        money5C.topleft = (1100,700)
#oyuncu gobline temas ederse
                                    if oyuncu.rect.colliderect(goblinC):
                                        pygame.mixer.music.load("audios/gameoverses.wav")
                                        pygame.mixer.music.play(1,0.0)
                                        point = 0
                                        yazi = YaziEkle(300,200,siyah,None,'GAME OVER!',64)
                                        pencere_go = pygame.display.set_mode((genislik,yukseklik))
                                        
                                        running_goblin = True
                                        while running_goblin:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    running = False
                                                    running1 = False
                                                    running2 = False
                                                    running3 = False
                                                    running4 = False
                                                    running_goblin = False
                                            pencere_go.fill(kirmizi)
                                            replay_button.draw(pencere_go)
                                            mouse_pos = pygame.mouse.get_pos()
                                            mouse_pressed = pygame.mouse.get_pressed()
                                            yazi.draw(pencere_go)
                                            if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                                                oyuncu.rect.bottom = 520
                                                oyuncu.rect.centerx = 350 
                                                running1 = False
                                                running2 = False
                                                running3 = False
                                                running4 = False
                                                running_goblin = False
                                            pygame.display.update()
#oyuncu oda kapisina temas ederse kazanacak
                                    if oyuncu.rect.colliderect((890,180,100,200)):
                                        pygame.mixer.music.load("audios/winses.wav")
                                        pygame.mixer.music.play(1,0.0)
                                        pencere_win = pygame.display.set_mode((genislik,yukseklik))
                                        arkaplan_win = pygame.image.load('images/win.jpeg')
                                        yildiz1 = pygame.image.load('images/star2.png')
                                        yildiz1C = yildiz1.get_rect()
                                        yildiz1C.topleft = (250,20)
                                        yildiz2 = pygame.image.load('images/star2.png')
                                        yildiz2C = yildiz2.get_rect()
                                        yildiz2C.topleft = (450,20)
                                        yildiz3 = pygame.image.load('images/star2.png')
                                        yildiz3C = yildiz3.get_rect()
                                        yildiz3C.topleft = (650,20)
                                        running_win = True
                                        while running_win:
                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    running = False
                                                    running1 = False
                                                    running2 = False
                                                    running3 = False
                                                    running4 = False
                                                    running_win = False
                                            pencere_win.fill(kirmizi)
                                            pencere_win.blit(arkaplan_win,(0,0))
                                            replay_button2.draw(pencere_win)
                                            pencere_win.blit(yildiz1,yildiz1C)
                                            pencere_win.blit(yildiz2,yildiz2C)
                                            pencere_win.blit(yildiz3,yildiz3C)
#topladigi altinlara gore win ekraninda kac yildiz aldigi gorunecek
                                            if point == 5:
                                                yildiz1 = pygame.image.load('images/star.png')
                                                yildiz2 = pygame.image.load('images/star.png')
                                                yildiz3 = pygame.image.load('images/star.png')
                                            elif point >= 3:
                                                yildiz1 = pygame.image.load('images/star.png')
                                                yildiz2 = pygame.image.load('images/star.png')
                                            elif point >= 1:
                                                yildiz1 = pygame.image.load('images/star.png')
                                            mouse_pos = pygame.mouse.get_pos()
                                            mouse_pressed = pygame.mouse.get_pressed()                                     
                                            if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                                                point = 0
                                                oyuncu.rect.bottom = 520
                                                oyuncu.rect.centerx = 350 
                                                running1 = False
                                                running2 = False
                                                running3 = False
                                                running4 = False
                                                running_win = False
                                            pygame.display.update()
                                    skor = YaziEkle(0,0,siyah,gumus,f'Skor: {point}',32)
                                    skor.draw(pencere4)
                                    pencere4.blit(money5,money5C)
                                    pencere4.blit(goblin,goblinC)
                                    hosgeldin_yazi.draw(pencere4)
                                    oyuncu_grup.draw(pencere4)
                                    oyuncu_grup.update()
                                    pygame.display.update()
                                    saat.tick(fps)
    pygame.display.update()

pygame.quit()
