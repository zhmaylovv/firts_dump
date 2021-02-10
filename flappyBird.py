





















import pygame
import random
import os
import time
import sys

pygame.font.init()

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
STAT_FONT = pygame.font.SysFont('comicsans', 50)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
try:
    pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
    bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
    bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png")).convert_alpha()) for x in range(1,4)]
    base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())
except Exception as e:
    print(e)
    time.sleep(3)

class Bird:
    MAX_ROTATION = 25
    IMGS = bird_images
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        displacement = self.vel*(self.tick_count)+0.5*(3)*(self.tick_count)**2

        if displacement >= 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL
    def draw(self, win):

        self.img_count += 1
        #Анимация самой птички
        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        #Если птичка летит вниз, то не хлопаем крыльями (Егор до такого не додумается)
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2
        #Поворачиваем птицу
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)


class Base:
    VEL = 5
    WIDTH = base_img.get_width()
    IMG = base_img


    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move (self):

        self.x1 -= self.VEL
        self.x2 -= self.VEL
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH
        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH


    def draw (self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))

class Pipe:
    GAP = 200
    VEL = 5
    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img
        self.passed = False

        self.set_height()
    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VEL

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird, win, base):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface((self.PIPE_TOP))
        bottom_mask = pygame.mask.from_surface((self.PIPE_BOTTOM))
        top_offset = self.x - bird.x, self.top - round(bird.y)
        bottom_offset = self.x - bird.x, self.bottom - round(bird.y)

        base_mask = pygame.mask.from_surface((base.IMG))

        b_punch = bird_mask.overlap (bottom_mask, bottom_offset)
        t_punch = bird_mask.overlap (top_mask, top_offset)
        f_punch = bird.y#base_mask.overlap (base_mask, (bird.x, FLOOR))

        if b_punch or t_punch or (bird.y + bird_mask.get_size()[1]) > base.y :
            return True
        return False


def draw_window(win, bird, Base, pipes, score): #pipes, base, score, gen, pipe_ind
    global score_add
    win.blit(bg_img, (0, 0))
    bird.draw(win)
    bird.move()
    Base.draw(win)
    Base.move()
    trash = []
    pipe_pass = False


    for pipe in pipes:


        pipe.move()
        pipe.draw(win)

        if pipe.x < bird.x and len(pipes)<2 :
            pipes.append(Pipe(WIN_WIDTH))

        if pipe.x + pipe_img.get_width() < 0:
            trash.append(pipes[0])



        if pipe.x + pipe_img.get_width() < bird.x:
            pipe.passed = True


    for i in trash:

        pipes.remove(i)
        score_add = False

    score_label = STAT_FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    pygame.display.update()

def draw_screenshot(win, surf_screen):
    win.blit(surf_screen, (0, 0))
    pygame.display.update()







bird = Bird(230, 250)
clock = pygame.time.Clock()
Base = Base(FLOOR)
pipes = [Pipe(700)]
score = 0
score_add = False
screenshot = 0
RUN = True

while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()

            sys.exit()
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
            bird.jump()
    draw_window(WIN, bird, Base, pipes, score)
    clock.tick(30)


    if pipes[0].passed and not score_add:
        score += 1
        score_add = True

    if pipes[0].collide(bird, WIN, Base):

        RUN = False
        score = 0


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()


'''while not RUN:


    draw_screenshot(WIN, surf_screen)
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
    if event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_UP):
        RUN = True'''
'''bird = Bird(230, 250)
bird.draw(WIN)
time.sleep(10)
'''
