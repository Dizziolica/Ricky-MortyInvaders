import pygame

# you'll be able to shoot every 450ms
RELOAD_SPEED = 450
score = 0
# the foes move every 1000ms sideways and every 3500ms down
MOVE_SIDE = 1000
MOVE_DOWN = 3500
screenW = 1336
screenH = 768
screen = pygame.display.set_mode((screenW, screenH))
clock = pygame.time.Clock()
start_time = 0
game_active = True
lives = 3

pygame.display.set_caption("Space Invader")

# create a bunch of events 
move_side_event = pygame.USEREVENT + 1
move_down_event = pygame.USEREVENT + 2
reloaded_event  = pygame.USEREVENT + 3

move_left, reloaded = True, True

# Background
space = pygame.image.load("space.png")
spaceSize = (screenW, screenH)
spaceImage = pygame.transform.scale(space, spaceSize)

#INVADERS
sizeX = 100
sizeY = 100
sizeS = (sizeX, sizeY)

yEnemy = 100
xEnemy = 500
yshot = 130
xshot = 130
             
enemyimage = pygame.image.load("ship.png").convert_alpha()
enemySize = pygame.transform.scale(enemyimage, sizeS)
enemyIImage = enemySize.get_rect(midleft = (30, 70))

#Shot
shotImage = pygame.image.load("dad.png").convert_alpha()
shotSize = pygame.transform.scale(shotImage, (60, 170 ))
shotIImage = shotSize.get_rect(bottomleft=(500, screenH - 100))

# set timer for the movement events
pygame.time.set_timer(move_side_event, MOVE_SIDE)
pygame.time.set_timer(move_down_event, MOVE_DOWN)

#Hero

heroImage = pygame.image.load("ricky.png").convert_alpha()
heroSize = pygame.transform.scale(heroImage, (50, 50))
heroIImage = heroSize.get_rect(midleft = (500, screenH - 250))

#Music
pygame.mixer.init()
sound = pygame.mixer.Sound("morty3.mp3")
sound.play(loops=-1, maxtime=0, fade_ms=0)
sound.set_volume(0.5)

pygame.font.init()

#Score
start_time = 0




        

invaders, shots = [], []
for x in range(100, 1250, 200):
    for y in range(50, 300, 100
    ):
        invaders.append(enemySize.get_rect(topleft=(x, y)))
        
for x in range(100):
   
    shots.append(enemySize.get_rect(bottomright=(heroIImage.x, heroIImage.y)))

        

        




while True:
    clock.tick(40)
    current_time = int(pygame.time.get_ticks() / 1000 ) - start_time
    test_font = pygame.font.SysFont('Pixe.ttf', 30)
    current_time = int(pygame.time.get_ticks() / 1000 ) - start_time
    score_message = test_font.render(f'Your score: {score}',False,(227,207,87))
    score_rect = score_message.get_rect(center = (100, 50))
            
    #close the game

    if pygame.event.get(pygame.QUIT):  break
    #moves of invader

    for e in pygame.event.get():

        if e.type == move_side_event:
            for invader in invaders:
               invader.move_ip((-30 if move_left else 30, 0))
            move_left = not move_left
        elif e.type == move_down_event:
            for invader in invaders:
                invader.move_ip(0, 50)
        elif e.type == reloaded_event:
            # when the reload timer runs out, reset it
            reloaded = True
            pygame.time.set_timer(reloaded_event, 0)

    # moves shots in the affect in invader
    for shot in shots[:]:
        shot.move_ip((0, -20))
        if not screen.get_rect().contains(shotIImage):
    #shots.remove(shot) s
             shot.y = heroIImage.y + 50
             shot.x = heroIImage.x
        else:
             hit = False
             for invader in invaders:
                 if invader.colliderect(shot):
                     hit = True
                    
                     invaders.remove(invader)
                
                #collide hero

                 



                  
             #shot hit              
                    
                 if hit:
                
                     shotIImage.x = heroIImage.x
                     shotIImage.y = heroIImage.y + 100

                     score += 10

                 if invader.y == heroIImage and invader.x == heroIImage.x and  heroIImage.colliderect(invaders):
                
                     lives -= 1
                     heroIImage.y = screenH - 100

                     if lives == 0:

                      capa_surface = pygame.image.load('game.png').convert_alpha()
                      capasize = (1336, 800)
                      capa_image = pygame.transform.scale(capa_surface, capasize)
                      capa_rect = capa_image.get_rect(center = (400, 200))
                      screen.blit(capa_image, capa_rect)
                      ricky2_surface = pygame.image.load('baba.png').convert_alpha()
                      default_ricky2_size = (100, 100)
                      ricky2_image = pygame.transform.scale(ricky2_surface, default_ricky2_size)
                      ricky2_rect = ricky2_image.get_rect(midleft = (600, 400))
                      screen.blit(ricky2_image, ricky2_rect)
                      start_time = pygame.time.get_ticks()
                      current_time = int(pygame.time.get_ticks() / 1000 ) - start_time
                     
            
                
                
    #moves hero         
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: 

        heroIImage.move_ip((-10, 0)) 
        shotIImage.x = heroIImage.x 
        shotIImage.y = heroIImage.y + 50
    if pressed[pygame.K_RIGHT]: 

        heroIImage.move_ip((10, 0))
        shotIImage.x = heroIImage.x 
        shotIImage.y = heroIImage.y + 50
    #shot
    if pressed[pygame.K_SPACE]: 
        if reloaded:
            shots.append(heroIImage.copy())
            reloaded = False
            # when shooting, create a timeout of RELOAD_SPEED
            pygame.time.set_timer(reloaded_event, RELOAD_SPEED)
    # hero moves
    if pressed[pygame.K_UP]: 

        heroIImage.move_ip((0, -10))

    if pressed[pygame.K_DOWN]: 

        heroIImage.move_ip((0, 10))
    

    heroIImage.clamp_ip(screen.get_rect())
    if heroIImage.x > screenW:
        heroIImage.x = 50
    if heroIImage.y > screenH:
        heroIImage.y = 100
        
    if heroIImage.y < 0:
        heroIImage.y = screenH - 100
    #score 
    
   
   

    #Background
    space = pygame.image.load("space.png")
    spaceSize = (screenW, screenH)
    spaceImage = pygame.transform.scale(space, spaceSize)
    screen.blit(spaceImage, (0,0))

    for invader in invaders: 
        if invader.y > screenH:
                invader.y = 150
        screen.blit( enemySize, invader)

    for shot in shots: 
        screen.blit(shotSize, shot)
    
    screen.blit(score_message, score_rect)
    screen.blit(heroImage, heroIImage)
    screen.blit(shotSize, shotIImage)
    
    pygame.display.flip()

    
