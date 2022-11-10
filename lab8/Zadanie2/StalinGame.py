#Правила: расстреливай антисоветские элементы, нажимая на F, нажми на F и SPACE, чтобы устроить массовые репрессии
#Чтобы двигаться, нажимай на кнопки RIGHT, LEFT, UP, DOWN
#Ecли запятнаешься связями с антисоветскими элементами, проиграешь

import math
import pygame as pg
from random import randint

import pygame.display

WIDTH, HEIGHT = 500, 500
FONE_COLOR = (155, 155, 155)
FPS = 30
pg.init()
pygame.display.set_caption("Сталинские репрессии")

f_score = pg.font.Font(None, 36)
f_good_click1 = pg.font.Font(None, 30)
f_good_click2 = pg.font.Font(None, 32)
screen = pg.display.set_mode((WIDTH, HEIGHT))

x = 50
y = 50
width = 100
height = 50
speed = 1
isJump = False
Jump = 7
bullets = []
napravlenie = "right"


class Ball:

    def __init__(self, radius_min=10, radius_max=30, speed_max=5):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)
        self.radius = randint(radius_min, radius_max)
        self.speed_x = randint(-speed_max, speed_max)
        self.speed_y = randint(-speed_max, speed_max)
        self.timeCreate = pg.time.get_ticks()
        colors = [(255, 255, 0), (0, 255, 0)]
        type = randint(0, 1)
        self.type = type
        self.color = colors[type]
        self.speed_max = speed_max


    def wall_collision(self):
        """
        Проверка на столкновение со стенами
        """
        if self.x - self.radius < 0:
            self.speed_x = randint(0, self.speed_max)
        elif self.x + self.radius > WIDTH:
            self.speed_x = randint(-self.speed_max, 0)
        elif self.y - self.radius < 0:
            self.speed_y = randint(0, self.speed_max)
        elif self.y + self.radius > HEIGHT:
            self.speed_y = randint(-self.speed_max, 0)

    def update(self, FPS : int):
        """
        Обработка логики шарика
        """
        self.wall_collision()

        self.x += self.speed_x/FPS
        self.y += self.speed_y/FPS

        if self.type == 1:
            k = 1
            if self.speed_x < 0:
                k = -1
            self.speed_x =  k * self.speed_max * (math.sin(self.timeCreate/500))**2
            if self.speed_y < 0:
                k = -1
            self.speed_y =  k * self.speed_max * (math.cos(self.timeCreate/500))**2

    def getScore(self):
        """
        Возращает количество очков за мячик
        """
        if self.type == 1:
            return 1
        return 3

    def render(self, surface : pg.Surface):
        """
        Отрисовывает мячик
        """
        pg.draw.circle(surface, self.color, (self.x, self.y), self.radius)



class Word:
    click_words = ["Контра!", "Враг народа!", "Троцкист!", "Кулак!", "Фашистское отродье!"]
    timeLive = 1000

    def __init__(self, countGoodClick : int, time, position):
        self.word1 = f_good_click1.render(self.GetGoodWord(countGoodClick), True, (0, 255, 255))
        self.word2 = f_good_click2.render(self.GetGoodWord(countGoodClick), True, (0, 0, 0))
        self.time = time
        self.position = position

    def GetGoodWord(self, countGoodClick : int):
        """
        Возращает слово, в зависимости от количества попаданий подряд
        """
        l = len(self.click_words)
        if countGoodClick >= l:
            return self.click_words[l-1]
        return self.click_words[countGoodClick]

    def render(self, surface : pg.Surface):
        """
        Отрисовка слова
        """
        surface.blit(self.word2, self.position)
        surface.blit(self.word1, self.position)

    def update(self):
        """
        Обработка логики слова
        """
        kMove = (1 - (pg.time.get_ticks() - self.time)/ self.timeLive) / FPS
        self.position = (self.position[0], self.position[1] - kMove)

    def itBe(self):
        """Проверка истечение срока жизни слова"""
        return pg.time.get_ticks() < self.time + self.timeLive

class snaryad:

    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = facing
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + 25, self.y + 25), self.radius)

    def hit(self, obj):
        return (self.x - obj.x)**2 + (self.y - obj.y)**2 <= (self.radius + obj.radius)**2


balls = []
words = []
lastCreate = 0
delayCreate = 0
good_click_count = 0
score = 0

def CreateBall():
    """
    Создание мячика
    """
    balls.append(Ball())

def CreateWord(goodClickCount : int, position):
    """Создание слова"""
    words.append(Word(goodClickCount, pg.time.get_ticks(), position))


def update():
    """Обработка логики игры (Ядро)"""
    global lastCreate, delayCreate, balls, FPS

    for ball in balls:
        ball.update(FPS)

    for word in words:
        if not word.itBe():
            words.remove(word)
            continue
        word.update()

    if pg.time.get_ticks() > (lastCreate + delayCreate):
        lastCreate = pg.time.get_ticks()
        delayCreate = randint(1000, 2000)
        CreateBall()

def render(screen):
    """Отрисовка экрана"""
    global balls, facing
    screen.blit(pygame.image.load('USSR.jpg'), (0, 0))
    screen.blit(pygame.image.load('Stalin.jpg'), (x, y))
    keys = pygame.key.get_pressed()
    textScore = f_score.render("Расстреляно: " + str(score), True, (200, 0, 0))
    if keys[pygame.K_f]:

        if napravlenie == "right":
            facing = 1
        elif napravlenie == "left":
            facing = -1
        bullets.append(snaryad(round(x), round(y), 5, 'red', facing))
    for bullet in bullets:
        bullet.draw(screen)
    for ball in balls:
        ball.render(screen)

    for word in words:
        word.render(screen)

    screen.blit(textScore, (0,0))

    pg.display.update()



running = True
while running:
    render(screen)

    for bullet in bullets:
        for ball in balls:
            if bullet.hit(ball):
                balls.remove(ball)
                score += 1
                position = [ball.x, ball.y]
                i = randint(0, 5)
                CreateWord(i, position)

        if 0 < bullet.x < 495:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 445:
        x += speed
        napravlenie = "right"
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        napravlenie = "left"
    if not (isJump):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 445:
            y += speed
        if keys[pygame.K_SPACE] and y > 50:
            isJump = True
    else:

        if Jump >= 0:
            pygame.time.delay(10)
            y -= (Jump ** 2)
            Jump -= 1
        elif 0 > Jump >= -7:
            pygame.time.delay(10)
            y += (Jump ** 2)
            Jump -= 1
        else:
            isJump = False
            Jump = 7
    for ball in balls:
        if ((x - ball.x) ** 2 + (y - ball.y) ** 2 <= (ball.radius) ** 2) or (
                (x + 50 - ball.x) ** 2 + (y - ball.y) ** 2 <= (ball.radius) ** 2):
            running = False
        elif ((x - ball.x)**2 + (y + 50 - ball.y)**2 <= (ball.radius)**2) or (
                (x + 50 - ball.x) ** 2 + (y + 50 - ball.y) ** 2) <= (ball.radius) ** 2:
            running = False
    update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()
