import pygame, random
from termcolor import colored
from pygame import mixer

pygame.init()

WINDOW_WIDTH = 880
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Puzzle Game')

FPS = 10
clock = pygame.time.Clock()

mixer.music.load('./obrazky./background.mp3')
mixer.music.play(-1)
key_sound = mixer.Sound('./obrazky./key_click.wav')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CRIMSON = (220, 20, 60)
ORANGE = (255, 127, 0)
VIOLET = (130, 27, 111)
SKYBLUE = (49, 71, 176)
PRD = (113, 168, 122)

rect_color = pygame.Color('violet')
color_active = pygame.Color('blue')
color_passive = rect_color

j = pygame.image.load("./obrazky./dokopy.jpg")

font_title = pygame.font.Font('./obrazky./Amatic-Bold.ttf', 120)
font_content = pygame.font.Font('./obrazky./Amatic-Bold.ttf', 50)
font_animals = pygame.font.Font('./obrazky./Amatic-Bold.ttf', 40)
input_font = pygame.font.Font(None,64)

# start screen
title_text = font_title.render('Puzzle Game',True ,BLACK)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 150)

choose_text = font_content.render('Choose your difficulty', True, SKYBLUE )
choose_rect = choose_text.get_rect()
choose_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)

easy_text = font_content.render("Press 'E' - Easy (3x3)", True, BLACK)
easy_rect = easy_text.get_rect()
easy_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40)

medium_text = font_content.render("Press 'M' - Medium (4x4)", True, BLACK)
medium_rect = medium_text.get_rect()
medium_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)

hard_text = font_content.render("Press 'H' - Hard (5x5)", True, BLACK)
hard_rect = hard_text.get_rect()
hard_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 140)

impossible_text = font_content.render("Press 'I' - Impossible (10x10)",True,BLACK)
impossible_rect = impossible_text.get_rect()
impossible_rect.center = (WINDOW_WIDTH // 2,WINDOW_HEIGHT // 2 + 190)

# end screen
play_again_text = font_title.render('Play Again?', True, SKYBLUE)
play_again_rect = play_again_text.get_rect()
play_again_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 150)

continue_text = font_content.render('Press Space', True, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 90)

vyber_text = font_title.render('Choose your puzzle!',True,color_active)
vyber_rect = vyber_text.get_rect()
vyber_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200)

slon_text = font_animals.render('Elephant -->  S',True,BLACK)
slon_rect = vyber_text.get_rect()
slon_rect.center = (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2 + 20)

