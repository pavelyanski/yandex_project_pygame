from auxiliary_functions import *


def initialization():
    global clock, screen
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(CAPTION)
    img = load_image(ICON)
    pygame.display.set_icon(img)
    clock = pygame.time.Clock()


def start_screen():
    global clock
    pygame.mixer.music.load(SOUNDTRACK)
    pygame.mixer.music.play(-1, 3)
    pygame.mixer.music.set_volume(0.3)
    fon = pygame.transform.scale(load_image(START_SCREEN), (WIDTH, HEIGHT))
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
    text = choose_hint()
    font = pygame.font.SysFont(None, 24)
    text_coord = HEIGHT
    string_rendered = font.render(text, True, RED)
    text_rect = string_rendered.get_rect()
    text_rect.top = text_coord - text_rect.height
    text_rect.x = WIDTH // 2 - text_rect.width // 2
    screen.blit(string_rendered, text_rect)

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


def pause_screen():
    pygame.mixer.music.load(SOUNDTRACK)
    pygame.mixer.music.play(-1, 3)
    pygame.mixer.music.set_volume(0.3)
    fon = pygame.transform.scale(load_image(PAUSE_SCREEN), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    text = "Для продолжения нажмите P"
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
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                pygame.mixer.music.stop()
                return
        pygame.display.flip()
        clock.tick(FPS)


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
    spider.points = 10000 if spider.points < 10000 else spider.points
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
                    WIN_SOUND.stop()
                    return
        pygame.display.flip()
        clock.tick(FPS)


def get_info(spider, screen):
    global level, heart_group
    text = f"Points: {spider.points}"
    font = pygame.font.SysFont(COMICS_FONT, 15)
    text_coord = 40
    string_rendered = font.render(text, True, BLUE)
    text_rect = string_rendered.get_rect()
    text_rect.top = text_coord
    text_rect.x = 15
    screen.blit(string_rendered, text_rect)
    font = pygame.font.SysFont(COMICS_FONT, 20)
    new_text = f'Lvl {level}'
    new_text_coord = 10
    color = BLACK if level <= 4 else RED
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
    global spLeft, spRight, spUp, all_sprites, gvens_speed_y, bonus_speed_y
    global main_run, spDown, level, bonuse_pause, fall_pause
    pygame.mixer.music.load(SOUNDTRACK)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1, 20)
    all_sprites = pygame.sprite.Group()
    level = 1
    gvens_speed_y = 5
    bonus_speed_y = 6
    bonus_pause = 10000
    fall_pause = 3000
    start_fon = False
    spLeft = spRight = False
    spider = Spider()
    run = True
    fon = pygame.transform.scale(load_image(BACKGROUND), (WIDTH, HEIGHT))
    pygame.time.set_timer(FALL_TIME, fall_pause)
    pygame.time.set_timer(BONUS_TIME, bonus_pause)
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
                if event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                    pause_screen()
                    pygame.mixer.music.play()
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
                Gven(gvens_speed_y)
            if event.type == BONUS_TIME:
                Bonus(bonus_speed_y, choice(BONUSES))
            if event.type == SPECIAL_GVEN_TIME:
                Bonus(SPECIAL_GVENS_SPEED_Y, choice(SPECIAL_GVENS))
        if spider.rect.y <= -1300:
            spider.points = 10000
        if spider.lives <= 0:
            pygame.mixer.music.stop()
            run = False
            lose_screen(spider)
        if spider.points >= 10000:
            pygame.mixer.music.stop()
            run = False
            win_screen(spider)
        if level >= 5 and not start_fon:
            fon = pygame.transform.scale(load_image(ICON), (WIDTH, HEIGHT))
            start_fon = True
        get_info(spider, screen)
        all_sprites.draw(screen)
        heart_group.draw(screen)
        all_sprites.update(spider)
        pygame.display.flip()


