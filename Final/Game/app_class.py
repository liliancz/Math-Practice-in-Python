import pygame, sys, copy
from settings import *
from button import * 
from questions import *

pygame.init()   
vec = pygame.math.Vector2
B_start = Button()
B_start.set(600,400,100,100)
B_next = Button()
B_next.set(592,285, 35,35)
B_prev = Button()
B_prev.set(590,225, 35,35)
B_O1 = Button()
B_O1.set(194,404,30,10)
B_O2 = Button()
B_O2.set(194,438,30,10)
B_O3 = Button()
B_O3.set(326,403,30,10)
B_O4 = Button()
B_O4.set(326,435,30,10)
Q1 = Question()
class App:
    def __init__(A):
        A.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        A.clock = pygame.time.Clock()
        A.running = True
        A.state = "name"                                                  #start
        A.cell_width = MAZE_WIDTH // COLS
        A.cell_height = MAZE_HEIGHT // ROWS
        A.enemies = []
        A.walls =[]
        A.coins =[]
        A.enemies = []
        A.load()
        A.x = 0
        A.y = 0
        A.score = 25
        A.check = False
        A.C_Q = 0
        A.M_Q = 25
        A.grade = "0"
     
        
    def run(A):
        while A.running:
            if A.state == "name":
                A.splash_draw()
            elif A.state == "start":
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
            elif A.state == "credits":
                A.credits_events()
                A.credits_update()
                A.credits_draw()
            elif A.state == "won":
                A.won_events()
                A.won_update()
                A.won_draw()
            elif A.state == "wrong":
                A.wrong_events()
                A.wrong_update()
                A.wrong_draw()
            elif A.state == "finish":
                A.finish_events()
                A.finish_update()
                A.finish_draw()



                          
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
        A.bg_empty = pygame.image.load('assets/bg.png')
        A.bg_empty = pygame.transform.scale(A.bg_empty, (MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_start = pygame.image.load('assets/layout.png')
        A.bg_start = pygame.transform.scale(A.bg_start,(MAZE_WIDTH, MAZE_HEIGHT)) 
        A.bg_inst = pygame.image.load('assets/ins.png')
        A.bg_inst = pygame.transform.scale(A.bg_inst,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_credits = pygame.image.load('assets/credits.png')
        A.bg_credits = pygame.transform.scale(A.bg_credits,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_q1 = pygame.image.load('assets/bg_q.png')
        A.bg_q1 = pygame.transform.scale(A.bg_q1,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_won = pygame.image.load('assets/won.png')
        A.bg_won = pygame.transform.scale(A.bg_won,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_wrong = pygame.image.load('assets/wrong.png')
        A.bg_wrong = pygame.transform.scale(A.bg_wrong,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_results = pygame.image.load('assets/results.png')
        A.bg_results = pygame.transform.scale(A.bg_results,(MAZE_WIDTH, MAZE_HEIGHT))
        A.bg_splash = pygame.image.load('assets/name.png')
        A.bg_splash = pygame.transform.scale(A.bg_splash,(MAZE_WIDTH, MAZE_HEIGHT))
        
        
        

    def CurrentGame(A):
        A.calculo = (A.score/A.M_Q)*100
        if (A.calculo >= 85):
            A.grade = "A"
        elif(A.calculo >= 75 and A.calculo < 85):
            A.grade = "B"
        elif(A.calculo >= 65 and A.calculo < 75):
            A.grade = "C"
        elif(A.calculo >= 55 and A.calculo < 65):
            A.grade = "D"
        elif (A.calculo < 55):
            A.grade = "F"

        if(A.C_Q >= A.M_Q):
            pygame.mixer.init()
            pygame.mixer.music.load('assets/end.wav')
            pygame.mixer.music.play()
            A.state = "finish"

        
        
                        
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
                elif(pygame.mouse.get_pos()[0] <= b0_x1 and
                   pygame.mouse.get_pos()[0] >= b0_x0 and
                   pygame.mouse.get_pos()[1] <= b2_y1 and
                   pygame.mouse.get_pos()[1] >= b2_y0):
                    A.state = 'credits'
                    print('CREDITS')
                    
                elif(pygame.mouse.get_pos()[0]<= B_start.x_w and
                   pygame.mouse.get_pos()[0] >= B_start.x and
                   pygame.mouse.get_pos()[1] <= B_start.y_h and
                   pygame.mouse.get_pos()[1] >= B_start.y):
                    print('EXIT')
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
                print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                if(pygame.mouse.get_pos()[0]<= B_prev.x_w and
                   pygame.mouse.get_pos()[0] >= B_prev.x and
                   pygame.mouse.get_pos()[1] <= B_prev.y_h and
                   pygame.mouse.get_pos()[1] >= B_prev.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('back to start')
                    A.state = "start"

                if(pygame.mouse.get_pos()[0] <= B_next.x_w and
                   pygame.mouse.get_pos()[0] >= B_next.x and
                   pygame.mouse.get_pos()[1] <= B_next.y_h and
                   pygame.mouse.get_pos()[1] >= B_next.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    A.state = "play"
                    Q1.Q1()
                    print('Pregunta 1')
                    #A.state = "play"
                    
                
            
                
    def Inst_update(A):
        pass


        
    def Inst_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_inst, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()


################### PLAY FUNCTIONS #################

    def play_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False 
            elif pygame.mouse.get_pressed() == (1,0,0):
                print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] )
                if(pygame.mouse.get_pos()[0]<= B_start.x_w and
                   pygame.mouse.get_pos()[0] >= B_start.x and
                   pygame.mouse.get_pos()[1] <= B_start.y_h and
                   pygame.mouse.get_pos()[1] >= B_start.y):
                    A.check = True
                    print('Check')
                elif(pygame.mouse.get_pos()[0]<= B_O1.x_w and
                   pygame.mouse.get_pos()[0] >= B_O1.x and
                   pygame.mouse.get_pos()[1] <= B_O1.y_h and
                   pygame.mouse.get_pos()[1] >= B_O1.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('B1')
                    Q1.selection = '1'
                elif(pygame.mouse.get_pos()[0]<= B_O2.x_w and
                   pygame.mouse.get_pos()[0] >= B_O2.x and
                   pygame.mouse.get_pos()[1] <= B_O2.y_h and
                   pygame.mouse.get_pos()[1] >= B_O2.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('B2')
                    Q1.selection = '2'
                elif(pygame.mouse.get_pos()[0]<= B_O3.x_w and
                   pygame.mouse.get_pos()[0] >= B_O3.x and
                   pygame.mouse.get_pos()[1] <= B_O3.y_h and
                   pygame.mouse.get_pos()[1] >= B_O3.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('B3')
                    Q1.selection = '3'
                elif(pygame.mouse.get_pos()[0]<= B_O4.x_w and
                   pygame.mouse.get_pos()[0] >= B_O4.x and
                   pygame.mouse.get_pos()[1] <= B_O4.y_h and
                   pygame.mouse.get_pos()[1] >= B_O4.y):
                    print(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] ) 
                    print('B4')
                    Q1.selection = '4'
                    
                    
        

    def play_update(A):
        A.CurrentGame()
        if (A.check == True and Q1.selection != "0"):
            if (Q1.selection == "4"):
                A.state = "won"
                A.C_Q = A.C_Q + 1
                pygame.mixer.init()
                pygame.mixer.music.load('assets/won.wav')
                pygame.mixer.music.play()
            elif (Q1.selection == "1"):
                A.state = "wrong"
                A.score = A.score - 1
                A.C_Q = A.C_Q + 1
                pygame.mixer.init()
                pygame.mixer.music.load('assets/sad.wav')
                pygame.mixer.music.play()
            elif (Q1.selection == "2"):
                A.state = "wrong"
                A.score = A.score - 1
                A.C_Q = A.C_Q + 1
                pygame.mixer.init()
                pygame.mixer.music.load('assets/sad.wav')
                pygame.mixer.music.play()
            elif (Q1.selection == "3"):
                A.state = "wrong"
                A.score = A.score - 1
                A.C_Q = A.C_Q + 1
                pygame.mixer.init()
                pygame.mixer.music.load('assets/sad.wav')
                pygame.mixer.music.play()
        elif (Q1.selection == "0"):
            A.check = False


   
       
 
    def play_draw(A):
        A.screen.fill(BLACK)
        if (Q1.ran == 0 or Q1.ran == 1):
            A.screen.blit(A.bg_q1, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        A.draw_text(str(A.score), A.screen, [435,250], 20, PURPLE, START_FONT)
        #A.draw_coins()
        #A.draw_grid()
       # A.draw_text('SCORE : {}'.format(A.player.current_score), A.screen, [60,0], 16, WHITE, START_FONT)
        A.draw_text(str(Q1.text), A.screen, [200,300], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.X), A.screen, [220,320], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.symbol), A.screen, [260,320], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.Y), A.screen, [280,320], 16, PURPLE, START_FONT)
        A.draw_text("=", A.screen, [320,320], 16, PURPLE, START_FONT)
        A.draw_text("Select answer:", A.screen, [200,370], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.fake1), A.screen, [210,400], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.fake2), A.screen, [210,430], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.fake3), A.screen, [340,400], 16, PURPLE, START_FONT)
        A.draw_text(str(Q1.Total), A.screen, [340,430], 16, PURPLE, START_FONT)


        if (Q1.selection == "1"):
           A.x = 200
           A.y = 410
        elif (Q1.selection == "2"):
            A.x = 200
            A.y = 440
        elif (Q1.selection == "3"):
            A.x = 331   
            A.y = 410
            
        elif (Q1.selection == "4"):
            A.x = 331
            A.y = 440

        if (Q1.selection != "0"):
            pygame.draw.circle(A.screen, PURPLE, (A.x,A.y), 5)
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
            elif pygame.mouse.get_pressed() == (1,0,0):
                if(pygame.mouse.get_pos()[0] <= B_next.x_w and
                   pygame.mouse.get_pos()[0] >= B_next.x and
                   pygame.mouse.get_pos()[1] <= B_next.y_h and
                   pygame.mouse.get_pos()[1] >= B_next.y):
                     A.state = 'play'
                     Q1.randomQuestion()
        
    def won_update(A):
        A.check == False

    def won_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_won, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()

################### WrONg OVER FUNCTIONS #################

    def wrong_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            elif pygame.mouse.get_pressed() == (1,0,0):
                if(pygame.mouse.get_pos()[0] <= B_next.x_w and
                   pygame.mouse.get_pos()[0] >= B_next.x and
                   pygame.mouse.get_pos()[1] <= B_next.y_h and
                   pygame.mouse.get_pos()[1] >= B_next.y):
                     A.state = 'play'
                     Q1.randomQuestion()
        
    def wrong_update(A):
        A.check == False


    def wrong_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_wrong, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()
       
################### CREDITS FUNCTIONS #################

    def credits_events(A):
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
                    A.state = "start"
                    
                
            
                
    def credits_update(A):
        pass


        
    def credits_draw(A):

        A.screen.fill(BLACK)
        A.screen.blit(A.bg_credits, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update()

################### FINISH FUNCTIONS #################

    def finish_events(A):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                A.running = False
            elif pygame.mouse.get_pressed() == (1,0,0):
                if(pygame.mouse.get_pos()[0] <= b0_x1 and
                    pygame.mouse.get_pos()[0] >= b0_x0 and
                    pygame.mouse.get_pos()[1] <= b3_y1 and
                    pygame.mouse.get_pos()[1] >= b3_y0):
                    A.state = 'start'
                    A.score = 25
                    A.C_Q = 0
                    print('CREDITS')
                    Q1.randomQuestion()
                elif(pygame.mouse.get_pos()[0]<= B_start.x_w and
                   pygame.mouse.get_pos()[0] >= B_start.x and
                   pygame.mouse.get_pos()[1] <= B_start.y_h and
                   pygame.mouse.get_pos()[1] >= B_start.y):
                    print('EXIT')
                    A.running = False

        
    def finish_update(A):
        A.check == False

    def finish_draw(A):
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_results, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        A.draw_text(str(A.score), A.screen, [435,250], 20, PURPLE, START_FONT)
        A.draw_text(A.grade, A.screen, [MAZE_WIDTH//2-50,MAZE_HEIGHT//2], 50, PURPLE, START_FONT)
        pygame.display.update()

################### SPLASH FUNCTIONS ###################################################### 
  
    def splash_draw(A):
        pygame.mixer.init()
        pygame.mixer.music.load('assets/start.wav')
        pygame.mixer.music.play()
        A.screen.fill(BLACK)
        A.screen.blit(A.bg_splash, (TOP_BOTTOM_BUFFER//2,TOP_BOTTOM_BUFFER//2))
        pygame.display.update() 
        pygame.time.delay(5000)
        A.state = "start"