from pygame import * 
window = display.set_mode((700, 500))
background = transform.scale(image.load("New Piskel.png"), (700, 500))

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y
        self.rect.x = player_x
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Player1(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 330:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 330:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
        self.speed_x = self.speed
        self.speed_y = self.speed
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
sprite1 = Player1("New Piskel (4).png", 25, 100, 20, 170, 10)

sprite2 = Player2("New Piskel (4).png", 650, 100, 20, 170, 10)

ball = Ball("New Piskel (5).png", 350, 250, 50, 50, 5)






game=True
finish = False


while game:
    if finish != True:
        window.blit(background,(0, 0))
        sprite1.update_l()
        sprite1.reset()
        sprite2.update_r()
        sprite2.reset()
        ball.update()
        ball.reset()
    if ball.rect.y < 0 or  ball.rect.y > 460:
        ball.speed_y *= -1
    if ball.rect.x > 640 or ball.rect.x < 0:
        ball.speed_x *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)