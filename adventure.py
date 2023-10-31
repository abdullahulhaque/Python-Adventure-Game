import pygame
import engine

# coins by 
# https://opengameart.org/content/rotating-coin-0
# enemy 
# https://opengameart.org/content/enemy-angry-nut
# lives
# https://opengameart.org/content/heart-3

def drawText(t, x, y):
    text = font.render(t, True, coin_color, Dark_Gray) # the true is anti aliasing
    text_rectangle = text.get_rect()

        # text_rectangle = (30,30) -- another way to the below
        # text_rectangle.x = 50  -- moves around display
        # text_rectangle.y = 50  -- moves around display

    text_rectangle.topleft = (x, y)
    screen.blit(text, text_rectangle)

# constant variables
SCREEN_SIZE = (800,600)
Dark_Gray = (52,52,52)
mustard = (250,250,250)
coin_color = (209, 206, 25)


# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Abdullah\'s Game')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24) #pygame directory

# game states = playing // win // lose
game_state = 'playing'

# player
player_image = pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_00.png")
player_x = 300

player_y = 0
player_speed = 0
player_acceleration = 0.2

player_width = 37
player_height = 68

player_direction = 'right'
player_state = 'idle' # or walking, one of these two


player_animations = { 
    'idle' : engine.Animation({
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_00.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_01.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_02.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_03.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\sprite_04.png")
    }),
    'walking' : engine.Animation({
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_04.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_05.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_06.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_07.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_08.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_09.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_10.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_11.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_12.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_13.png"),
        pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\vitawalk_14.png"),

    })
    
}

# platforms
platforms = [
    #middle
    pygame.Rect(100,300,400,50),
    #left
    pygame.Rect(100,250,50,50),
    #right
    pygame.Rect(450,250,50,50)

]

# coins
coin_image = pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_0.png")
coin_animation = engine.Animation({
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_0.png"),
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_1.png"),
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_2.png"),
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_3.png"),
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_4.png"),
    pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\coin_5.png")
})
coins = [
    pygame.Rect(100,200,23,23),
    pygame.Rect(200,250,23,23)
]

score = 0

# enemies
enemy_image = pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\enemy.png")
enemies = [
    pygame.Rect(150,272,42,28)
]

lives = 3
heart_image = pygame.image.load(r"C:\Users\avang\OneDrive\Desktop\AdventureGame\images\Heart.png")

running = True
x, y = 10,10
while running: 
#keeps it running forever
# game loop

    # ----
    #INPUT
    # ----

    # check for quit
    for event in pygame.event.get():
# print(event) # this gives us every detail happening on screen, forward backward up down etc,
        if event.type == 256: # you can also say if event.type == pygame.Quit:  (it closes app)
            running = False

    if game_state == 'playing':

        new_player_x = player_x
        new_player_y = player_y

    # player input
        keys = pygame.key.get_pressed()
        #a = left
        if keys[pygame.K_a]:
            new_player_x -= 2
            player_direction = 'left'
            player_state = 'walking'
        #d = right
        if keys[pygame.K_d]:
            new_player_x += 2
            player_direction = 'right'
            player_state = 'walking'
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            player_state = 'idle'
        # w = jump (if on ground)
        if keys[pygame.K_w] and player_on_ground:
            player_speed = -5

        

    # --
    # update
    # --

    
    if game_state == 'playing':

        # upate player animation
        # update player animation if the state exists
        if player_state in player_animations:
            player_animations[player_state].update()


        # update coin animation
        coin_animation.update()

        # horizontal movement

        new_player_rect = pygame.Rect(new_player_x, player_y, player_width, player_height)
        x_collision = False

        #... check agaisnt every platform
        for p in platforms: 
            if p.colliderect(new_player_rect):
                x_collision = True
                break

        # set x collision to true

        if x_collision == False:
            player_x = new_player_x
        # player_x = new_player_x 

        #VERTICAL,  the above stuff is horizontal movement, now lets do VERTICAL

        player_speed += player_acceleration
        new_player_y += player_speed

        new_player_rect = pygame.Rect(player_x, new_player_y, player_width, player_height)
        y_collision = False
        player_on_ground = False

        #... check agaisnt every platform
        for p in platforms: 
            if p.colliderect(new_player_rect): #if there is a collision
                y_collision = True
                player_speed = 0
                # if the platform is below the player, stick to platform
                if p[1] > new_player_y:
                    #stick the player to the platform
                    player_y = p[1] - player_height #if we dont subtract player height, it sticks player to platform
                    player_on_ground = True
                break

    
        if y_collision == False:
            player_y = new_player_y

        # seeing if any coins have been collected
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        for c in coins:
            if c.colliderect(player_rect): #if coin touches player it will be removed
                coins.remove(c) #it will be removed as soon as touch
                score += 1 # adds up the points
                # win if the score is 2
                if score >= 2:
                    game_state = 'win'

        # seeing if player has hit enemy
        for e in enemies:
            if e.colliderect(player_rect): #if enemy touches player
                lives -= 1
                #reset player position
                player_x = 300
                player_y = 0
                player_speed = 0 # set this so if player spawns on enemy it does not mess up
                # change the game state
                # if no lives remaining
                if lives <= 0:
                    game_state = 'lose'

    # ----
    #draw
    # ----

    #code below is background
    screen.fill(Dark_Gray)

    #platform
    for p in platforms: 
        pygame.draw.rect(screen, mustard, p)
        

    # coins
    for c in coins:
        #screen.blit(coin_image, (c[0], c[1])) # x and y coordinates
        coin_animation.draw(screen, c.x, c.y, False, False)

    # enemies
    for e in enemies:
        screen.blit(enemy_image, (e.x, e.y)) # x and y coordinates

    #this is the player code below
    if player_direction == 'right':
        #screen.blit(player_image, (player_x, player_y)) #blit means to load an image and the 0,0 are the x y coordinates
        player_animations[player_state].draw(screen, player_x, player_y, False, False)
    elif player_direction == 'left':
        #screen.blit(pygame.transform.flip(player_image, True, False), (player_x, player_y))
        player_animations[player_state].draw(screen, player_x, player_y, True, False)
    
    # this is the player code below
    if player_state == 'idle' or player_state == 'walking':
        if player_direction == 'right':
            player_animations[player_state].draw(screen, player_x, player_y, False, False)
    elif player_direction == 'left':
        player_animations[player_state].draw(screen, player_x, player_y, True, False)




    # --
    # player information display want on top of everything so will go last
    # --

    # score
    screen.blit(coin_image, (x, y))
    drawText(str(score), 50, 10)


    # score_text = font.render('Score: ' + str(score), True, mustard, Dark_Gray) # the true is anti aliasing
    # score_text_rectangle = score_text.get_rect()

    # score_text_rectangle = (30,30) -- another way to the below
    # score_text_rectangle.x = 50  -- moves around display
    # score_text_rectangle.y = 50  -- moves around display

    # score_text_rectangle = (3, 4)
    # screen.blit(score_text, score_text_rectangle)

    # lives
    for l in range(lives):
        screen.blit(heart_image, (665 +(l*50), 2))

    if game_state == 'win':
        drawText('You win!', 350, 200)
    #draw win text
    if game_state == 'lose':
        drawText('You lose!', 350, 200)
    # draw lose text

    #this is to present screen
    pygame.display.flip()

    clock.tick(60) #we dont want game to run faster than 60fps

#quit
pygame.quit()