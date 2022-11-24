import math
from random import choice
from random import randint
import pygame
import pygame.display
pygame.init()
f_score = pygame.font.Font(None, 36)
FPS = 60
pygame.display.set_caption("Пушка")
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 800
HEIGHT = 600
A = 50
B = HEIGHT - 80
x = 60
y = HEIGHT - 30
class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x + A
        self.y = B
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        if self.y < HEIGHT - self.r:
            self.vy -= 10/FPS
        self.x += self.vx
        self.y -= self.vy
        if self.x < self.r:
            self.vx *= -1
        if self.x > WIDTH - self.r:
            self.vx *= -1
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy *= -0.8
            self.vx *= 0.9
        if self.y < self.r:
            self.vy *= -1


    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        return (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 < (self.r + obj.r - 5)**2


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 5

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self, A, B):
        pygame.draw.line(screen, GREY, (x, y), (x + A, B), 20)
        pygame.draw.circle(screen, (100, 100, 100), (x-10, y), 20)
        pygame.draw.ellipse(screen, GREY, (x - 60, y, 100, 40))
        pygame.draw.circle(screen, BLACK, (x - 40, y + 20), 10)
        pygame.draw.circle(screen, BLACK, (x - 10, y + 20), 10)
        pygame.draw.circle(screen, BLACK, (x + 20, y + 20), 10)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        speed_max = 50
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(30, 50)
        self.color = choice(GAME_COLORS)
        self.live = 1
        self.speed_max = speed_max
        self.type = type
        self.speed_x = randint(-speed_max, speed_max)
        self.speed_y = randint(-speed_max, speed_max)
        self.timeCreate = pygame.time.get_ticks()
    # FIXME: don't work!!! How to call this functions when object is created?

    def target_hittest(self):
        """
        Проверка на столкновение со стенами
        """
        if self.x - self.r < 0:
            self.speed_x = randint(0, self.speed_max)
        elif self.x + self.r > WIDTH:
            self.speed_x = randint(-self.speed_max, 0)
        elif self.y - self.r < 0:
            self.speed_y = randint(0, self.speed_max)
        elif self.y + self.r > HEIGHT:
            self.speed_y = randint(-self.speed_max, 0)

    def go(self, FPS : int):
        """
        Обработка логики шарика
        """
        self.target_hittest()

        self.x += self.speed_x/FPS
        self.y += self.speed_y/FPS

        k = 1
        if self.speed_x < 0:
            k = -1
        self.speed_x =  k * self.speed_max * (math.sin(self.timeCreate/500))**2
        if self.speed_y < 0:
            k = -1
        self.speed_y =  k * self.speed_max * (math.cos(self.timeCreate/500))**2


    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)




pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
score = 0
balls = []
lastCreate = 0
delayCreate = 10000
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
finished = False
tg = [target1, target2]
while not finished:
    screen.blit(pygame.image.load('post-29-1325673135.jpg'), (0, 0))
    screen.blit(f_score.render("Счёт: " + str(score), True, (200, 0, 0)), (0,0))
    gun.draw(A, B)

    for target in tg:
        target.draw()
        target.go(FPS)
    for b in balls:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
            if event.pos[0] > x:
                A = 50* math.cos(math.atan((event.pos[1]-450) / (event.pos[0])))
                B = HEIGHT - 80 + 50 * math.sin(math.atan((event.pos[1]-450) / (event.pos[0])))
            elif event.pos[0] <= x:
                A = -50 * math.cos(math.atan((event.pos[1] - 450) / (event.pos[0])))
                B = HEIGHT - 80 + 50 * math.sin(math.atan((event.pos[1] - 450) / (event.pos[0])))
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    for b in balls:
        b.move()
        for target in tg:
            if b.hittest(target) and target.live:
                target.live = 0
                score += 1
                tg.remove(target)
                tg.append(Target())
        if pygame.time.get_ticks() > (lastCreate + delayCreate):
            lastCreate = pygame.time.get_ticks()
            balls.remove(b)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and x < 740:
        x += 10
    if keys[pygame.K_LEFT] and x > 60:
        x -= 10

    gun.power_up()
pygame.quit()
