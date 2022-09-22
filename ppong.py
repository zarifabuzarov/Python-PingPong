import pygame

pygame.init()

win_width = 600
win_height = 500
FPS = 60

clock = pygame.time.Clock()
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Shooter')

def imgfromtext(text, size, color = (0, 0, 0)):
    return pygame.font.SysFont('Arial', size).render(text, False, color)

class Sprite:
    def __init__(self, window : pygame.display.set_mode, width : int, height : int, images : list() = [], sounds : list() = [], speed : int = 1):
        self.images = list()
        self.sounds = list()
        self.speed = speed
        self.width = width
        self.height = height
        for image in images:
            if type(image) == type(''):
                self.images.append(pygame.transform.scale(pygame.image.load(image), (width, height)))
            else:
                self.images.append(pygame.transform.scale(image, (width, height)))
        self.image = 0
        self.rect = pygame.rect.Rect(0, 0, width, height)
        if self.images:
            self.__upimg__()
        for sound in sounds:
            self.sounds.append(pygame.mixer.Sound(sound))
        self.window = window

    def __upimg__(self):
        self.img = self.images[self.image]
        self.rect = self.img.get_rect()

    def draw(self):
        self.window.blit(self.img, (self.rect.x, self.rect.y))

    def goto(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_img(self, num):
        self.__upimg__()
        if type(num) == type(0):
            self.image = num
        else:
            self.img = num

    def add_img(self, img):
        self.images.append(pygame.transform.scale(img, (width, height)))
        self.__upimg__()

    def collide(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def play(self, num):
        if self.sounds:
            self.sounds[num].play()

    def controls(self, *args):
        keys = pygame.key.get_pressed()
        if keys[args[0]]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
        if keys[args[1]]:
            if (self.rect.x + self.rect.width) < win_width:
                self.rect.x += self.speed
        if keys[args[2]]:
            if self.rect.y > 0:
                self.rect.y -= self.speed
        if keys[args[3]]:
            if (self.rect.y + self.rect.height) < win_height:
                self.rect.y += self.speed

left_racket = Sprite(win, 20, 100, ['racket.png'], [], 5)
right_racket = Sprite(win, 20, 100, ['racket.png'], [], 5)
ball = Sprite(win, 50, 50, ['tenis_ball.png'])

left_racket.goto(100, 200)
right_racket.goto(500, 200)
ball.goto(275, 225)

sy = 3
sx = -3

while True:
    keys = pygame.key.get_pressed()
    left_racket.controls(pygame.K_BACKSPACE, pygame.K_BACKSPACE, pygame.K_w, pygame.K_s)
    right_racket.controls(pygame.K_BACKSPACE, pygame.K_BACKSPACE, pygame.K_UP, pygame.K_DOWN)
    ball.rect.x += sx
    ball.rect.y += sy
    if ball.rect.x < 1 or ball.rect.x+ball.width >= win_width:
        break
    if ball.rect.y < 1 or ball.rect.y+ball.height >= win_height:
        sy *= -1
    if ball.collide(left_racket) or ball.collide(right_racket):
        sx *= -1
        ball.rect.y += sy
    win.fill((200, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    left_racket.draw()
    right_racket.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(FPS)

win.fill((255, 255, 255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()