import pygame

FPS = 60
SIZE = WIDTH, HEIGHT = 500, 500
BLACK = pygame.Color("black")
RED = pygame.Color("red")
WHITE = pygame.Color("white")
BLUE = pygame.Color("blue")
YELLOW = pygame.Color("yellow")
GREEN = pygame.Color("green")
GOLD = pygame.Color("#ffd700")
spLeft = spRight = False
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
SIZES = {'hp': (100, 100), 'speed': (130, 130), 'bomb': (100, 100), 'gold_gven': (130, 130), 'diamond_gven': (120, 120)}
DELTA_X = {'hp': (-3, 3), 'speed': (-3, 3), 'bomb': (-3, 3), 'gold_gven': (-10, 10), 'diamond_gven': (-10, 10)}
BONUSES = ['bomb', 'hp', 'speed', 'bomb']
SPECIAL_GVENS = ['gold_gven', 'gold_gven', 'diamond_gven']
all_sprites = pygame.sprite.Group()
gven_group = pygame.sprite.Group()
heart_group = pygame.sprite.Group()
GAME = None
