from pygame import *

rocket_texture = 'rocket.bmp'
ball_texture = 'ball.bmp'
bg_texture = 'galaxy.png'
win_title = 'Ping-pong'
FPS = 60

font.init()
font1 = font.Font(None, 80)
lose = font1.render('Lose', True, (255, 0, 0))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption(win_title)
background = transform.scale(image.load(bg_texture), (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

class Ball(GameSprite):
    def upd(self, t1, t2):
        k = key.get_pressed()
        if k[K_t]:
            self.rect.y -= self.speed
        if k[K_g]:
            self.rect.y += self.speed
        if k[K_f]:
            self.rect.x -= self.speed
        if k[K_h]:
            self.rect.x += self.speed

rocket_player = Player(rocket_texture, win_width - (win_width-5), win_height/2, 10, 100, 15)
rocket_AI = Player(rocket_texture, win_width - 15, win_height/2, 10, 100, 15)
ball = Ball(ball_texture, win_width/2, win_height/2, 25, 25, 5)

run = True
finish = False
delay = int(round(1000/FPS))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0,0))
        rocket_player.update_l()
        rocket_AI.update_r()
        ball.upd()

    rocket_player.reset()
    rocket_AI.reset()
    ball.reset()
    display.update()
    time.delay(delay)