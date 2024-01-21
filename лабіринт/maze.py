from pygame import *
from random import randint
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed=key.get_pressed()

        if keys_pressed[K_w] and player.rect.y > 0: 
            player.rect.y-=self.speed     
        if keys_pressed[K_s] and player.rect.y < 420: 
            player.rect.y+=self.speed 
        if keys_pressed[K_a] and player.rect.x > 0: 
            player.rect.x-=self.speed
        if keys_pressed[K_d] and player.rect.x < 620: 
            player.rect.x+=self.speed

class Enemy(GameSprite):
    direction="left"
    def update(self):
        if self.rect.x<=470:
            self.direction="right"
        if self.rect.x>=615:
            self.direction="left"
        if self.direction=="left":
            self.rect.x-=self.speed
        else:
            self.rect.x+=self.speed


speed=5
win_width=700
win_hieght=500

window = display.set_mode((win_width,win_hieght))
display.set_caption("Maze")
background=transform.scale(image.load("background.png"),(win_width,win_hieght))

player=GameSprite("hero.png" , 5 , win_hieght-80 , 4)
monster=GameSprite("zombie.png" , win_width-80 , 280 , 2)
final=GameSprite("treasure.png", win_width-50,win_hieght-80,0)


class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_heidth):
        super().__init__()
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.wall_width=wall_width
        self.wall_heidth=wall_heidth
        self.image=Surface((wall_width,wall_heidth))
        self.image.fill((color_1,color_2,color_3))
        self.rect=self.image.get_rect()
        self.rect.x=wall_x
        self.rect.y=wall_y

    def draw_wall(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

random=2#randint(1,3)
wal1=125
wal2=70
if (random==1):
    #1 лабіринт
    #основа
    wall_1=Wall(85, 107, 47, 80,10,wal2*7,10)#горизонтальні
    wall_2=Wall(85, 107, 47, 80,490,wal2*7,10)#горизонтальні
    wall_3=Wall(85, 107, 47, 80,120,10,380)#вертикальні
    wall_4=Wall(85, 107, 47, wal2*7+80,120,10,380)#вертикальні

    wall_5=Wall(85, 107, 47, 150,wal1,10,wal1*2)#вертикальна
    wall_6=Wall(85, 107, 47, 150,wal1,wal2,10)#горизонтальні
    wall_7=Wall(85, 107, 47, 220,wal1*2,10,wal1*2)#вертикальна
    wall_8=Wall(85, 107, 47, 290,10,10,wal1*3)#вертикальна
    wall_9=Wall(85, 107, 47, 290,wal1*2,55,10)#горизонтальні
    wall_10=Wall(85, 107, 47, 420,wal1,10,wal1*3)#вертикальна
    wall_11=Wall(85, 107, 47, 490,10,10,wal1*3)#вертикальна


#80 ліва частина 100 права 180 сум їх пол сум 90
#525 всього лабіринт сума вертикальних стінок 70 
#вільного місця 455


if (random==2):
    #2 лабіринт
    #основа
    wall_1=Wall(85, 107, 47, 80,10,wal2*7,10)#горизонтальні
    wall_2=Wall(85, 107, 47, 80,490,wal2*7,10)#горизонтальні
    wall_3=Wall(85, 107, 47, 80,10,10,200)#вертикальні
    wall_4=Wall(85, 107, 47, 80,290,10,200)#вертикальні
    wall_5=Wall(85, 107, 47, wal2*7+80,120,10,380)#вертикальні

    wall_6=Wall(85, 107, 47, 150,wal1*2,420,10)#горизонтальні
    wall_7=Wall(85, 107, 47, 150,wal1,10,wal1*2)#вертикальна
    wall_8=Wall(85, 107, 47, 150+wal2*3,wal1,10,wal1*2)#вертикальна
    wall_9=Wall(85, 107, 47, 250,10,10,wal1)#вертикальна
    wall_10=Wall(85, 107, 47, 250,380,10,wal1)#вертикальна
    wall_11=Wall(85, 107, 47, 490,10,10,wal1)#вертикальна
    wall_12=Wall(85, 107, 47, 490,380,10,wal1)#вертикальна


if (random==3):
    #3 лабіринт
    #основа
    wall_1=Wall(85, 107, 47, 80,10,wal2*7,10)#горизонтальні
    wall_2=Wall(85, 107, 47, 80,490,wal2*7,10)#горизонтальні
    wall_3=Wall(85, 107, 47, 80,10,10,380)#вертикальні
    wall_4=Wall(85, 107, 47, wal2*7+80,120,10,380)#вертикальні

    wall_5=Wall(85, 107, 47, 80,wal1*2+70,140,10)#горизонтальні
    wall_6=Wall(85, 107, 47, 270,wal1*2+70,180,10)#горизонтальні
    wall_7=Wall(85, 107, 47, 160,180,410,10)#горизонтальні
    wall_8=Wall(85, 107, 47, 125+wal2*3,10,10,100)#вертикальна
    wall_9=Wall(85, 107, 47, 150+wal2*3,wal1*2+70,10,100)#вертикальна
    wall_10=Wall(85, 107, 47, 150+wal2*3,wal1*2+70,10,100)#вертикальна
    wall_11=Wall(85, 107, 47, 150+wal2*3,wal1*2+70,10,100)#вертикальна


font.init()
font=font.Font(None,70)
win=font.render("YOU WIN",True,(255,215,0))
lose=font.render("YOU LOSE",True,(180,0,0))


game = True
finish =False
do_mon=False

clock=time.Clock()
fps=60

mixer.init()
mixer.music.load("C418.ogg")
mixer.music.play()
eating=mixer.Sound("eating.ogg")
kick=mixer.Sound("kick.ogg")


while game :
    for e in event.get():
        if e.type==QUIT:
            game = False

    if finish != True:
        window.blit(background,(0,0))   
        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()

        if (random==1):

            wall_1.draw_wall()
            wall_2.draw_wall()
            wall_3.draw_wall()
            wall_4.draw_wall()
            wall_5.draw_wall()
            wall_6.draw_wall()
            wall_7.draw_wall()
            wall_8.draw_wall()
            wall_9.draw_wall()
            wall_10.draw_wall()
            wall_11.draw_wall()

        if (random==2):

            wall_1.draw_wall()
            wall_2.draw_wall()
            wall_3.draw_wall()
            wall_4.draw_wall()
            wall_5.draw_wall()
            wall_6.draw_wall()
            wall_7.draw_wall()
            wall_8.draw_wall()
            wall_9.draw_wall()
            wall_10.draw_wall()
            wall_11.draw_wall()
            wall_12.draw_wall()

        if (random==3):

            wall_1.draw_wall()
            wall_2.draw_wall()
            wall_3.draw_wall()
            wall_4.draw_wall()
            wall_5.draw_wall()
            wall_6.draw_wall()
            wall_7.draw_wall()
            wall_8.draw_wall()
            wall_9.draw_wall()
            wall_10.draw_wall()
            wall_11.draw_wall()
            
    keys_pressed=key.get_pressed() 
     

    if keys_pressed[K_w] and player.rect.y > 0: 
        player.rect.y-=speed     
    if keys_pressed[K_s] and player.rect.y < 440: 
        player.rect.y+=speed 
    if keys_pressed[K_a] and player.rect.x > 0: 
        player.rect.x-=speed 
    if keys_pressed[K_d] and player.rect.x < 640: 
        player.rect.x+=speed

    
    if do_mon== True:
        if monster.rect.x < 680: 
            monster.rect.x+=speed-3
        else:
            do_mon=False
    if do_mon == False:
        if monster.rect.x > 580: 
            monster.rect.x-=speed-3
        else:
            do_mon=True


    if (random==1):
        if (sprite.collide_rect(player,monster) 
            or sprite.collide_rect(player,wall_1) 
            or sprite.collide_rect(player,wall_2) 
            or sprite.collide_rect(player,wall_3)
            or sprite.collide_rect(player,wall_4)
            or sprite.collide_rect(player,wall_5)
            or sprite.collide_rect(player,wall_6)
            or sprite.collide_rect(player,wall_7)
            or sprite.collide_rect(player,wall_8)
            or sprite.collide_rect(player,wall_9)
            or sprite.collide_rect(player,wall_10)
            or sprite.collide_rect(player,wall_11) 
            ):

            finish=True
            window.blit(lose,(200,200))
            mixer.music.stop()
            kick.play()
    if (random==2):
        if (sprite.collide_rect(player,monster) 
            or sprite.collide_rect(player,wall_1) 
            or sprite.collide_rect(player,wall_2) 
            or sprite.collide_rect(player,wall_3)
            or sprite.collide_rect(player,wall_4)
            or sprite.collide_rect(player,wall_5)
            or sprite.collide_rect(player,wall_6)
            or sprite.collide_rect(player,wall_7)
            or sprite.collide_rect(player,wall_8)
            or sprite.collide_rect(player,wall_9)
            or sprite.collide_rect(player,wall_10)
            or sprite.collide_rect(player,wall_11)
            or sprite.collide_rect(player,wall_12)
            ):

            finish=True
            window.blit(lose,(200,200))
            mixer.music.stop()
            kick.play()
    if (random==3):
        if (sprite.collide_rect(player,monster) 
            or sprite.collide_rect(player,wall_1) 
            or sprite.collide_rect(player,wall_2) 
            or sprite.collide_rect(player,wall_3)
            or sprite.collide_rect(player,wall_4)
            or sprite.collide_rect(player,wall_5)
            or sprite.collide_rect(player,wall_6)
            or sprite.collide_rect(player,wall_7)
            or sprite.collide_rect(player,wall_8)
            or sprite.collide_rect(player,wall_9)
            or sprite.collide_rect(player,wall_10)
            or sprite.collide_rect(player,wall_11)
            ):     
        
            finish=True
            window.blit(lose,(200,200))
            mixer.music.stop()
            kick.play()

    if sprite.collide_rect(player,final):
        finish=True
        window.blit(win,(200,200))
        eating.play()

    display.update()
    clock.tick(fps)