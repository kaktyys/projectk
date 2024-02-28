import pygame
import sys

pygame.init()

width, height = 1200, 600
a = 20
v = 25

fonColor = (235, 235, 235)  # 12 51 6
scoreColor = (16, 196, 76)
levelColor = (32, 128, 170)
topscoreColor = (250, 0, 0)

koluchki_up = pygame.image.load('koluchki.png')
koluchki_up_rect = koluchki_up.get_rect()
koluchki_up_rect.left = 0

koluchki_down = pygame.image.load('koluchka.png')
koluchki_down_rect = koluchki_down.get_rect()
koluchki_down_rect.left = 0

clock = pygame.time.Clock()
font = pygame.font.SysFont('', 30)

canvas = pygame.display.set_mode((width, height))
pygame.display.set_caption('My game')


def Start():
    canvas.fill(fonColor)
    start = pygame.image.load('start.png')
    start_rect = start.get_rect()
    start_rect.center = (width / 2, height / 2)
    canvas.blit(start, start_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                Game()
        pygame.display.update()


def Game():
    while True:
        global luchnik
        global score
        luchnik = Luchnik()
        man = Man()
        count = 0
        score = 0
        m = []
        while True:
            canvas.fill(fonColor)
            Level(score)
            luchnik.update()
            count += 1

            if count == v:
                count = 0
                new_flame = Arrow()
                m.append(new_flame)
            for f in m:
                if f.arrow_rect.left <= 0:
                    m.remove(f)
                    score += 1
                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        man.up = True
                        man.down = False
                    elif event.key == pygame.K_DOWN:
                        man.down = True
                        man.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        man.up = False
                        man.down = True
                    elif event.key == pygame.K_DOWN:
                        man.down = True
                        man.up = False

            score_text = font.render('Score:' + str(score), True, scoreColor)
            level_text = font.render('Level:' + str(level), True, levelColor)
            topscore_text = font.render('Top Score:' + str(topscore.topscore), True, topscoreColor)

            score_text_rect = score_text.get_rect()
            level_text_rect = level_text.get_rect()
            topscore_text_rect = topscore_text.get_rect()

            score_text_rect.center = (100, koluchki_up_rect.bottom + score_text_rect.height / 2)
            level_text_rect.center = (550, koluchki_up_rect.bottom + score_text_rect.height / 2)
            topscore_text_rect.center = (1100, koluchki_up_rect.bottom + score_text_rect.height / 2)

            canvas.blit(score_text, score_text_rect)
            canvas.blit(level_text, level_text_rect)
            canvas.blit(topscore_text, topscore_text_rect)
            canvas.blit(koluchki_up, koluchki_up_rect)
            canvas.blit(koluchki_down, koluchki_down_rect)
            man.update()
            for i in m:
                if i.arrow_rect.colliderect(man.man_rect):
                    Finish()
                    if score > man.man_score:
                        man.man_score = score
            pygame.display.update()
            clock.tick(a)


def Level(score):
    global level
    if score in range(0, 10):
        koluchki_up_rect.bottom = 40
        koluchki_down_rect.top = height - 40
        level = 1
    elif score in range(10, 20):
        koluchki_up_rect.bottom = 65
        koluchki_down_rect.top = height - 65
        level = 2
    elif score in range(20, 30):
        koluchki_up_rect.bottom = 90
        koluchki_down_rect.top = height - 90
        level = 3
    elif score in range(30, 45):
        koluchki_up_rect.bottom = 115
        koluchki_down_rect.top = height - 115
        level = 4
    elif score in range(45, 60):
        koluchki_up_rect.bottom = 140
        koluchki_down_rect.top = height - 140
        level = 5
    elif score > 60:
        koluchki_up_rect.bottom = 165
        koluchki_down_rect.top = height - 165
        level = 6


def Finish():
    topscore.top_score(score)
    finish = pygame.image.load('finish.png')
    finish_rect = finish.get_rect()
    finish_rect.center = (width / 2, height / 2)
    canvas.blit(finish, finish_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                Game()
        pygame.display.update()


class Man:
    speedM = 10

    def __init__(self):
        self.man = pygame.image.load('man.png')
        self.man_rect = self.man.get_rect()
        self.man_rect.left = 20
        self.man_rect.top = height / 2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.man, self.man_rect)
        if self.man_rect.top <= koluchki_up_rect.bottom:
            Finish()
            if score > self.man_score:
                self.man_score = score
        if self.man_rect.bottom >= koluchki_down_rect.top:
            Finish()
            if score > self.man_score:
                self.man_score = score
        if self.up:
            self.man_rect.top -= 10
        if self.down:
            self.man_rect.bottom += 10


class Luchnik:
    speedL = 10

    def __init__(self):
        self.luchnik = pygame.image.load('luchnik.png')
        self.luchnik_rect = self.luchnik.get_rect()
        self.luchnik_rect.top = height / 2
        self.luchnik_rect.right = width
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.luchnik, self.luchnik_rect)
        if self.luchnik_rect.bottom >= koluchki_down_rect.top:
            self.up = True
            self.down = False
        elif self.luchnik_rect.top <= koluchki_up_rect.bottom:
            self.up = False
            self.down = True

        if self.up:
            self.luchnik_rect.top -= self.speedL
        elif self.down:
            self.luchnik_rect.top += self.speedL


class Arrow:
    speedA = 20

    def __init__(self):
        self.arrow = pygame.image.load('strela.png')
        self.arrow = pygame.transform.scale(self.arrow, (50, 30))
        self.arrow_rect = self.arrow.get_rect()
        self.arrow_rect.right = luchnik.luchnik_rect.left
        self.arrow_rect.top = luchnik.luchnik_rect.top + 30

    def update(self):
        canvas.blit(self.arrow, self.arrow_rect)

        if self.arrow_rect.left > 0:
            self.arrow_rect.left -= self.speedA


class TopScore:
    def __init__(self):
        self.topscore = 0

    def top_score(self, score):
        if score > self.topscore:
            self.topscore = score
        return self.topscore


topscore = TopScore()
Start()