def create_particles(position, image, first_size=(30, 30), sizes=(20, 25)):
    for _ in range(PARTICLE_COUNT):
        Particle(position, choice(NUMBERS), choice(NUMBERS), image, first_size, sizes)


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
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = speed_y

    def update(self, spider):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = pygame.transform.scale(self.frames[self.cur_frame], self.size)
        if level >= 5:
            self.rect.x += randint(-5, 5)
        self.rect.y += self.speed_y
        if pygame.sprite.collide_mask(self, spider):
            SAVE_SOUND.play()
            create_particles((spider.rect.x, self.rect.y), GVEN, *PARTICLE_SIZES[GVEN])
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
        self.rect.x = randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_y = speed_y

    def update(self, spider):
        self.rect.x += randint(*DELTA_X[self.value])
        self.rect.y += self.speed_y
        if pygame.sprite.collide_mask(self, spider):
            if self.value == BONUSES_TYPES[0]:
                HEART_SOUND.play()
                create_particles((self.rect.x, self.rect.y), HEART)
                spider.add_live()
                self.kill()
            elif self.value == BONUSES_TYPES[1]:
                spider.lose()
                create_particles((self.rect.x, self.rect.y), BOMB)
                MINUS_HEART_SOUND.play(0)
                self.kill()
            elif self.value == BONUSES_TYPES[2]:
                SPEED_SOUND.play()
                create_particles((self.rect.x, self.rect.y), SPEED, *PARTICLE_SIZES[SPEED])
                spider.speed_x += 1 if spider.speed_x <= 10 else 0
                spider.speed_y += 1
                self.kill()
            elif self.value == BONUSES_TYPES[3]:
                create_particles((self.rect.x, self.rect.y), GOLD_COIN, *PARTICLE_SIZES[GOLD_COIN])
                for _ in range(5):
                    spider.win()
                self.kill()
            elif self.value == BONUSES_TYPES[4]:
                create_particles((self.rect.x, self.rect.y), DIAMOND, *PARTICLE_SIZES[DIAMOND])
                for _ in range(10):
                    spider.win()
                self.kill()
        if self.rect.y >= HEIGHT:
            self.kill()


class Level(pygame.sprite.Sprite):
    def __init__(self):
        global level, LEVELS_SPEED, screen, GOLD, BLACK, RED, BLUE
        super().__init__(all_sprites)
        self.text = f"--level {level}--"
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
    def __init__(self):
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
        if spUp and (self.rect.x + self.rect.width == WIDTH or self.rect.x == 0):
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
        global gvens_speed_y, fall_pause, FALL_TIME, bonus_speed_y, level
        self.points += 100
        if self.points >= 1000 and self.points % 1000 == 0:
            level += 1
            NEW_LEVEL_SOUND.play(0)
            Level()
            gvens_speed_y += 1
            bonus_speed_y += 1
            if fall_pause >= 2000:
                fall_pause -= 80
            pygame.time.set_timer(FALL_TIME, fall_pause)
            BONUSES.append('bomb')
            if self.points == 4000:
                self.image = pygame.transform.scale(load_image(BLACK_SPIDER), (50, 60))

    def add_live(self):
        self.lives += 1


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dx, dy, image, first_size, sizes):
        self.fire = [pygame.transform.scale(load_image(image), first_size)]
        for scale in sizes:
            self.fire.append(pygame.transform.scale(self.fire[0], (scale, scale)))
        super().__init__(all_sprites)
        self.image = choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self, spider):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(SCREEN_RECT):
            self.kill()


if __name__ == "__main__":
    initialization()
    LOSE_SOUND = pygame.mixer.Sound("data/sounds/lose_sound.ogg")
    MISS_SOUND = pygame.mixer.Sound("data/sounds/miss_sound.ogg")
    NEW_LEVEL_SOUND = pygame.mixer.Sound("data/sounds/new_level_sound.ogg")
    MINUS_HEART_SOUND = pygame.mixer.Sound("data/sounds/minus_heart.ogg")
    SPEED_SOUND = pygame.mixer.Sound("data/sounds/speed_sound.ogg")
    HEART_SOUND = pygame.mixer.Sound("data/sounds/heart_sound.ogg")
    WIN_SOUND = pygame.mixer.Sound("data/sounds/win_sound.ogg")
    SAVE_SOUND = pygame.mixer.Sound("data/sounds/save_sound.ogg")
    MISS_SOUND.set_volume(1)
    LOSE_SOUND.set_volume(0.2)
    NEW_LEVEL_SOUND.set_volume(0.3)
    MINUS_HEART_SOUND.set_volume(0.2)
    SPEED_SOUND.set_volume(1)
    HEART_SOUND.set_volume(1)
    WIN_SOUND.set_volume(0.2)
    SAVE_SOUND.set_volume(0.4)
    while main_run:
        start_screen()
        if not GAME:
            instruction_screen()
        run_game()

pygame.quit()
