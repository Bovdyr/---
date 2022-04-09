#Создай собственный Шутер!
from pygame import *
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap
from random import *
#from time import *
import os

mixer.init()
font.init()


font_1 = font.SysFont('Arial', 36)
window = display.set_mode ((700, 500))
display.set_caption ("Шутер")
background = transform.scale(image.load("222.jpg"), (700,500))
game = True
clock = time.Clock()
FPS = 60
clock.tick(FPS)
speed = 3
mixer.music.load("bd1783803c8f94a.mp3")
mixer.music.play()
#kick = mixer.Sound("fire.ogg")
'''font.init()
font = font.Font(None,70)'''
finish = False
'''run = True
propusk = 0
balli = 0
wine = 0
heal = 3
num_fire = 0
monsters = sprite.Group()
bulletes = sprite.Group()
asteroids = sprite.Group()'''

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,x,y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        self.image = transform.scale(image.load(player_image), (30,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def Updatel(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and a1.rect.y>5:
            a1.rect.y -= speed
        if keys_pressed[K_DOWN] and a1.rect.y<390:
            a1.rect.y += speed
    def Updater(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and a2.rect.y>5:
            a2.rect.y -= speed
        if keys_pressed[K_s] and a2.rect.y<390:
            a2.rect.y += speed
        '''if keys_pressed[K_SPACE] and num_fire < 5:
            self.fire()
            num_fire += 1
        elif num_fire > 5:
            num_fire = 0
            start = time()
            sleep(3)
            end = time()
            if keys_pressed[K_SPACE] and end - start = 3:
                text_h = font_1.render("Жизни: "+ str(heal),1,(255,255,255))
    def fire(self):
        bullet1 = Bullet("bullet.png", self.rect.centerx, self.rect.top, 3)
        bulletes.add(bullet1)'''


'''class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed,65,65)
    def update(self):
        global propusk
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)
            self.rect.y = 10
            propusk += 1
            self.rect.y += self.speed
    def Srr(self):
        global wine
        if sprite.groupcollide(monsters, bulletes, True, True):
            wine += 1
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)

class asteroidsq(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed,65,65)
    def update(self):
        global propusk
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(25,650)
            self.speed = randint(1,2)
            self.rect.y = 10
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed,10,20)
    def update(self):
        if self.rect.y >0:
            self.rect.y -= self.speed
        else:
            self.kill()'''


'''win = font.render('YOU WIN!', True, (0, 215, 0))
fal = font.render('YOU LOSE!', True, (225, 0, 0))'''
a1 = Player('111.jpg', 10, 430, speed)
a2 = Player('111.jpg', 640, 430, speed)
'''a_1 = asteroidsq("asteroid.png", randint(25,650), 10, 1)
a_2 = asteroidsq("asteroid.png", randint(25,650), 10, 1)
a_3 = asteroidsq("asteroid.png", randint(25,650), 10, 1)
b_1 = Enemy("ufo.png", randint(25,650), 10, randint(1,2))
b_2 = Enemy("ufo.png", randint(25,650), 10, randint(1,2))
b_3 = Enemy("ufo.png", randint(25,650), 10, randint(1,2))
b_4 = Enemy("ufo.png", randint(25,650), 10, randint(1,2))
b_5 = Enemy("ufo.png", randint(25,650), 10, randint(1,2))
bul_1 = Bullet('bullet.png', randint(25,40), 430, speed)
bul_2 = Bullet('bullet.png', 20, 430, speed)
monsters.add(b_1,b_2,b_3,b_4,b_5)
asteroids.add(a_1, a_2, a_3)
'''
#bulletes.add(bul_1)
#bullet.kill()
#spritest = sprite.groupcollide(monsters, bulletes, True, True)
#spritest_list = sprite.spritecollide(monsters, a, False)
while game:
    if finish == False:
        '''text_lose = font_1.render("Пропущено: "+ str(propusk),1,(255,255,255))
        text_wine = font_1.render("Счёт: "+ str(wine),1,(255,255,255))
        text_h = font_1.render("Жизни: "+ str(heal),1,(255,255,255))'''
        window.blit(background, (0,0))
        window.blit(a1.image,(a1.rect.x,a1.rect.y))
        window.blit(a2.image,(a2.rect.x,a2.rect.y))
        '''window.blit(text_lose,(10,50))
        window.blit(text_wine,(10,10))
        window.blit(text_h,(10,90))
        monsters.draw(window)
        bulletes.draw(window)
        asteroids.draw(window)'''
        a1.Updatel()
        a2.Updater()
        '''monsters.update()
        bulletes.update()
        asteroids.update()
        if sprite.groupcollide(monsters, bulletes, True, True):
            wine += 1
            b = Enemy("ufo.png", randint(25,650), 10, 1)
            monsters.add(b)

        if sprite.spritecollide(a, monsters, False):
            window.blit(fal ,(280,230))
            finish = True

        if sprite.spritecollide(a, asteroids, True):
            heal -= 1
            ast = asteroidsq("asteroid.png", randint(25,650), 10, 1)
            asteroids.add(ast)
            
        if heal <= 0:
            window.blit(fal ,(280,230))
            finish = True

        if wine >= 10:
            window.blit(win ,(270,230))
            finish = True
            

        if propusk >= 10:
            window.blit(fal ,(280,230))
            finish = True'''
            
        for e in event.get():
            if e.type == QUIT:
                game = False
    display.update()