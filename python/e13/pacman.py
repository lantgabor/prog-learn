import pygame
import sys
from enum import Enum
from typing import Tuple

print("=== GRID-BASED PACMAN GAME STARTING ===")

# Initialize Pygame
pygame.init()
print("Pygame initialized successfully")

# Constants
CELL_SIZE = 30
FPS = 60
MOVE_SPEED = 8  # Frames per cell movement (lower = faster)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PINK = (255, 192, 203)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)
DARK_BLUE = (33, 33, 222)


class Direction(Enum):
    """Enum for movement directions"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    NONE = (0, 0)


class Cell(Enum):
    """Enum for cell types in the map"""
    EMPTY = 0
    WALL = 1
    DOT = 2
    POWER_PELLET = 3
    GHOST_HOUSE = 4


class Entity:
    """Base class for all game entities - GRID BASED"""
    def __init__(self, grid_x: int, grid_y: int, color: Tuple[int, int, int]):
        # Grid position (integer coordinates)
        self.grid_x = grid_x
        self.grid_y = grid_y
        
        # Visual position for smooth animation (float)
        self.visual_x = float(grid_x)
        self.visual_y = float(grid_y)
        
        self.color = color
        self.direction = Direction.NONE
        self.next_direction = Direction.NONE
        
        # Movement animation
        self.is_moving = False
        self.move_progress = 0  # 0 to MOVE_SPEED
        self.target_x = grid_x
        self.target_y = grid_y
        
    def get_grid_position(self) -> Tuple[int, int]:
        """Get the current grid position"""
        return (self.grid_x, self.grid_y)
    
    def update_visual_position(self):
        """Smoothly interpolate visual position towards grid position"""
        if self.is_moving:
            # Interpolate between current grid position and target
            progress_ratio = self.move_progress / MOVE_SPEED
            self.visual_x = self.grid_x + (self.target_x - self.grid_x) * progress_ratio
            self.visual_y = self.grid_y + (self.target_y - self.grid_y) * progress_ratio
            
            self.move_progress += 1
            
            # Complete the move
            if self.move_progress >= MOVE_SPEED:
                self.grid_x = self.target_x
                self.grid_y = self.target_y
                self.visual_x = float(self.grid_x)
                self.visual_y = float(self.grid_y)
                self.is_moving = False
                self.move_progress = 0
        else:
            # Not moving, visual matches grid
            self.visual_x = float(self.grid_x)
            self.visual_y = float(self.grid_y)
    
    def draw(self, screen: pygame.Surface):
        """Draw the entity on the screen"""
        # Draw at visual position for smooth movement
        center_x = int(self.visual_x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.visual_y * CELL_SIZE + CELL_SIZE // 2)
        
        pygame.draw.circle(
            screen,
            self.color,
            (center_x, center_y),
            CELL_SIZE // 2 - 2
        )


class PacMan(Entity):
    """PacMan player class - GRID BASED"""
    def __init__(self, grid_x: int, grid_y: int):
        super().__init__(grid_x, grid_y, YELLOW)
        self.score = 0
        self.lives = 3
        print(f"PacMan initialized at grid ({grid_x}, {grid_y})")
        
    def set_direction(self, direction: Direction):
        """Set the next direction for PacMan"""
        self.next_direction = direction
        print(f"PacMan next_direction set to {direction}")
        
    def update(self, game_map: 'GameMap'):
        """Update PacMan's position - GRID BASED"""
        print(f"PacMan.update() - grid: ({self.grid_x}, {self.grid_y}), moving: {self.is_moving}, dir: {self.direction}")
        
        # Update visual position for smooth animation
        self.update_visual_position()
        
        # Can only change direction when not moving
        if not self.is_moving:
            # Try to use the queued next direction
            if self.next_direction != Direction.NONE:
                new_x = self.grid_x + self.next_direction.value[0]
                new_y = self.grid_y + self.next_direction.value[1]
                
                if game_map.can_move_to(new_x, new_y):
                    print(f"  Direction change accepted: {self.next_direction}")
                    self.direction = self.next_direction
                    self.next_direction = Direction.NONE
                    self._start_move(new_x, new_y)
                else:
                    print(f"  Direction change blocked - wall at ({new_x}, {new_y})")
            
            # Continue in current direction if no new direction
            if not self.is_moving and self.direction != Direction.NONE:
                new_x = self.grid_x + self.direction.value[0]
                new_y = self.grid_y + self.direction.value[1]
                
                if game_map.can_move_to(new_x, new_y):
                    self._start_move(new_x, new_y)
                    print(f"  Moving {self.direction} to ({new_x}, {new_y})")
                else:
                    print(f"  Blocked - stopping")
                    self.direction = Direction.NONE
    
    def _start_move(self, target_x: int, target_y: int):
        """Start moving to a target grid position"""
        self.target_x = target_x
        self.target_y = target_y
        self.is_moving = True
        self.move_progress = 0


