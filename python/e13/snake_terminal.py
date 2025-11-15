import time
import sys
import os
import random
import termios
import tty
import select

# Daniel Shiffman
# http://codingtra.in
# http://patreon.com/codingtrain
# Code for: https://youtu.be/AaGK-fj-BAM
# Python/Terminal CLI version

class Snake:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.xspeed = 1
        self.yspeed = 0
        self.total = 0
        self.tail = []
    
    def eat(self, pos):
        d = ((self.x - pos[0])**2 + (self.y - pos[1])**2)**0.5
        if d < 1:
            self.total += 1
            return True
        else:
            return False
    
    def dir(self, x, y):
        self.xspeed = x
        self.yspeed = y
    
    def death(self):
        for pos in self.tail:
            d = ((self.x - pos[0])**2 + (self.y - pos[1])**2)**0.5
            if d < 1:
                return True
        return False
    
    def update(self, scl, width, height):
        for i in range(len(self.tail) - 1):
            self.tail[i] = self.tail[i + 1]
        
        if self.total >= 1:
            if len(self.tail) < self.total:
                self.tail.append((self.x, self.y))
            else:
                self.tail[self.total - 1] = (self.x, self.y)
        
        self.x = self.x + self.xspeed * scl
        self.y = self.y + self.yspeed * scl
        
        self.x = max(0, min(self.x, width - scl))
        self.y = max(0, min(self.y, height - scl))


def pick_location(width, height, scl):
    cols = width // scl
    rows = height // scl
    food_x = random.randint(0, cols - 1) * scl
    food_y = random.randint(0, rows - 1) * scl
    return (food_x, food_y)


def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')


def draw_board(width, height, scl, snake, food):
    cols = width // scl
    rows = height // scl
    
    # Create empty board
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # Draw snake tail
    for pos in snake.tail:
        col = pos[0] // scl
        row = pos[1] // scl
        if 0 <= row < rows and 0 <= col < cols:
            board[row][col] = 'o'
    
    # Draw snake head
    head_col = snake.x // scl
    head_row = snake.y // scl
    if 0 <= head_row < rows and 0 <= head_col < cols:
        board[head_row][head_col] = 'O'
    
    # Draw food
    food_col = food[0] // scl
    food_row = food[1] // scl
    if 0 <= food_row < rows and 0 <= food_col < cols:
        board[food_row][food_col] = '*'
    
    # Print board
    print('┌' + '─' * cols + '┐')
    for row in board:
        print('│' + ''.join(row) + '│')
    print('└' + '─' * cols + '┘')


def get_key():
    if select.select([sys.stdin], [], [], 0)[0]:
        return sys.stdin.read(1)
    return None


def main():
    width = 30
    height = 20
    scl = 1
    
    s = Snake()
    food = pick_location(width, height, scl)
    game_over = False
    
    # Set up terminal for non-blocking input
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())
        
        frame_count = 0
        frame_rate = 10  # frames per second
        frame_delay = 1.0 / frame_rate
        
        while not game_over:
            start_time = time.time()
            
            # Get keyboard input
            key = get_key()
            if key:
                if key == 'w' or key == '\x1b':
                    # Check if it's an arrow key
                    if key == '\x1b':
                        next1 = get_key()
                        next2 = get_key()
                        if next1 == '[':
                            if next2 == 'A':  # Up arrow
                                s.dir(0, -1)
                            elif next2 == 'B':  # Down arrow
                                s.dir(0, 1)
                            elif next2 == 'C':  # Right arrow
                                s.dir(1, 0)
                            elif next2 == 'D':  # Left arrow
                                s.dir(-1, 0)
                    else:
                        s.dir(0, -1)
                elif key == 's':
                    s.dir(0, 1)
                elif key == 'd':
                    s.dir(1, 0)
                elif key == 'a':
                    s.dir(-1, 0)
                elif key == 'q':
                    break
            
            # Clear screen and draw
            clear_screen()
            
            if s.eat(food):
                food = pick_location(width, height, scl)
            
            if s.death():
                game_over = True
                clear_screen()
                print("\n" * 5)
                print("  ╔════════════════════╗")
                print("  ║    YOU LOST!       ║")
                print("  ║                    ║")
                print(f"  ║  Score: {s.total:3d}        ║")
                print("  ╔════════════════════╗")
                print("\n")
                break
            
            s.update(scl, width, height)
            draw_board(width, height, scl, s, food)
            
            print(f"\nScore: {s.total}")
            print("Controls: W/A/S/D or Arrow Keys | Q to quit")
            
            # Frame timing
            elapsed = time.time() - start_time
            if elapsed < frame_delay:
                time.sleep(frame_delay - elapsed)
            
            frame_count += 1
    
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if __name__ == "__main__":
    main()