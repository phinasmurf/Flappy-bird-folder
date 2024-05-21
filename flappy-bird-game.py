import pygame 
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
points = 0

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

def update_points(pile_list):
    global points
    score_font = pygame.font.Font('font/Pixeltype.ttf', 50)

    if pile_list:
        for piles_ract in pile_list:
            if piles_ract.right == (200, (0, 400)):
                points += 1
                print(points)
               
    score_surface = font.render(str(points), False,(64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)


def collisions(bird_rect, piles):
    if piles:
         for piles_rect in piles:
             if bird_rect.colliderect(piles_rect):
                return False
    return True 

def collision_ground(bird_rect, ground_rect):
    if ground_rect:
        if bird_rect.colliderect(ground_rect):
            return False
    return True


#Baground surfaces
sky_bg = pygame.image.load('graphics/sky.png').convert()
ground_bg = pygame.image.load('graphics/ground.png').convert()
ground_rect = ground_bg.get_rect( topleft = (0,325))

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

pile_list = []

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
                bird_gravity = -11
                    #start_time = pygame.time.get_ticks()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                

        if game_start == True:
            if event.type == pile_timer and game_active:
                if randint (0,2):
                    pile_list.append(pile_up.get_rect(midtop = (randint(900,1100), randint(200, 325))))
                else:
                    pile_list.append(pile_down.get_rect(midbottom = (randint(900,1100), randint(100,200))))

    if game_active:
        #Bagground
        screen.blit(sky_bg, (0,0))
        screen.blit(ground_bg, ground_rect)
    
        #Player gravity
        if game_start == False:
            screen.blit(text_surf, (250, 50))
        elif game_start == True:
            bird_gravity += 1
            bird_rect.y += bird_gravity
            if bird_rect.bottom > 325:
                bird_rect.bottom = 337
                game_active = False
        screen.blit(main_bird, bird_rect)

        #pile movement
        pile_list = pile_movement(pile_list)
        update_points(pile_list)
        game_active = collisions(bird_rect, pile_list)
        game_active = collision_ground(bird_rect, ground_rect)
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(end_text, (320, 50))
        pile_list.clear()
        bird_rect.midbottom = (150, 200)

    pygame.display.update()
    clock.tick(60)