class Ghost(Entity):
    """Ghost enemy class - GRID BASED"""
    def __init__(self, grid_x: int, grid_y: int, color: Tuple[int, int, int], name: str):
        super().__init__(grid_x, grid_y, color)
        self.name = name
        self.frightened = False
        self.frightened_timer = 0
        self.base_color = color
        print(f"Ghost {name} initialized at grid ({grid_x}, {grid_y})")
        
    def update(self, game_map: 'GameMap', target: Tuple[int, int]):
        """Update ghost's position with simple AI - GRID BASED"""
        import random
        
        # Update frightened state
        if self.frightened:
            self.frightened_timer -= 1
            if self.frightened_timer <= 0:
                self.frightened = False
        
        # Update visual position for smooth animation
        self.update_visual_position()
        
        # Can only change direction when not moving
        if not self.is_moving:
            # Get possible directions
            possible_directions = []
            opposite_map = {
                Direction.UP: Direction.DOWN,
                Direction.DOWN: Direction.UP,
                Direction.LEFT: Direction.RIGHT,
                Direction.RIGHT: Direction.LEFT,
                Direction.NONE: Direction.NONE
            }
            
            for direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]:
                new_x = self.grid_x + direction.value[0]
                new_y = self.grid_y + direction.value[1]
                
                if game_map.can_move_to(new_x, new_y):
                    # Don't go backwards unless it's the only option
                    opposite = opposite_map[self.direction]
                    if direction != opposite or len(possible_directions) == 0:
                        possible_directions.append(direction)
            
            # Choose a direction
            if possible_directions:
                # Simple random AI
                self.direction = random.choice(possible_directions)
                new_x = self.grid_x + self.direction.value[0]
                new_y = self.grid_y + self.direction.value[1]
                self._start_move(new_x, new_y)
            else:
                self.direction = Direction.NONE
    
    def _start_move(self, target_x: int, target_y: int):
        """Start moving to a target grid position"""
        self.target_x = target_x
        self.target_y = target_y
        self.is_moving = True
        self.move_progress = 0
    
    def set_frightened(self, duration: int):
        """Set ghost to frightened mode"""
        self.frightened = True
        self.frightened_timer = duration
    
    def draw(self, screen: pygame.Surface):
        """Draw the ghost"""
        color = BLUE if self.frightened else self.base_color
        
        # Draw at visual position for smooth movement
        center_x = int(self.visual_x * CELL_SIZE + CELL_SIZE // 2)
        center_y = int(self.visual_y * CELL_SIZE + CELL_SIZE // 2)
        
        pygame.draw.circle(
            screen,
            color,
            (center_x, center_y),
            CELL_SIZE // 2 - 2
        )
        
        # Draw eyes
        eye_offset = 5
        pygame.draw.circle(
            screen,
            WHITE,
            (center_x - eye_offset, center_y - 3),
            3
        )
        pygame.draw.circle(
            screen,
            WHITE,
            (center_x + eye_offset, center_y - 3),
            3
        )


class GameMap:
    """Game map class that holds the 2D matrix - GRID BASED"""
    def __init__(self):
        # Define the map as a 2D matrix
        # 0 = Empty, 1 = Wall, 2 = Dot, 3 = Power Pellet, 4 = Ghost House
        self.map_data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1],
            [0, 0, 0, 1, 2, 1, 0, 0, 0, 4, 0, 0, 0, 1, 2, 1, 0, 0, 0],
            [1, 1, 1, 1, 2, 1, 0, 1, 1, 4, 1, 1, 0, 1, 2, 1, 1, 1, 1],
            [0, 0, 0, 0, 2, 0, 0, 1, 4, 4, 4, 1, 0, 0, 2, 0, 0, 0, 0],
            [1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1],
            [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0],
            [1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
            [1, 3, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 3, 1],
            [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
            [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
            [1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1],
            [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        
        self.height = len(self.map_data)
        self.width = len(self.map_data[0])
        self.total_dots = self.count_dots()
        
        print(f"Map created: {self.width}x{self.height} grid, {self.total_dots} dots")
        
    def count_dots(self) -> int:
        """Count total dots in the map"""
        count = 0
        for row in self.map_data:
            for cell in row:
                if cell == Cell.DOT.value or cell == Cell.POWER_PELLET.value:
                    count += 1
        return count
    
    def get_cell(self, grid_x: int, grid_y: int) -> int:
        """Get the cell value at given GRID position"""
        if 0 <= grid_y < self.height and 0 <= grid_x < self.width:
            return self.map_data[grid_y][grid_x]
        return Cell.WALL.value  # Treat out of bounds as wall
    
    def set_cell(self, grid_x: int, grid_y: int, value: int):
        """Set the cell value at given GRID position"""
        if 0 <= grid_y < self.height and 0 <= grid_x < self.width:
            self.map_data[grid_y][grid_x] = value
    
    def can_move_to(self, grid_x: int, grid_y: int) -> bool:
        """Check if an entity can move to the given GRID position - SIMPLE!"""
        cell = self.get_cell(grid_x, grid_y)
        is_walkable = cell != Cell.WALL.value
        print(f"    can_move_to grid({grid_x}, {grid_y}) = cell:{cell} -> {is_walkable}")
        return is_walkable
    
    def draw(self, screen: pygame.Surface):
        """Draw the map on the screen"""
        for y in range(self.height):
            for x in range(self.width):
                cell = self.map_data[y][x]
                
                # Calculate pixel position
                pixel_x = x * CELL_SIZE
                pixel_y = y * CELL_SIZE
                rect = pygame.Rect(pixel_x, pixel_y, CELL_SIZE, CELL_SIZE)
                
                if cell == Cell.WALL.value:
                    pygame.draw.rect(screen, DARK_BLUE, rect)
                    pygame.draw.rect(screen, BLUE, rect, 1)
                elif cell == Cell.DOT.value:
                    center_x = pixel_x + CELL_SIZE // 2
                    center_y = pixel_y + CELL_SIZE // 2
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), 2)
                elif cell == Cell.POWER_PELLET.value:
                    center_x = pixel_x + CELL_SIZE // 2
                    center_y = pixel_y + CELL_SIZE // 2
                    pygame.draw.circle(screen, WHITE, (center_x, center_y), 6)
                elif cell == Cell.GHOST_HOUSE.value:
                    pygame.draw.rect(screen, PINK, rect)


class Game:
    """Main game class"""
    def __init__(self):
        print("\n=== Initializing Game ===")
        self.game_map = GameMap()
        
        self.screen_width = self.game_map.width * CELL_SIZE
        self.screen_height = self.game_map.height * CELL_SIZE + 50  # Extra space for UI
        print(f"Screen size: {self.screen_width} x {self.screen_height}")
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pac-Man (Grid-Based)")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.won = False
        
        # Initialize entities at GRID positions
        print("\n=== Creating Entities ===")
        self.pacman = PacMan(9, 15)
        self.ghosts = [
            Ghost(9, 9, RED, "Blinky"),
            Ghost(8, 9, PINK, "Pinky"),
            Ghost(10, 9, CYAN, "Inky"),
            Ghost(9, 10, ORANGE, "Clyde"),
        ]
        
        self.dots_eaten = 0
        self.font = pygame.font.Font(None, 36)
        
        # Validate starting positions
        print("\n=== Initial Position Check ===")
        pm_cell = self.game_map.get_cell(self.pacman.grid_x, self.pacman.grid_y)
        print(f"PacMan at grid ({self.pacman.grid_x}, {self.pacman.grid_y}) - cell value: {pm_cell}")
        
        for ghost in self.ghosts:
            g_cell = self.game_map.get_cell(ghost.grid_x, ghost.grid_y)
            print(f"{ghost.name} at grid ({ghost.grid_x}, {ghost.grid_y}) - cell value: {g_cell}")
        
        # Test movement capability
        print("\n=== PacMan Movement Test ===")
        test_dirs = [("UP", 0, -1), ("DOWN", 0, 1), ("LEFT", -1, 0), ("RIGHT", 1, 0)]
        for name, dx, dy in test_dirs:
            test_x = self.pacman.grid_x + dx
            test_y = self.pacman.grid_y + dy
            can_move = self.game_map.can_move_to(test_x, test_y)
            print(f"  Can move {name} to grid ({test_x}, {test_y}): {can_move}")
        
        print("=== Game Initialized ===\n")
        
    def handle_events(self):
        """Handle user input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QUIT event received")
                self.running = False
            elif event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.pacman.set_direction(Direction.UP)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.pacman.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.pacman.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.pacman.set_direction(Direction.RIGHT)
                elif event.key == pygame.K_SPACE and (self.game_over or self.won):
                    print("SPACE pressed - resetting game")
                    self.reset_game()
    
    def update(self):
        """Update game state"""
        if self.game_over or self.won:
            return
        
        # Update PacMan
        self.pacman.update(self.game_map)
        
        # Check if PacMan ate a dot (only when at exact grid position)
        if not self.pacman.is_moving:
            grid_x, grid_y = self.pacman.get_grid_position()
            cell = self.game_map.get_cell(grid_x, grid_y)
            
            if cell == Cell.DOT.value:
                self.pacman.score += 10
                self.game_map.set_cell(grid_x, grid_y, Cell.EMPTY.value)
                self.dots_eaten += 1
                print(f"Ate dot! Score: {self.pacman.score}")
            elif cell == Cell.POWER_PELLET.value:
                self.pacman.score += 50
                self.game_map.set_cell(grid_x, grid_y, Cell.EMPTY.value)
                self.dots_eaten += 1
                # Make all ghosts frightened
                for ghost in self.ghosts:
                    ghost.set_frightened(300)  # 5 seconds at 60 FPS
                print(f"Ate power pellet! Score: {self.pacman.score}, Ghosts frightened!")
        
        # Check if won
        if self.dots_eaten >= self.game_map.total_dots:
            self.won = True
            print("YOU WIN!")
        
        # Update ghosts
        for ghost in self.ghosts:
            ghost.update(self.game_map, (self.pacman.grid_x, self.pacman.grid_y))
            
            # Check collision with PacMan (only when both at exact grid positions)
            if not self.pacman.is_moving and not ghost.is_moving:
                if ghost.grid_x == self.pacman.grid_x and ghost.grid_y == self.pacman.grid_y:
                    if ghost.frightened:
                        # Eat the ghost
                        self.pacman.score += 200
                        ghost.grid_x = 9
                        ghost.grid_y = 9
                        ghost.visual_x = 9.0
                        ghost.visual_y = 9.0
                        ghost.frightened = False
                        ghost.is_moving = False
                        print(f"Ate {ghost.name}! Score: {self.pacman.score}")
                    else:
                        # PacMan loses a life
                        self.pacman.lives -= 1
                        print(f"Hit by {ghost.name}! Lives remaining: {self.pacman.lives}")
                        if self.pacman.lives <= 0:
                            self.game_over = True
                            print("GAME OVER!")
                        else:
                            self.reset_positions()
    
    def reset_positions(self):
        """Reset positions of PacMan and ghosts"""
        print("Resetting positions...")
        self.pacman.grid_x = 9
        self.pacman.grid_y = 15
        self.pacman.visual_x = 9.0
        self.pacman.visual_y = 9.0
        self.pacman.direction = Direction.NONE
        self.pacman.next_direction = Direction.NONE
        self.pacman.is_moving = False
        
        ghost_positions = [(9, 9), (8, 9), (10, 9), (9, 10)]
        for i, ghost in enumerate(self.ghosts):
            ghost.grid_x, ghost.grid_y = ghost_positions[i]
            ghost.visual_x = float(ghost.grid_x)
            ghost.visual_y = float(ghost.grid_y)
            ghost.direction = Direction.NONE
            ghost.frightened = False
            ghost.is_moving = False
    
    def reset_game(self):
        """Reset the entire game"""
        print("Resetting game...")
        self.game_map = GameMap()
        self.pacman = PacMan(9, 15)
        self.ghosts = [
            Ghost(9, 9, RED, "Blinky"),
            Ghost(8, 9, PINK, "Pinky"),
            Ghost(10, 9, CYAN, "Inky"),
            Ghost(9, 10, ORANGE, "Clyde"),
        ]
        self.dots_eaten = 0
        self.game_over = False
        self.won = False
    
    def draw(self):
        """Draw everything on the screen"""
        self.screen.fill(BLACK)
        
        # Draw map
        self.game_map.draw(self.screen)
        
        # Draw entities
        self.pacman.draw(self.screen)
        for ghost in self.ghosts:
            ghost.draw(self.screen)
        
        # Draw UI
        score_text = self.font.render(f"Score: {self.pacman.score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {self.pacman.lives}", True, WHITE)
        self.screen.blit(score_text, (10, self.screen_height - 45))
        self.screen.blit(lives_text, (self.screen_width - 150, self.screen_height - 45))
        
        # Draw game over or win text
        if self.game_over:
            game_over_text = self.font.render("GAME OVER - Press SPACE to restart", True, RED)
            text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(game_over_text, text_rect)
        elif self.won:
            win_text = self.font.render("YOU WIN! - Press SPACE to restart", True, YELLOW)
            text_rect = win_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))
            self.screen.blit(win_text, text_rect)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        print("\n=== ENTERING MAIN GAME LOOP ===\n")
        frame_count = 0
        
        while self.running:
            frame_count += 1
            
            # Reduced logging - only first 5 frames and every 60 frames
            if frame_count <= 5:
                print(f"\n========== FRAME {frame_count} ==========")
            elif frame_count % 60 == 0:
                print(f"\n[Frame {frame_count}] PacMan: grid({self.pacman.grid_x}, {self.pacman.grid_y}), Score: {self.pacman.score}")
            
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        print("\n=== GAME LOOP ENDED ===")
        pygame.quit()
        sys.exit()


def main():
    """Main entry point"""
    print("\n" + "="*50)
    print("GRID-BASED PACMAN GAME")
    print("="*50 + "\n")
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"\n!!! EXCEPTION OCCURRED !!!")
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    print("Script started - Grid-based system")
    main()