import os
import sys
from random import randint as r, choice as ch

import pygame

from constnts import *

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()


def start_screen():
    pygame.mixer.music.load("data/soundtrack.mp3")
    pygame.mixer.music.play(-1, 3)
    pygame.mixer.music.set_volume(0.3)
    fon = pygame.transform.scale(load_image('start_screen.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 350
    for line in INTRO_TEXT:
        string_rendered = font.render(line, True, GOLD)
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                return
        pygame.display.flip()
        clock.tick(FPS)


def get_result():
    with open(RESULTS) as file:
        max_result = max([int(x) for x in file])
    return max_result


def write_result(spider):
    with open(RESULTS, "a", encoding="utf8") as file:
        file.write(str(spider.points) + "\n")


def lose_screen(spider):
    LOSE_SOUND.play(0)
    write_result(spider)
    fon = pygame.transform.scale(load_image(LOSE_SCREEN), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    new_text = [f'Результат: {spider.points}', f"Рекорд: {get_result()}"]
    new_text_coord = 430
    for line in new_text:
        string_rendered = font.render(line, True, GOLD)
        points_rect = string_rendered.get_rect()
        points_rect.top = new_text_coord
        points_rect.x = WIDTH - 175
        new_text_coord += points_rect.height
        screen.blit(string_rendered, points_rect)
    text = "Для продолжения нажмите пробел"
    font = pygame.font.SysFont(None, 25)
    text_coord = HEIGHT
    string_rendered = font.render(text, True, RED, BLACK)
    text_rect = string_rendered.get_rect()
    text_rect.top = text_coord - text_rect.height
    text_rect.x = WIDTH // 2 - text_rect.width // 2
    screen.blit(string_rendered, text_rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    LOSE_SOUND.stop()
                    return
        pygame.display.flip()
        clock.tick(FPS)


def win_screen(spider):
    write_result(spider)
    WIN_SOUND.play()
    fon = pygame.transform.scale(load_image(WIN_SCREEN), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    new_text = [f'Результат: {spider.points}', f"Рекорд: {get_result()}"]
    new_text_coord = 430
    for line in new_text:
        string_rendered = font.render(line, True, GOLD, BLACK)
        points_rect = string_rendered.get_rect()
        points_rect.top = new_text_coord
        points_rect.x = WIDTH - 175
        new_text_coord += points_rect.height
        screen.blit(string_rendered, points_rect)
    text = "Для продолжения нажмите пробел"
    font = pygame.font.SysFont(None, 25)
    text_coord = HEIGHT
    string_rendered = font.render(text, True, RED, BLACK)
    text_rect = string_rendered.get_rect()
    text_rect.top = text_coord - text_rect.height
    text_rect.x = WIDTH // 2 - text_rect.width // 2
    screen.blit(string_rendered, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
        pygame.display.flip()
        clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def get_info(spider, screen):
    global LEVEL, heart_group
    text = f"Points: {spider.points}"
    font = pygame.font.SysFont(COMICS_FONT, 15)
    text_coord = 40
    string_rendered = font.render(text, True, BLUE)
    text_rect = string_rendered.get_rect()
    text_rect.top = text_coord
    text_rect.x = 15
    screen.blit(string_rendered, text_rect)
    font = pygame.font.SysFont(COMICS_FONT, 20)
    new_text = f'Lvl {LEVEL}'
    new_text_coord = 10
    color = BLACK if LEVEL <= 4 else RED
    string_rendered = font.render(new_text, True, color)
    level_rect = string_rendered.get_rect()
    level_rect.top = new_text_coord
    level_rect.x = WIDTH - level_rect.width * 1.2
    screen.blit(string_rendered, level_rect)
    heart_group = pygame.sprite.Group()
    for i in range(spider.lives):
        Heart(i)


def instruction_screen():
    global GAME
    GAME = True
    fon = pygame.transform.scale(load_image(INSTRUCTION), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def run_game():
    global spLeft, spRight, spUp, all_sprites, GVENS_SPEED_Y, BONUS_SPEED_Y
    global BONUS_PAUSE, FALL_PAUSE, main_run, LEVEL, spDown
    pygame.mixer.music.load("data/soundtrack.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 20)
    all_sprites = pygame.sprite.Group()
    LEVEL = 1
    GVENS_SPEED_Y = 5
    BONUS_SPEED_Y = 6
    BONUS_PAUSE = 10000
    FALL_PAUSE = 3000
    START_FON = False
    spLeft = spRight = False
    spider = Spider()
    run = True
    fon = pygame.transform.scale(load_image(BACKGROUND), (WIDTH, HEIGHT))
    pygame.time.set_timer(FALL_TIME, FALL_PAUSE)
    pygame.time.set_timer(BONUS_TIME, BONUS_PAUSE)
    pygame.time.set_timer(SPECIAL_GVEN_TIME, SPECIAL_GVEN_PAUSE)
    while run:
        screen.blit(fon, (0, 0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    spLeft = True
                if event.key == pygame.K_RIGHT:
                    spRight = True
                if event.key == pygame.K_UP:
                    spUp = True
                if event.key == pygame.K_DOWN:
                    spDown = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    spLeft = False
                if event.key == pygame.K_RIGHT:
                    spRight = False
                if event.key == pygame.K_UP:
                    spUp = False
                if event.key == pygame.K_DOWN:
                    spDown = False
            if event.type == FALL_TIME:
                Gven(GVENS_SPEED_Y)
            if event.type == BONUS_TIME:
                Bonus(BONUS_SPEED_Y, ch(BONUSES))
            if event.type == SPECIAL_GVEN_TIME:
                Bonus(SPECIAL_GVENS_SPEED_Y, ch(SPECIAL_GVENS))
        if spider.lives <= 0:
            pygame.mixer.music.stop()
            lose_screen(spider)
            run = False
        if spider.points >= 10000:
            pygame.mixer.music.stop()
            win_screen(spider)
            run = False
        if LEVEL >= 5 and not START_FON:
            fon = pygame.transform.scale(load_image(ICON), (WIDTH, HEIGHT))
            START_FON = True
        get_info(spider, screen)
        all_sprites.draw(screen)
        heart_group.draw(screen)
        all_sprites.update(spider)
        pygame.display.flip()


def load_image(name, colorkey=None):
    fullname = os.path.join(DIRECTORY, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Heart(pygame.sprite.Sprite):
    def __init__(self, coord):
        super().__init__(heart_group)
        self.image = pygame.transform.scale(load_image(HEART), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 0 + self.rect.width * coord * 0.5
        self.rect.y = -10


class Gven(pygame.sprite.Sprite):
    def __init__(self, speed_y):
        super().__init__(all_sprites, gven_group)
        self.frames = []
        self.image = load_image(GVEN)
        self.get_gvens()
        self.cur_frame = 0
        self.size = SIZES[GVEN]
        self.image = pygame.transform.scale(self.frames[self.cur_frame], self.size)
        self.rect = self.image.get_rect()
        self.rect.x = r(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = speed_y

    def update(self, spider):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], self.size)
        if LEVEL >= 5:
            self.rect.x += r(-5, 5)
        self.rect.y += self.speed_y
        if pygame.sprite.collide_mask(self, spider):
            SAVE_SOUND.play()
            self.kill()
            spider.win()
        if self.rect.y >= HEIGHT:
            spider.lose()
            self.kill()
            if spider.lives > 0:
                MISS_SOUND.play(0)

    def get_gvens(self):
        for i in range(0, 360, 3):
            self.frames.append(pygame.transform.rotate(self.image, i))


class Bonus(pygame.sprite.Sprite):
    def __init__(self, speed_y, value):
        super().__init__(all_sprites)
        self.value = value
        self.image = pygame.transform.scale(load_image(f'{value}.png'), SIZES[self.value])
        self.rect = self.image.get_rect()
        self.rect.x = r(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = speed_y

    def update(self, spider):
        self.rect.x += r(*DELTA_X[self.value])
        self.rect.y += self.speed_y
        if pygame.sprite.collide_mask(self, spider):
            if self.value == BONUSES_TYPES[0]:
                HEART_SOUND.play()
                spider.add_live()
                self.kill()
            elif self.value == BONUSES_TYPES[1]:
                spider.lose()
                MINUS_HEART_SOUND.play(0)
                self.kill()
            elif self.value == BONUSES_TYPES[2]:
                SPEED_SOUND.play()
                spider.speed_x += 1 if spider.speed_x <= 10 else 0
                spider.speed_y += 1
                self.kill()
            elif self.value == BONUSES_TYPES[3]:
                for _ in range(5):
                    spider.win()
                self.kill()
            elif self.value == BONUSES_TYPES[4]:
                for _ in range(10):
                    spider.win()
                self.kill()
        if self.rect.y >= HEIGHT:
            self.kill()


class Level(pygame.sprite.Sprite):
    def __init__(self):
        global LEVEL, LEVELS_SPEED, screen, GOLD, BLACK, RED, BLUE
        super().__init__(all_sprites)
        self.text = f"--level {LEVEL}--"
        font = pygame.font.SysFont(COMICS_FONT, 50)
        self.image = font.render(self.text, True, BLUE, RED)
        self.rect = self.image.get_rect()
        self.rect.y -= self.rect.height
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.screen = screen
        self.speed_y = LEVELS_SPEED

    def update(self, spider):
        self.screen.blit(self.image, self.rect)
        self.rect.y += self.speed_y
        if self.rect.y >= HEIGHT:
            self.kill()


class Spider(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(load_image(SPIDER), (50, 60))
        self.rect = self.image.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.rect.x = WIDTH // 2 - self.w
        self.rect.y = HEIGHT - self.h
        self.speed_x = 5
        self.speed_y = 3
        self.lives = 3
        self.points = 0

    def update(self, spider):
        if spLeft:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.rect.x - self.speed_x >= 0:
                self.rect = self.rect.move(-self.speed_x, 0)
            else:
                self.rect.x = 0
        if spRight:
            self.image = pygame.transform.flip(self.image, True, False)
            if self.rect.x + self.speed_x <= WIDTH - self.w:
                self.rect = self.rect.move(self.speed_x, 0)
            else:
                self.rect.x = WIDTH - self.rect.width
        if spUp:
            self.rect = self.rect.move(0, -self.speed_y)
        if spDown:
            if self.rect.y + self.speed_y + self.rect.height <= HEIGHT:
                self.rect = self.rect.move(0, self.speed_y)
            else:
                self.rect.y = HEIGHT - self.rect.height
        if self.rect.y + self.rect.height < HEIGHT and not (self.rect.x + self.rect.width == WIDTH or \
                                                            self.rect.x == 0):
            self.rect = self.rect.move(0, self.speed_y)

    def lose(self):
        self.lives -= 1

    def win(self):
        global GVENS_SPEED_Y, FALL_PAUSE, FALL_TIME, BONUS_SPEED_Y, LEVEL
        self.points += 100
        if self.points >= 1000 and self.points % 1000 == 0:
            LEVEL += 1
            NEW_LEVEL_SOUND.play(0)
            Level()
            GVENS_SPEED_Y += 1
            BONUS_SPEED_Y += 1
            if FALL_PAUSE >= 2000:
                FALL_PAUSE -= 80
            pygame.time.set_timer(FALL_TIME, FALL_PAUSE)
            BONUSES.append('bomb')
            if self.points == 4000:
                self.image = pygame.transform.scale(load_image(BLACK_SPIDER), (50, 60))

    def add_live(self):
        self.lives += 1


img = load_image(ICON)
pygame.display.set_icon(img)

if __name__ == "__main__":
    while main_run:
        start_screen()
        if not GAME:
            instruction_screen()
        run_game()

pygame.quit()
