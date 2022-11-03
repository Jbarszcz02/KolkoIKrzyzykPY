import pygame, sys
import numpy as np
# Inicjalizcja
pygame.init()

# Ustawienie szerokości , wysokości
WIDTH = 600
HEIGHT = 600

# Szerokość linii w grze
LINE_WIDTH = 15

# Wiersze i kolumny
BOARD_ROWS = 3
BOARD_COLS = 3

# Radius koła i szerokość
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15

# Szerokość X i odstęp
CROSS_WIDTH = 25
SPACE = 55

# Kolory w RGB
RED = (255, 0, 0)
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Ekran z podaną szerokością i wysokością
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

# Ustawienie tytułu
pygame.display.set_caption(" Kółko i Krzyżyk ")

# Kolor ekranu
screen.fill( BG_COLOR )

# Tworzenie Board
board = np.zeros( (BOARD_ROWS, BOARD_COLS) )
print(board)

# Tworzenie linii
# pygame.draw.line(screen, RED,(10, 10), (300,300), 10)


# Funkcja rysująca linie

def draw_lines():
    # Pierwsza pozioma linia
    pygame.draw.line(screen, LINE_COLOR, (0,200),(600,200) , LINE_WIDTH)
    
    # Druga pozioma linia
    pygame.draw.line(screen, LINE_COLOR, (0,400),(600,400) , LINE_WIDTH)
    
    # Pierwsza pionowa linia
    pygame.draw.line(screen, LINE_COLOR, (200,0),(200,600) , LINE_WIDTH)
    
    # Druga pionowa linia
    pygame.draw.line(screen, LINE_COLOR, (400,0),(400,600) , LINE_WIDTH)
    
# Funkcja rysująca figury

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int( col * 200 + 100 ), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH )
                pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),(col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
    
# Zaznaczanie kwadratu
def mark_square(row, col, player):
    board[row][col] = player
    
# Sprawdzenie czy kwadrat jest dostępny
def available_square(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

# Sprawdzenie czy plansza jest pełna
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

# Sprawdzanie wygranej
def check_win(player):
    # Pionowe sprawdzenie wygranej
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
        
    # Poziome sprawdzenie wygranej
    for row in range(BOARD_ROWS):
        if board[row][0] == player == board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
        
    # Pierwsza przekątna wygrana
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    
    # Druga przekątna wygrana
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    
    return False

# Rysowanie wygranej linii
def draw_vertical_winning_line(col, player):
    posX = col * 200  + 100
    
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    
    pygame.draw.line(screen, color, (posX, 15) , (posX, HEIGHT - 15), 15)

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100
 
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
        
    pygame.draw.line(screen,color,( 15, posY), (WIDTH - 15, posY), 15)

def draw_asc_diagonal(player):
     if player == 1:
        color = CIRCLE_COLOR
     elif player == 2:
        color = CROSS_COLOR
    
     pygame.draw.line(screen,color,(15, HEIGHT - 15), (WIDTH - 15, 15), 15)

def draw_desc_diagonal(player):
     if player == 1:
        color = CIRCLE_COLOR
     elif player == 2:
        color = CROSS_COLOR

     pygame.draw.line(screen,color,(15,15), (WIDTH - 15, HEIGHT - 15), 15)
#Funkcja restartu
def restart():
    screen.fill( BG_COLOR )
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# Wywołanie funkcji rysującej linie   
draw_lines()

# Zmienna gracza
player = 1

# Koniec gry
game_over = False


# Główna pętla , żeby ekran sie nie zamykał, aktualizacja ekranu ,żeby zmienić np. kolor
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            
            mouseX = event.pos[0] # x 
            mouseY = event.pos[1] # y
            
            # Klikanie w pole przez gracza
            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)
            
            # Sprawdzenie czy mozna kliknąć pole i zmiana gracza na drugiego
            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col, 1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_square(clicked_row,clicked_col, 2)
                    if check_win(player):
                        game_over = True
                    player = 1
                
                draw_figures()
                
                
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_r:
                 restart()
                 game_over = False
                
                
    pygame.display.update()