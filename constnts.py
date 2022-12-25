import pygame

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
main_run = True
FPS = 60
SIZE = WIDTH, HEIGHT = 500, 500
SCREEN_RECT = (0, 0, WIDTH, HEIGHT)
BLACK = pygame.Color("black")
RED = pygame.Color("red")
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")
GOLD = pygame.Color("#ffd700")
spLeft = spRight = spUp = spDown = False
GVENS_SPEED_Y = 5
SPECIAL_GVENS_SPEED_Y = 10
LEVEL = 1
BONUS_SPEED_Y = 6
LEVELS_SPEED = 8
FALL_TIME = pygame.USEREVENT + 1
BONUS_TIME = pygame.USEREVENT + 2
SPECIAL_GVEN_TIME = pygame.USEREVENT + 3
BONUS_PAUSE = 10000
FALL_PAUSE = 3000
SPECIAL_GVEN_PAUSE = 80000
PARTICLE_COUNT = 25
NUMBERS = range(-5, 6)
SIZES = {"hp": (100, 100), "speed": (130, 130), "bomb": (100, 100), "gold_gven": (130, 130), "diamond_gven": (120, 120),
         "gven.png": (160, 160)}
DELTA_X = {"hp": (-3, 3), "speed": (-3, 3), "bomb": (-3, 3), "gold_gven": (-10, 10), "diamond_gven": (-10, 10)}
BONUSES = ["bomb", "hp", "speed", "bomb"]
SPECIAL_GVENS = ["gold_gven", "gold_gven", "diamond_gven"]
all_sprites = pygame.sprite.Group()
gven_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
GAME = False
ICON = "icon.jpg"
SPIDER = "spider.png"
GVEN = "gven.png"
HEART = "hp.png"
BOMB = "bomb.png"
SPEED = "speed.png"
GOLD_COIN = "gold_coin.png"
DIAMOND = "diamond.png"
PARTICLE_SIZES = {"speed.png": ((60, 60), (50, 55)), "gold_coin.png": ((40, 40), (30, 35)),
                  "diamond.png": ((80, 80), (70, 75))}
BLACK_SPIDER = "black_spider.png"
BACKGROUND = "background.jpg"
INSTRUCTION = "instruction.jpg"
COMICS_FONT = "comicsansms"
WIN_SCREEN = "win_screen.jpg"
START_SCREEN = "start_screen.png"
LOSE_SCREEN = "lose_screen.jpg"
PAUSE_SCREEN = "pause_screen.jpg"
DIRECTORY = "data"
RESULTS = "data/results.txt"
BONUSES_TYPES = ("hp", "bomb", "speed", "gold_gven", "diamond_gven")
INTRO_TEXT = ["Добро пожаловать в игру!", "Исправь ошибку Эндрю Гарфилда!", "СПАСИ Гвен!"]
CAPTION = "Save Gven!"
LOSE_SOUND = pygame.mixer.Sound("data/lose_sound.ogg")
MISS_SOUND = pygame.mixer.Sound("data/miss_sound.ogg")
NEW_LEVEL_SOUND = pygame.mixer.Sound("data/new_level_sound.ogg")
MINUS_HEART_SOUND = pygame.mixer.Sound("data/minus_heart.ogg")
SPEED_SOUND = pygame.mixer.Sound("data/speed_sound.ogg")
HEART_SOUND = pygame.mixer.Sound("data/heart_sound.ogg")
WIN_SOUND = pygame.mixer.Sound("data/win_sound.ogg")
SAVE_SOUND = pygame.mixer.Sound("data/save_sound.ogg")
SOUNDTRACK = "data/soundtrack.mp3"
MISS_SOUND.set_volume(1)
LOSE_SOUND.set_volume(0.2)
NEW_LEVEL_SOUND.set_volume(0.3)
MINUS_HEART_SOUND.set_volume(0.2)
SPEED_SOUND.set_volume(1)
HEART_SOUND.set_volume(1)
WIN_SOUND.set_volume(0.2)
SAVE_SOUND.set_volume(0.4)
GRAVITY = 0.5
