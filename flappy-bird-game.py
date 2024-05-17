import pygame 
from sys import exit
from random import randint

#Important variables
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
mouse_pos = pygame.mouse.get_pos()
game_active = True
game_start = False
start_time = 0

#Functions
def pile_movement(pile_list):
    if pile_list:
        for piles_rect in pile_list:
            piles_rect.x -= 4
            if piles_rect.y > 201:
                screen.blit(pile_up, piles_rect)
            elif piles_rect.y < 200:
                screen.blit(pile_down, piles_rect)

        pile_list = [pile for pile in pile_list if pile.right > 0]
        return pile_list  
    else:
        return []

#def display_score():
     #current_time = (pygame.time.get_ticks() / 1000)

     #score surface
     #score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
     #score_surface = font.render(int(current_time), False,(64, 64, 64) )
     #screen.blit(score_surface, current_time)

#Baground surfaces
sky_bg = pygame.image.load('graphics/sky.png').convert()
ground_bg1 = pygame.image.load('graphics/ground.png').convert()
ground_rect1 = ground_bg1.get_rect( topleft = (0,325))

#Text surfaces
font = pygame.font.Font('font/Pixeltype.ttf', 50) 
text_surf = font.render('Welcome to flappy bird!', False, (64, 64, 64))
start_text = False

#Text end surface
end_text = font.render('You died!', False, (64, 64, 64))

#Character 
main_bird = pygame.image.load('graphics/flappy_bird.png').convert_alpha()
main_bird = pygame.transform.rotozoom(main_bird, 0, 0.05)
bird_rect = main_bird.get_rect(center = (150, 200))
bird_gravity = 0

#piles
pile_up = pygame.image.load('graphics/piles/up_piles.png').convert_alpha()
pile_up_rect = pile_up.get_rect(midtop = (600, 200))

pile_down = pygame.image.load('graphics/piles/down_pipe.png').convert_alpha()
pile_down_rect = pile_down.get_rect(midbottom = (600, 200))

pile_list = ''

#Timer
pile_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pile_timer, 1400)

while True:
    #check for player-input to close the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        #Jump when space is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                game_start = True
                bird_gravity = -13
                start_time = int(pygame.time.get_ticks()/1000)
        
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bird_rect.collidepoint(mouse_pos): 
                print(mouse_pos)

        if game_start == True:
            if event.type == pile_timer and game_active:
                if randint (0,2):
                    pile_list.append(pile_up.get_rect(midtop = (randint(900,1100), randint(200, 325))))
                else:
                    pile_list.append(pile_down.get_rect(midbottom = (randint(900,1100), randint(100,200))))

    if game_active:
        #Bagground
        screen.blit(sky_bg, (0,0))
        screen.blit(ground_bg1, ground_rect1)
    
        #Player gravity
        if game_start == False:
            screen.blit(text_surf, (250, 50))
        elif game_start == True:
            bird_gravity += 1
            bird_rect.y += bird_gravity
            if bird_rect.bottom > 325:
                bird_rect.bottom = 337
                #game_active = False
        screen.blit(main_bird, bird_rect)
        
        #piles
        #pile_up_rect.left -= 4
        #if pile_up_rect.right < 0:
        #    pile_up_rect.left = 820
        #if pile_up_rect.colliderect(bird_rect):
        #    game_active = False

        #pile movement
        pile_list = pile_movement(pile_list)
        #display_score()
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(end_text, (320, 50))

    pygame.display.update()
    clock.tick(60)