panda_text = font_animals.render('Panda      -->  P',True,BLACK)
panda_rect = vyber_text.get_rect()
panda_rect.center = (WINDOW_WIDTH // 2 - 120, WINDOW_HEIGHT // 2 + 60)

tiger_text = font_animals.render('T  <-- Tiger',True,BLACK)
tiger_rect = vyber_text.get_rect()
tiger_rect.center = (WINDOW_WIDTH // 2 + 570, WINDOW_HEIGHT // 2 + 20)

monkey_text = font_animals.render('O  <-- Monkey',True,BLACK)
monkey_rect = vyber_text.get_rect()
monkey_rect.center = (WINDOW_WIDTH // 2 + 570, WINDOW_HEIGHT // 2 + 60)

exit_text = font_animals.render("EXIT -> ESC",True,SKYBLUE)
exit_rect = exit_text.get_rect()
exit_rect.bottomright = (WINDOW_WIDTH , WINDOW_HEIGHT )

input_rect = pygame.Rect(360,260,150,75)

selected_img = None
is_game_over = False
show_start_screen = False
show_zaciatok = True

rows = None
cols = None

cell_width = None
cell_height = None

cells = []

def start_game(mode):
    global cells, cell_width, cell_height, show_start_screen
    
    rows = mode
    cols = mode
    num_cells = rows * cols

    cell_width = WINDOW_WIDTH // rows
    cell_height = WINDOW_HEIGHT // cols

    cells = []
    rand_indexes = list(range(0, num_cells))

    for i in range(num_cells):
        x = (i % rows) * cell_width
        y = (i // cols) * cell_height
        rect = pygame.Rect(x, y, cell_width, cell_height)
        rand_pos = random.choice(rand_indexes)
        rand_indexes.remove(rand_pos)
        cells.append({'rect': rect, 'border': WHITE, 'order': i, 'pos':rand_pos})
    show_start_screen = False

active = False
running = True
user_text = ''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound = mixer.Sound('./obrazky./click.wav')
            click_sound.play()
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if active == True:
                show_start_screen = False
                pygame.event.get()
                pygame.display.update()
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[0:-1]
                if event.key == pygame.K_p:
                    key_sound.play()
                    bg = pygame.image.load('./obrazky./pandu.jpg')
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0, 0)
                    show_zaciatok = False
                    show_start_screen = True
                    active = False
                elif event.key == pygame.K_t:
                    key_sound.play()
                    bg = pygame.image.load('./obrazky./tigra.jpg')
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0, 0)
                    show_zaciatok = False
                    show_start_screen = True
                    active = False
                elif event.key == pygame.K_s:
                    key_sound.play()
                    bg = pygame.image.load('./obrazky./slona.jpg')
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0, 0)
                    show_zaciatok = False
                    show_start_screen = True
                    active = False
                elif event.key == pygame.K_o:
                    key_sound.play()
                    bg =pygame.image.load('./obrazky./opicu.jpg')
                    bg_rect = bg.get_rect()
                    bg_rect.topleft = (0, 0)
                    show_zaciatok = False
                    show_start_screen = True
                    active = False
                else:
                    quit()
                    
            if is_game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    key_sound.play()
                    mouse_pos = pygame.mouse.get_pos()
                    is_game_over = False
                    show_zaciatok = True
                    show_start_screen = False
                    show_zaciatok = True
                    selected_img = None
                    pygame.display.update()
            if show_start_screen:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    key_sound.play()
                    pygame.display.update()
                    start_game(3)
                elif keys[pygame.K_m]:
                    key_sound.play()
                    pygame.display.update()
                    start_game(4)
                elif keys[pygame.K_h]:
                    key_sound.play()
                    pygame.display.update()
                    start_game(5)
                elif keys[pygame.K_i]:
                    key_sound.play()
                    pygame.display.update()
                    start_game(10)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
            mouse_pos = pygame.mouse.get_pos()

            for cell in cells:
                rect = cell['rect']
                order = cell['order']

                if rect.collidepoint(mouse_pos):
                    if not selected_img:
                        selected_img = cell
                        cell['border'] = RED
                    else:
                        current_img = cell
                        if current_img['order'] != selected_img['order']:
                            #swap images
                            temp = selected_img['pos']
                            cells[selected_img['order']]['pos'] = cells[current_img['order']]['pos']
                            cells[current_img['order']]['pos'] = temp

                            cells[selected_img['order']]['border'] = WHITE
                            selected_img = None

                            # check if puzzle is solved
                            is_game_over = True
                            for cell in cells:
                                if cell['order'] != cell['pos']:
                                    is_game_over = False
    if active:
        rect_color = color_active
    else:
        rect_color = color_passive
        
    if show_start_screen:
        screen.fill(PRD)
        screen.blit(title_text, title_rect)
        screen.blit(choose_text, choose_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        screen.blit(impossible_text,impossible_rect)
        screen.blit(exit_text,exit_rect)
        pygame.event.get()
    elif show_zaciatok:
        screen.blit(j,(0,0))
        text_surface = input_font.render(user_text,True,(255,255,255))
        pygame.draw.rect(screen,rect_color,input_rect,2)
        screen.blit(text_surface,(input_rect.x + 15, input_rect.y + 15))
        screen.blit(vyber_text,vyber_rect)
        screen.blit(slon_text,slon_rect)
        screen.blit(panda_text,panda_rect)
        screen.blit(tiger_text,tiger_rect)
        screen.blit(monkey_text,monkey_rect)
        screen.blit(exit_text,exit_rect)
        input_rect.w = max(150,text_surface.get_width() + 20)
        selected_img = None
        current_img = None
        
    else:

        screen.fill(WHITE)

        if not is_game_over:
            for i, val in enumerate(cells):
                pos = cells[i]['pos']
                img_area = pygame.Rect(cells[pos]['rect'].x, cells[pos]['rect'].y, cell_width, cell_height)
                screen.blit(bg, cells[i]['rect'], img_area)
                pygame.draw.rect(screen, cells[i]['border'], cells[i]['rect'], 1)
        else:
            screen.blit(bg, bg_rect)
            screen.blit(play_again_text, play_again_rect)
            screen.blit(continue_text, continue_rect)
            screen.blit(exit_text,exit_rect)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()