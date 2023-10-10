import pygame
from pygame.locals import *
from pygame import mixer
import pickle
from os import path

# intialize mixer for sound
mixer.init()
pygame.init()


clock = pygame.time.Clock()
fps = 50

width = 600
height = 600

# create window for the game on screen
area = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sky Hopper')


# define font
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)


tile_size = 30
game_over = 0
main_menu = True
level = 0
max_levels = 7
score = 0


# define colours
white = (255, 255, 255)
blue = (0, 0, 255)


# load images
sun = pygame.image.load('img/moon.png')
background = pygame.image.load('img/sky1.jpg')
restart_btn = pygame.image.load('img/restart_btn.png')
start_btn = pygame.image.load('img/start_btn.png')
exit_btn = pygame.image.load('img/exit_btn.png')

# load sounds
coin_sound = pygame.mixer.Sound('img/coin.wav')
coin_sound.set_volume(0.3)
end_sound = pygame.mixer.Sound('img/coin.wav')
end_sound.set_volume(0.3)
jump_sound = pygame.mixer.Sound('img/jump.wav')
jump_sound.set_volume(0.3)
game_over_sound = pygame.mixer.Sound('img/game_over.wav')
game_over_sound.set_volume(0.3)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    area.blit(img, (x, y))

# reset level when game is over / restart


def reset_level(level):
    end_sound.play()
    player.reset(100, height - 130)
    blob_group.empty()
    Base_group.empty()
    coin_group.empty()
    lava_group.empty()
    exit_group.empty()
    # load in level data and create world
    if path.exists(f'level{level}_data'):
        levelfile = open(f'level{level}_data', 'rb')
        world_data = pickle.load(levelfile)
    world = World(world_data)

    # create dummy coin for showing the score
    score_coin = Coin(tile_size // 2, tile_size // 2)
    coin_group.add(score_coin)
    return world


# button class for start , exit,restart etc buttons
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button
        area.blit(self.image, self.rect)
        return action


class Player():
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        anim_walk = 1
        above_obj = 20

        if game_over == 0:
            # get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                jump_sound.play()
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # handle animation
            if self.counter > anim_walk:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # check for collision
            self.in_air = True
            for tile in world.tile_list:
                # check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # check for collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
                game_over_sound.play()

            # check for collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                game_over_sound.play()

            # check for collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            # check for collision with Bases
            for Base in Base_group:
                # collision in the x direction
                if Base.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # collision in the y direction
                if Base.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # check if below Base
                    if abs((self.rect.top + dy) - Base.rect.bottom) < above_obj:
                        self.vel_y = 0
                        dy = Base.rect.bottom - self.rect.top
                    # check if above Base
                    elif abs((self.rect.bottom + dy) - Base.rect.top) < above_obj:
                        self.rect.bottom = Base.rect.top - 1
                        self.in_air = False
                        dy = 0
                    # move sideways with the Base
                    if Base.move_x != 0:
                        self.rect.x += Base.move_direction

            # update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.ghost
            draw_text('GAME OVER!', font, blue,
                      (width // 2) - 200, height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        # draw player onto area
        area.blit(self.image, self.rect)

        return game_over

    def reset(self, x, y):

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            right_dir = pygame.image.load(f'img/guy{num}.png')
            right_dir = pygame.transform.scale(right_dir, (30, 60))
            left_dir = pygame.transform.flip(right_dir, True, False)
            self.images_right.append(right_dir)
            self.images_left.append(left_dir)
        self.ghost = pygame.image.load('img/ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


class World():
    def __init__(self, data):
        self.tile_list = []

        # load images
        dt = pygame.image.load('img/dirt.png')
        grass = pygame.image.load('img/grass.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dt, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size,
                                 row_count * tile_size + 15)
                    blob_group.add(blob)
                if tile == 4:
                    base = Base(col_count * tile_size,
                                row_count * tile_size, 1, 0)
                    Base_group.add(base)
                if tile == 5:
                    base = Base(col_count * tile_size,
                                row_count * tile_size, 0, 1)
                    Base_group.add(base)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count *
                                tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2),
                                row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)
                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count *
                                tile_size - (tile_size // 2))
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            area.blit(tile[0], tile[1])


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Base(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/Base.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/coin.png')
        self.image = pygame.transform.scale(
            img, (tile_size // 2, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(
            img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


player = Player(50, height - 230)

blob_group = pygame.sprite.Group()
Base_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# coin icon on left corner
score_coin = Coin(tile_size // 2, tile_size // 2)
coin_group.add(score_coin)

# load in level data and create world
if path.exists(f'level{level}_data'):
    worldfile = open(f'level{level}_data', 'rb')
    world_data = pickle.load(worldfile)
world = World(world_data)


# create buttons
restart_button = Button(width // 2 - 50, height // 2 + 100, restart_btn)
start_button = Button(width // 2 - 250, height // 2, start_btn)
exit_button = Button(width // 2 + 50, height // 2, exit_btn)


run = True
while run:
    clock.tick(fps)  # player speed and base moving speed
    area.blit(background, (0, 0))
    area.blit(sun, (100, 100))

    if main_menu == True:
        if exit_button.draw():
            run = False
        if start_button.draw():
            main_menu = False
    else:
        world.draw()

        if game_over == 0:
            blob_group.update()
            Base_group.update()

            if pygame.sprite.spritecollide(player, coin_group, True):
                score += 1
                coin_sound.play()
            draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)

        blob_group.draw(area)
        Base_group.draw(area)
        lava_group.draw(area)
        coin_group.draw(area)
        exit_group.draw(area)

        game_over = player.update(game_over)

        # if player has died
        if game_over == -1:
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        # if player has completed the level
        if game_over == 1:
            # reset game and go to next level
            level += 1
            if level <= max_levels:
                # reset level
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:
                draw_text('YOU WIN!', font, blue,
                          (width // 2) - 140, height // 2)
                if restart_button.draw():
                    level = 1
                    # reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
