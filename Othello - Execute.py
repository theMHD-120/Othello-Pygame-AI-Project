"""
    ||| In the name of ALLAH |||
    -----------------------------
    Seyed Mahdi Mahdavi Mortazavi 
    StdNo.: 40030490
    -----------------------------
    Artificial Intelligence (AI)
    Assignement: Final Project #01
    >>> Othello Game Implementation
"""
import sys
import copy
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
board_size = 8
square_size = 70
window_size = board_size * square_size

# Colors constant
black = (104, 0, 0)
purple = (85, 0, 151)
yellow = (254, 190, 0)
white = (255, 255, 255)

# Pygame display setup
window = pygame.display.set_mode((window_size, 700))
pygame.display.set_caption("Othello")

# Directions for move checking (8 possible directions)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Font of messages setup
font_size = 28
pygame.font.init()
font = pygame.font.SysFont("Segoe UI Black", font_size)

# Menu Options (difficulty levels: 1, 2, 3)
difficulty_levels = {"easy": 2, "medium": 4, "hard": 6}
difficulty = difficulty_levels["easy"]  # Default difficulty level

# Number of pieces (pieces or discs - for each color)
white_pieces = 2
black_pieces = 2

# Scoreboard variables
ai_wins = 0
human_wins = 0

# Initialize the board
def init_board():
    """
    Initialize the Othello board with starting positions.

    Returns:
        numpy.ndarray: The initialized board: 
        >>> 0: Empty
        >>> 1: White
        >>> -1: Black
    """
    board = np.zeros((board_size, board_size))
    board[3, 3] = board[4, 4] = 1  # White
    board[3, 4] = board[4, 3] = -1  # Black
    return board

# A global variable for the gameboard
board = init_board()

