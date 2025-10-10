import pygame
import math


# Shape classes
class Shape:
    def __init__(self, x, y, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.color = color


class Triangle(Shape):
    def __init__(self, x, y, size=50, color=(255, 255, 255)):
        super().__init__(x, y, color)
        self.size = size

    def draw(self, screen):
        points = [
            (self.x, self.y - self.size),
            (self.x - self.size, self.y + self.size),
            (self.x + self.size, self.y + self.size),
        ]
        pygame.draw.polygon(screen, self.color, points)


class Square(Shape):
    def __init__(self, x, y, size=50, color=(255, 255, 255)):
        super().__init__(x, y, color)
        self.size = size

    def draw(self, screen):
        rect = pygame.Rect(
            self.x - self.size, self.y - self.size, self.size * 2, self.size * 2
        )
        pygame.draw.rect(screen, self.color, rect)


class Circle(Shape):
    def __init__(self, x, y, radius=25, color=(255, 255, 255)):
        super().__init__(x, y, color)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Initialize shapes list and current shape type
shapes = []
current_shape = "circle"  # Default shape
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
}
current_color = colors["white"]  # Default color

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            x, y = pygame.mouse.get_pos()

            # Create new shape based on current selection
            if current_shape == "triangle":
                shapes.append(Triangle(x, y, color=current_color))
            elif current_shape == "square":
                shapes.append(Square(x, y, color=current_color))
            elif current_shape == "circle":
                shapes.append(Circle(x, y, color=current_color))

        elif event.type == pygame.KEYDOWN:
            # Change shape with number keys
            if event.key == pygame.K_1:
                current_shape = "triangle"
            elif event.key == pygame.K_2:
                current_shape = "square"
            elif event.key == pygame.K_3:
                current_shape = "circle"
            # Change colors with letter keys
            elif event.key == pygame.K_r:
                current_color = colors["red"]
            elif event.key == pygame.K_g:
                current_color = colors["green"]
            elif event.key == pygame.K_b:
                current_color = colors["blue"]
            elif event.key == pygame.K_w:
                current_color = colors["white"]

    # Fill the screen with background color
    screen.fill("purple")

    # Draw all shapes
    for shape in shapes:
        shape.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
