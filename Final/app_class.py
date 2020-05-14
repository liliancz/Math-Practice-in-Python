import pygame, sys, copy
from settings import *
from button import * 
from questions import *

pygame.init()   
vec = pygame.math.Vector2
B_start = Button()
B_start.set(0,0,100,100)
Q1 = Question()
class App:
    def __init__(A):
        A.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        A.clock = pygame.time.Clock()
        A.running = True
        A.state = "start"                                                  #start
        A.cell_width = MAZE_WIDTH // COLS
        A.cell_height = MAZE_HEIGHT // ROWS
        A.enemies = []
        A.walls =[]
        A.coins =[]
        A.enemies = []
        A.load()
     
        
    def run(A):
        while A.running:
            if A.state == "start":
                A.start_events()
                A.start_update()
                A.start_draw()
            elif A.state == "Inst":
                A.Inst_events()
                A.Inst_update()
                A.Inst_draw()
            elif A.state == "play":
                A.play_events()
                A.play_update()
                A.play_draw()




                          
            else:
                A.running = False


                
            A.clock.tick(FPS)            
        pygame.quit()
        sys.exit()

################### HELPFULL FUNCTIONS ##############


    def draw_text(A, displayed_text, screen, pos, size, colour, font_name,
                  centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(displayed_text, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0]= pos[0]-text_size[0]//2
            pos[1]= pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def load(A):
        A.bg_empty = pygame.image.load('bg.png')
        A.bg_empty = pygame.transform.scale(A.bg_empty, (MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_start = pygame.image.load('layout.png')
        A.bg_start = pygame.transform.scale(A.bg_start,(MAZE_WIDTH, MAZE_HEIGHT)) 
        A.bg_inst = pygame.image.load('ins.png')
        A.bg_inst = pygame.transform.scale(A.bg_inst,(MAZE_WIDTH, MAZE_HEIGHT)) 

        
        
                        
    def make_enemies(A):
        for index, pos in enumerate(A.e_pos):
            A.enemies.append(Enemy(A, vec(pos), index))

        
    def draw_grid(A):
        for x in range(WIDTH//A.cell_width):
            pygame.draw.line(A.background, GREY, (x*A.cell_width, 0),
                             (x*A.cell_width, HEIGHT))
        for x in range(HEIGHT//A.cell_height):
            pygame.draw.line(A.background, GREY, (0, x*A.cell_height),
                             (WIDTH, x*A.cell_height))
       # for wall in A.walls:
        #    pygame.draw.rect(A.background, (112, 55, 169),(wall.x*A.cell_width,
         #                   wall.y*A.cell_height, A.cell_width, A.cell_height))
       # for coin in A.coins:
        #    pygame.draw.rect(A.background, (10,150,20), (coin.x*A.cell_width,
         #                   coin.y*A.cell_height, A.cell_width, A.cell_height))

    def reset(A):
        A.player.lives = 3
        A.player.current_score = 0
        A.player.grid_pos = vec(A.player.starting_pos)
        A.player.pix_pos = A.player.get_pix_pos()
        A.player.direction *= 0
        for enemy in A.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0
            
        A.coins = []
        with open("walls.txt", 'r') as file:
            for yindex, line in enumerate(file):
                for xindex, char in enumerate(line):
                    if char == 'C':
                        A.coins.append(vec(xindex, yindex))
        A.state = "play"

    def get_click(A):
        pass




                    
################### START FUNCTIONS ######################################################
                    
    def start_events(A):
        pygame.display.set_caption('MATH GAME')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if pygame.mouse.get_pressed() == (1,0,0):
                print('clicl')
                if(pygame.mouse.get_pos()[0] <= b0_x1 and
                   pygame.mouse.get_pos()[0] >= b0_x0 and
                   pygame.mouse.get_pos()[1] <= b1_y1 and
                   pygame.mouse.get_pos()[1] >= b1_y0):
                    A.state = "Inst"
                    
                    print(A.state)
                if(pygame.mouse.get_pos()[0] <= b0_x1 and
                   pygame.mouse.get_pos()[0] >= b0_x0 and
                   pygame.mouse.get_pos()[1] <= b2_y1 and
                   pygame.mouse.get_pos()[1] >= b2_y0):
                    print('CREDITS')
                    A.state == 'credits'
                if(pygame.mouse.get_pos()[0] <= b0_x1 and
                   pygame.mouse.get_pos()[0] >= b0_x0 and
                   pygame.mouse.get_pos()[1] <= b3_y1 and
                   pygame.mouse.get_pos()[1] >= b3_y0):
                    print('EXIT')
                    A.state == 'exit'
                    A.running = False
                    
            
                
    def start_update(A):
        pass
        
    def start_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_start, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()

################### INSTRUCTIONS FUNCTIONS ######################################################
                    
    def Inst_events(A):
        pygame.display.set_caption('MATH GAME')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if pygame.mouse.get_pressed() == (1,0,0):
                 if(pygame.mouse.get_pos()[0]<= B_start.x_w and
                   pygame.mouse.get_pos()[0] >= B_start.x and
                   pygame.mouse.get_pos()[1] <= B_start.y_h and
                   pygame.mouse.get_pos()[1] >= B_start.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('Pregunta 1')
                    A.state = "play"
                    
                
            
                
    def Inst_update(A):
        pass


        
    def Inst_draw(A):
        B_start.set(600,400,100,100)
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_inst, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()


################### PLAY** FUNCTIONS ######################################################
                    
    def play_events(A):
        pygame.display.set_caption('MATH GAME')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if pygame.mouse.get_pressed() == (1,0,0):
                 if(pygame.mouse.get_pos()[0]<= B_start.x_w and
                   pygame.mouse.get_pos()[0] >= B_start.x and
                   pygame.mouse.get_pos()[1] <= B_start.y_h and
                   pygame.mouse.get_pos()[1] >= B_start.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('Correct')
                    
                
            
                
    def play_update(A):
        pass


        
    def play_draw(A):
        B_start.set(600,400,100,100) 
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_empty, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()


################### PLAY FUNCTIONS #################

    def played_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    A.player.move(vec(-1,0))
                    A.player.p_Iy = 3
                if event.key == pygame.K_RIGHT:
                    A.player.move(vec(1,0))
                    A.player.p_Iy = 1
                if event.key == pygame.K_DOWN:
                    A.player.move(vec(0,1))
                    A.player.p_Iy = 2
                if event.key == pygame.K_UP:
                    A.player.move(vec(0,-1))
                    A.player.p_Iy = 0

    def played_update(A):
        A.player.update()
        for enemy in A.enemies:
            enemy.update()
        for enemy in A.enemies:
            if enemy.grid_pos == A.player.grid_pos:
                A.remove_life()
        if A.player.current_score > 2000:
            A.state = 'won'
                
    def played_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.background, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        A.draw_coins()
        #A.draw_grid()
        A.draw_text('SCORE : {}'.format(A.player.current_score), A.screen, [60,0], 16, WHITE, START_FONT)
        A.draw_text('HIGH SCORE : 0', A.screen, [WIDTH//2+60,0], 16, WHITE,START_FONT)
        A.player.draw()
        for enemy in A.enemies:
            enemy.draw()
        pygame.display.update()

    def remove_life(A):
        A.player.lives -= 1
        if A.player.lives == 0:
            A.state = "game over"
        else:
            A.player.grid_pos = vec(A.player.starting_pos)
            A.player.pix_pos = A.player.get_pix_pos()
            A.player.direction *= 0
            for enemy in A.enemies:
                enemy.grid_pos = vec(enemy.starting_pos)
                enemy.pix_pos = enemy.get_pix_pos()
                enemy.direction *= 0
            
            
        
    def draw_coins(A):
        for coin in A.coins:
            pygame.draw.circle(A.screen, COIN_COLOUR,(int(coin.x*A.cell_width)+A.cell_width//2+TOP_BOTTOM_BUFFER//2,int(coin.y*A.cell_height)+A.cell_height//2+TOP_BOTTOM_BUFFER//2),COIN_RADIUS)

    
################### GAME OVER FUNCTIONS #################

    def game_over_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                A.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                 A.running = False
    
    def game_over_update(A):
        pass
    def game_over_draw(A):
        A.screen.fill(BLACK)
        quit_text = "PRESS ESCAPE BUTTON TO QUIT"
        A.draw_text("GAME OVER", A.screen, [WIDTH//2, 100], 36, RED, OVER_FONT, centered= True)
        A.draw_text(quit_text, A.screen, [WIDTH//2, 600], OVER_TEXT_SIZE, (190, 190,190), OVER_FONT, centered= True)
        A.draw_text('PRESS SPACE BAR TO PLAY', A.screen, [WIDTH//2, HEIGHT//2],START_TEXT_SIZE, (170,132,58), START_FONT, centered=True)
        A.draw_text('1 PLAYER ONLY', A.screen, [WIDTH//2, HEIGHT//2+50],START_TEXT_SIZE, (44,167,198), START_FONT, centered=True)
        A.draw_text('HIGH SCORE', A.screen, [WIDTH//2, 10],START_TEXT_SIZE, WHITE, START_FONT, centered=True)
        pygame.display.update()


################### WON OVER FUNCTIONS #################

    def won_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                A.reset()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                 A.running = False
    
    def won_update(A):
        pass
    def won_draw(A):
        A.screen.fill(BLACK)
        quit_text = "PRESS ESCAPE BUTTON TO QUIT"
        A.draw_text("WON", A.screen, [WIDTH//2, 100], 36, RED, OVER_FONT, centered= True)
        A.draw_text(quit_text, A.screen, [WIDTH//2, 600], OVER_TEXT_SIZE, (190, 190,190), OVER_FONT, centered= True)
        A.draw_text('PRESS SPACE BAR TO PLAY', A.screen, [WIDTH//2, HEIGHT//2],START_TEXT_SIZE, (170,132,58), START_FONT, centered=True)
        A.draw_text('1 PLAYER ONLY', A.screen, [WIDTH//2, HEIGHT//2+50],START_TEXT_SIZE, (44,167,198), START_FONT, centered=True)
        A.draw_text('HIGH SCORE', A.screen, [WIDTH//2, 10],START_TEXT_SIZE, WHITE, START_FONT, centered=True)
        pygame.display.update()
       
        
