from pygame import *








class GameSprite(sprite.Sprite):
    def __init__(self, pic_name, start_x, start_y, speed, dim_x, dim_y):
        super().__init__()
        self.picture = transform.scale(image.load(pic_name), (dim_x, dim_y))
        self.speed = speed
        self.rect = self.picture.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

    def reset(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed






window = display.set_mode((600, 500))
a = transform.scale(image.load("racket.png"), (600, 500))


r1 = Player("racket.png", 30, 200, 4, 50, 100)
r2 = Player("racket.png", 520, 200, 4, 50, 100)

ball = GameSprite("tenis_ball.png", 200, 200, 4, 30, 30)


game = True
finish = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(a, (0,0))
        r1.update()
        r2.update()
        r1.reset()
        r2.reset()
        ball.reset()

    display.update()
    clock.tick(60)