# Functions and explanations
def draw_board(valid_moves=None, message=None):
    """
    Draw the Othello board and its pieces.

    Args:
        valid_moves (list, optional): List of tuples representing valid moves (row, col). Defaults to None.
        message (str, optional): Message to display on the screen. Defaults to None.
    """
    window.fill(yellow)
    
    # Draw the board grids
    for row in range(board_size):
        for col in range(board_size):
            pygame.draw.rect(window, black, (col * square_size, row * square_size, square_size, square_size), 1)
            if board[row, col] == 1:
                pygame.draw.circle(window, white, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 2)
            elif board[row, col] == -1:
                pygame.draw.circle(window, black, (col * square_size + square_size // 2, row * square_size + square_size // 2), square_size // 2 - 2)
    
    # Display the message on the screen
    if message:
        if message[0] == "Y":
            text = font.render(f"1) Status: {message}", True, black)
        else:
            text = font.render(f"1) Status: {message}", True, white)
        window.blit(text, (10, 565))
    
    # Highlight valid moves for the human player
    if valid_moves:
        for move in valid_moves:
            pygame.draw.rect(window, purple, (move[1] * square_size, move[0] * square_size, square_size, square_size), 4)
    
    # Draw scoreboard
    draw_piece_numbers()
    draw_scoreboard()
    pygame.display.flip()

def draw_piece_numbers():
    """
    Draw the current number of white (AI) pieces and black (human) pieces.
    """
    scoreboard_text = font.render(f"2) Pieces: White-{white_pieces}  Black-{black_pieces}", True, black)
    window.blit(scoreboard_text, (10, 605))

def draw_scoreboard():
    """
    Draw the scoreboard showing number of wins for AI and human.
    """
    scoreboard_text = font.render(f"3) Scoreboard: AI-{ai_wins}  You-{human_wins}", True, black)
    window.blit(scoreboard_text, (10, 645))

def is_valid_move(board, row, col, player):
    """
    Check if a move is valid for a given player.

    Args:
        board (numpy.ndarray): The current game board.
        row (int): Row index of the move.
        col (int): Column index of the move.
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    if board[row, col] != 0:
        return False
    for direction in directions:
        if check_direction(board, row, col, direction, player):
            return True
    return False

def check_direction(board, row, col, direction, player):
    """
    Check if there are pieces to flip in a specific direction.

    Args:
        board (numpy.ndarray): The current game board.
        row (int): Row index of the move.
        col (int): Column index of the move.
        direction (tuple): Direction to check (e.g., (-1, 0) for up).
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        bool: True if there are pieces to flip, False otherwise.
    """
    r, c = row + direction[0], col + direction[1]
    if not (0 <= r < board_size and 0 <= c < board_size):
        return False
    if board[r, c] != -player:
        return False
    while 0 <= r < board_size and 0 <= c < board_size:
        r += direction[0]
        c += direction[1]
        if not (0 <= r < board_size and 0 <= c < board_size):
            return False
        if board[r, c] == player:
            return True
        if board[r, c] == 0:
            return False
    return False

def get_valid_moves(board, player):
    """
    Get a list of valid moves for a given player.

    Args:
        board (numpy.ndarray): The current game board.
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        list: List of tuples representing valid moves (row, col).
    """
    valid_moves = []
    for row in range(board_size):
        for col in range(board_size):
            if is_valid_move(board, row, col, player):
                valid_moves.append((row, col))
    return valid_moves

def apply_move(board, row, col, player):
    """
    Apply a move to the board by flipping pieces.

    Args:
        board (numpy.ndarray): The current game board.
        row (int): Row index of the move.
        col (int): Column index of the move.
        player (int): Current player (-1 for Black, 1 for White).
    """
    board[row, col] = player
    for direction in directions:
        if check_direction(board, row, col, direction, player):
            r, c = row + direction[0], col + direction[1]
            while board[r, c] == -player:
                board[r, c] = player
                r += direction[0]
                c += direction[1]

def switch_player(player):
    """
    Switch the current player.

    Args:
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        int: New player value (-1 or 1).
    """
    return -player

def minimax(board, depth, alpha, beta, maximizing_player, player):
    """
    Minimax algorithm with alpha-beta pruning to find the best move.

    Args:
        board (numpy.ndarray): The current game board.
        depth (int): Depth of the search tree.
        alpha (float): Alpha value for pruning.
        beta (float): Beta value for pruning.
        maximizing_player (bool): True if maximizing player's turn, False otherwise.
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        tuple: Best evaluation value and corresponding move.
    """
    valid_moves = get_valid_moves(board, player)
    if depth == 0 or not valid_moves:
        return evaluate_board(board, player), None
    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            apply_move(new_board, move[0], move[1], player)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, False, switch_player(player))
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in valid_moves:
            new_board = copy.deepcopy(board)
            apply_move(new_board, move[0], move[1], player)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, True, switch_player(player))
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate_board(board, player):
    """
    Evaluate the board for a given player.

    Args:
        board (numpy.ndarray): The current game board.
        player (int): Current player (-1 for Black, 1 for White).

    Returns:
        int: Evaluation score based on the board state.
    """
    return np.sum(board) * player

def get_piece_numbers(board):
    """
    Get the current number of white and black pieces.
    """
    global white_pieces, black_pieces
    white_pieces = np.count_nonzero(board == 1)
    black_pieces = np.count_nonzero(board == -1)

def is_game_over(board):
    """
    Check if the game is over (no valid moves for both players).

    Args:
        board (numpy.ndarray): The current game board.

    Returns:
        bool: True if the game is over, False otherwise.
    """
    return not get_valid_moves(board, 1) and not get_valid_moves(board, -1)

def get_winner(board):
    """
    Get the winner of the game based on the current board state.
    np.count_nonzero: counts the non-zero (empty) homes
    
    Args:
        board (numpy.ndarray): The current game board.

    Returns:
        str: The winner ("Black", "White", or "Draw").
    """
    black_count = np.count_nonzero(board == -1)  
    white_count = np.count_nonzero(board == 1)
    if black_count > white_count:
        return "Black"
    elif white_count > black_count:
        return "White"
    else:
        return "Draw"

def draw_menu():
    """
    Draw the welcome menu with difficulty selection.
    """
    window.fill(yellow)
    back_image = pygame.image.load("./media/menu image.png")
    window.blit(back_image, (-50, 200))
    
    title_text = font.render("Welcome to Othello!", True, black)
    window.blit(title_text, (window_size // 2 - title_text.get_width() // 2, 50))
    
    menu_text = font.render("Select Difficulty:", True, black)
    window.blit(menu_text, (window_size // 2 - menu_text.get_width() // 2, 150))
    
    easy_text = font.render("1. Easy", True, black)
    window.blit(easy_text, (window_size // 2 - easy_text.get_width() // 2, 200))
    
    medium_text = font.render("2. Medium", True, black)
    window.blit(medium_text, (window_size // 2 - medium_text.get_width() // 2, 250))
    
    hard_text = font.render("3. Hard", True, black)
    window.blit(hard_text, (window_size // 2 - hard_text.get_width() // 2, 300))
    
    pygame.display.flip()

def draw_game_over_menu(winner):
    """
    Draw the game over menu with winner announcement and play again options.
    """
    window.fill(yellow)
    back_image = pygame.image.load("./media/menu image.png")
    window.blit(back_image, (-50, 200))
    
    if winner[0] == "W":
        text = font.render(f"Game Over! AI wins!", True, black)
    else:
        text = font.render(f"Greeting! You win!", True, purple)
    window.blit(text, (window_size // 2 - text.get_width() // 2, 50))
    
    play_again_text = font.render("1. Play Again", True, white)
    window.blit(play_again_text, (window_size // 2 - play_again_text.get_width() // 2, 150))
    
    quit_text = font.render("2. Quit", True, white)
    window.blit(quit_text, (window_size // 2 - quit_text.get_width() // 2, 200))
    
    pygame.display.flip()

def main_menu():
    """
    Main menu loop to handle difficulty selection.
    """
    global difficulty
    running = True
    
    while running:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    difficulty = difficulty_levels["easy"]
                    running = False
                elif event.key == pygame.K_2:
                    difficulty = difficulty_levels["medium"]
                    running = False
                elif event.key == pygame.K_3:
                    difficulty = difficulty_levels["hard"]
                    running = False

def game_over_menu(winner):
    """
    Game over menu loop to handle winner announcement and play again options.
    """
    global ai_wins, human_wins
    running = True
    
    if winner == 'White':  # AI wins
        ai_wins += 1
    elif winner == 'Black':  # Human wins
        human_wins += 1

    while running:
        draw_game_over_menu(winner)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return True  # Play again
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()  # Quit

def play_game():
    """
    Main game loop for Othello.
    """
    global board
    player = -1  # Black starts
    game_over = False
    
    while not game_over:
        if player == -1:
            valid_moves = get_valid_moves(board, player)
            if not valid_moves:
                player = switch_player(player)
                continue  # Skip turn if no valid moves for Black
            draw_board(valid_moves, "Your Turn ...")  # Display message for human player
            move_made = False
            # Wait for human player input
            while not move_made:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_position = pygame.mouse.get_pos()
                        clicked_row = mouse_position[1] // square_size
                        clicked_col = mouse_position[0] // square_size
                        if (clicked_row, clicked_col) in valid_moves:
                            pygame.mixer.music.load("./media/button sound.mp3")
                            pygame.mixer.music.play(0)
                            apply_move(board, clicked_row, clicked_col, player)
                            move_made = True
                            player = switch_player(player)
                            get_piece_numbers(board)
                            draw_board(None)  # Update board after human move
        else:
            valid_moves = get_valid_moves(board, player)
            if not valid_moves:
                player = switch_player(player)
                continue  # Skip turn if no valid moves for White
            draw_board(None, "AI Thinking ...")  # Display message for AI's turn
            _, best_move = minimax(board, difficulty, float('-inf'), float('inf'), True, player) # set difficulty as depth
            if best_move:
                apply_move(board, best_move[0], best_move[1], player)
                player = switch_player(player)
                get_piece_numbers(board)
                draw_board(None)  # Update board after AI move
        
        if is_game_over(board):
            winner = get_winner(board)
            global white_pieces, black_pieces
            white_pieces = black_pieces = 2
            game_over = True

    if game_over_menu(winner):
        board = init_board()
        play_game()

# Start the game
if __name__ == "__main__":
    main_menu()
    play_game()