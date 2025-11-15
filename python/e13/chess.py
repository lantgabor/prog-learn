import pygame

# Simple Chess Game with OOP refactoring

class Piece:
    def __init__(self, color, row, col):
        self.color = color  # 'white' or 'black'
        self.row = row
        self.col = col
        self.selected = False
        self.symbol = ''
    
    def get_valid_moves(self, board):
        return []
    
    def _get_line_moves(self, board, directions):
        moves = []
        for dr, dc in directions:
            for i in range(1, 8):
                new_row = self.row + dr * i
                new_col = self.col + dc * i
                if not (0 <= new_row < 8 and 0 <= new_col < 8):
                    break
                if board[new_row][new_col] is None:
                    moves.append((new_row, new_col))
                elif board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
        return moves


class Pawn(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♟'
    
    def get_valid_moves(self, board):
        moves = []
        direction = -1 if self.color == 'white' else 1
        
        # Move forward
        if 0 <= self.row + direction < 8 and board[self.row + direction][self.col] is None:
            moves.append((self.row + direction, self.col))
            
            # Double move from start
            start_row = 6 if self.color == 'white' else 1
            if self.row == start_row and board[self.row + 2 * direction][self.col] is None:
                moves.append((self.row + 2 * direction, self.col))
        
        # Capture diagonally
        for dc in [-1, 1]:
            new_row, new_col = self.row + direction, self.col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] and board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        
        return moves


class Rook(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♜'
    
    def get_valid_moves(self, board):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return self._get_line_moves(board, directions)


class Knight(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♞'
    
    def get_valid_moves(self, board):
        moves = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dr, dc in knight_moves:
            new_row, new_col = self.row + dr, self.col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        return moves


class Bishop(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♝'
    
    def get_valid_moves(self, board):
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        return self._get_line_moves(board, directions)


class Queen(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♛'
    
    def get_valid_moves(self, board):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        return self._get_line_moves(board, directions)


class King(Piece):
    def __init__(self, color, row, col):
        super().__init__(color, row, col)
        self.symbol = '♚'
    
    def get_valid_moves(self, board):
        moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = self.row + dr, self.col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                        moves.append((new_row, new_col))
        return moves


def create_board():
    board = [[None for _ in range(8)] for _ in range(8)]
    
    # Pawns
    for col in range(8):
        board[1][col] = Pawn('black', 1, col)
        board[6][col] = Pawn('white', 6, col)
    
    # Rooks
    board[0][0] = Rook('black', 0, 0)
    board[0][7] = Rook('black', 0, 7)
    board[7][0] = Rook('white', 7, 0)
    board[7][7] = Rook('white', 7, 7)
    
    # Knights
    board[0][1] = Knight('black', 0, 1)
    board[0][6] = Knight('black', 0, 6)
    board[7][1] = Knight('white', 7, 1)
    board[7][6] = Knight('white', 7, 6)
    
    # Bishops
    board[0][2] = Bishop('black', 0, 2)
    board[0][5] = Bishop('black', 0, 5)
    board[7][2] = Bishop('white', 7, 2)
    board[7][5] = Bishop('white', 7, 5)
    
    # Queens
    board[0][3] = Queen('black', 0, 3)
    board[7][3] = Queen('white', 7, 3)
    
    # Kings
    board[0][4] = King('black', 0, 4)
    board[7][4] = King('white', 7, 4)
    
    return board


def draw_board(screen, square_size):
    colors = [(240, 217, 181), (181, 136, 99)]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))


def draw_pieces(screen, board, square_size, font):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece:
                color = (255, 255, 255) if piece.color == 'white' else (0, 0, 0)
                text = font.render(piece.symbol, True, color)
                text_rect = text.get_rect(center=(col * square_size + square_size // 2, row * square_size + square_size // 2))
                screen.blit(text, text_rect)
                
                if piece.selected:
                    pygame.draw.rect(screen, (0, 255, 0), (col * square_size, row * square_size, square_size, square_size), 3)


def draw_valid_moves(screen, valid_moves, square_size):
    for row, col in valid_moves:
        pygame.draw.circle(screen, (0, 200, 0), 
                         (col * square_size + square_size // 2, row * square_size + square_size // 2), 10)


def main():
    pygame.init()
    
    width = 640
    height = 640
    square_size = width // 8
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simple Chess")
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 80)
    
    board = create_board()
    selected_piece = None
    valid_moves = []
    current_turn = 'white'
    game_over = False
    winner = None
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col = x // square_size
                row = y // square_size
                
                if selected_piece:
                    # Try to move
                    if (row, col) in valid_moves:
                        # Capture piece if present
                        captured = board[row][col]
                        if captured and isinstance(captured, King):
                            game_over = True
                            winner = current_turn
                        
                        # Move piece
                        board[selected_piece.row][selected_piece.col] = None
                        selected_piece.row = row
                        selected_piece.col = col
                        board[row][col] = selected_piece
                        selected_piece.selected = False
                        selected_piece = None
                        valid_moves = []
                        
                        # Switch turns
                        current_turn = 'black' if current_turn == 'white' else 'white'
                    else:
                        # Deselect
                        selected_piece.selected = False
                        selected_piece = None
                        valid_moves = []
                
                # Select new piece
                if board[row][col] and board[row][col].color == current_turn and not selected_piece:
                    selected_piece = board[row][col]
                    selected_piece.selected = True
                    valid_moves = selected_piece.get_valid_moves(board)
        
        # Draw everything
        draw_board(screen, square_size)
        
        if not game_over:
            if valid_moves:
                draw_valid_moves(screen, valid_moves, square_size)
            
            draw_pieces(screen, board, square_size, font)
            
            # Draw turn indicator
            turn_font = pygame.font.Font(None, 36)
            turn_text = turn_font.render(f"{current_turn.capitalize()}'s turn", True, (255, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 200, 40))
            screen.blit(turn_text, (10, 10))
        else:
            draw_pieces(screen, board, square_size, font)
            
            # Game over screen
            overlay = pygame.Surface((width, height))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            
            game_over_font = pygame.font.Font(None, 74)
            winner_text = game_over_font.render(f"{winner.capitalize()} Wins!", True, (255, 215, 0))
            winner_rect = winner_text.get_rect(center=(width // 2, height // 2))
            screen.blit(winner_text, winner_rect)
        
        pygame.display.flip()
        clock.tick(30)
    
    pygame.quit()


if __name__ == "__main__":
    main()