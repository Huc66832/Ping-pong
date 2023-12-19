from pygame import *
import time as tt

racket_texture = 'racket.bmp'
AI_racket_texture = 'AI_racket.bmp'
ball_texture = 'ball.bmp'
bg_texture = 'galaxy.png'
win_title = 'Ping-pong'
FPS = 60
mx = 1
my = 1
score = 0
b_speed = 7
t_start = tt.time()

font.init()
font1 = font.Font(None, 20)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption(win_title)
background = transform.scale(image.load(bg_texture), (win_width, win_height))

class GameSprite(sprite.Sprite):
    def __init__(self, self_image, self_x, self_y, size_x, size_y, self_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(self_image), (size_x, size_y))
        self.speed = self_speed
        self.rect = self.image.get_rect()
        self.rect.x = self_x
        self.rect.y = self_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def update_r(self, b):
        self.rect.y = b.rect.y

class Ball(GameSprite):
    def upd(self):
        global my
        global mx
        global score
        global b_speed
        self.rect.x -= b_speed * mx
        self.rect.y += b_speed * my
        if self.rect.y <= 7 or self.rect.y >= win_height - 7:
            my *= -1


racket_player = Racket(racket_texture, win_width - (win_width - 5), win_height / 2, 10, 100, 15)
racket_AI = Racket(AI_racket_texture, win_width - 15, win_height/2, 10, 10, 15)
ball = Ball(ball_texture, win_width/2, win_height/2, 10, 10, 3)

run = True
finish = False
delay = int(round(1000/FPS))

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.blit(background, (0, 0))
        racket_player.update_l()
        racket_AI.update_r(ball)
        ball.upd()

    if sprite.collide_rect(ball, racket_player) or sprite.collide_rect(ball, racket_AI):
        mx *= -1

    if ball.rect.x <= 5:
        ball.rect.x = win_width/2
        ball.rect.y = win_height/2
        my *= -1
        score += 1
        t_start = tt.time()

    timer = round(tt.time() - t_start, 1)
    text_score = font1.render(f'Loses: {score}', True, (255, 255, 255))
    t_time = font1.render(f'{timer}', True, (255, 255, 255))
    window.blit(text_score, (10, 10))
    window.blit(t_time, (win_width/2, 10))
    racket_player.reset()
    racket_AI.reset()
    ball.reset()

    display.update()
    time.delay(delay)
