import pygame


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def to_tuple(self):
        return (self.x, self.y)


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point, color=(255, 0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self._calculate_midpoints()

    def _calculate_midpoints(self):
        """Calculate all midpoints of the triangle sides"""
        self.midpoint_a = Point(
            (self.p2.x + self.p3.x) / 2, (self.p2.y + self.p3.y) / 2
        )  # Midpoint of side A (opposite to p1)
        self.midpoint_b = Point(
            (self.p1.x + self.p3.x) / 2, (self.p1.y + self.p3.y) / 2
        )  # Midpoint of side B (opposite to p2)
        self.midpoint_c = Point(
            (self.p1.x + self.p2.x) / 2, (self.p1.y + self.p2.y) / 2
        )  # Midpoint of side C (opposite to p3)

    def calculate_centroid(self):
        """Calculate the centroid (intersection of medians) of the triangle"""
        return Point(
            (self.p1.x + self.p2.x + self.p3.x) / 3,
            (self.p1.y + self.p2.y + self.p3.y) / 3,
        )

    def draw(self, screen, draw_midpoints=True):
        """Draw the triangle and optionally its midpoints"""
        points = [self.p1.to_tuple(), self.p2.to_tuple(), self.p3.to_tuple()]
        pygame.draw.polygon(screen, self.color, points)

        # Initialize font
        font = pygame.font.Font(None, 20)  # Default font, size 20

        # Draw vertex points and their coordinates
        for i, point in enumerate([self.p1, self.p2, self.p3], 1):
            # Draw coordinate text with white background for better visibility
            text = f"P{i}({int(point.x)}, {int(point.y)})"
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(topleft=(point.x + 10, point.y + 10))

            # Draw white background
            background_rect = text_rect.inflate(10, 6)
            pygame.draw.rect(screen, (255, 255, 255), background_rect)
            pygame.draw.rect(screen, (200, 200, 200), background_rect, 1)

            # Draw text
            screen.blit(text_surface, text_rect)

        if draw_midpoints:
            # Draw midpoints as small circles
            midpoint_color = (0, 0, 255)  # Blue color for midpoints
            radius = 5

            # Draw and label midpoints
            for i, midpoint in enumerate(
                [self.midpoint_a, self.midpoint_b, self.midpoint_c], 1
            ):
                pygame.draw.circle(screen, midpoint_color, midpoint.to_tuple(), radius)

                # Draw midpoint coordinates
                text = f"M{i}({int(midpoint.x)}, {int(midpoint.y)})"
                text_surface = font.render(text, True, midpoint_color)
                text_rect = text_surface.get_rect(
                    topleft=(midpoint.x + 10, midpoint.y + 10)
                )

                # Draw white background
                background_rect = text_rect.inflate(10, 6)
                pygame.draw.rect(screen, (255, 255, 255), background_rect)
                pygame.draw.rect(screen, (200, 200, 200), background_rect, 1)

                # Draw text
                screen.blit(text_surface, text_rect)

            # Draw lines to midpoints (medians)
            pygame.draw.line(
                screen,
                midpoint_color,
                self.p1.to_tuple(),
                self.midpoint_a.to_tuple(),
                1,
            )
            pygame.draw.line(
                screen,
                midpoint_color,
                self.p2.to_tuple(),
                self.midpoint_b.to_tuple(),
                1,
            )
            pygame.draw.line(
                screen,
                midpoint_color,
                self.p3.to_tuple(),
                self.midpoint_c.to_tuple(),
                1,
            )

            # Draw and label centroid
            centroid = self.calculate_centroid()
            pygame.draw.circle(
                screen, (0, 255, 0), centroid.to_tuple(), radius
            )  # Green centroid

            # Draw centroid coordinates
            text = f"C({int(centroid.x)}, {int(centroid.y)})"
            text_surface = font.render(text, True, (0, 155, 0))
            text_rect = text_surface.get_rect(
                topleft=(centroid.x + 10, centroid.y + 10)
            )

            # Draw white background
            background_rect = text_rect.inflate(10, 6)
            pygame.draw.rect(screen, (255, 255, 255), background_rect)
            pygame.draw.rect(screen, (200, 200, 200), background_rect, 1)

            # Draw text
            screen.blit(text_surface, text_rect)


class Game:
    def __init__(self, width=1280, height=1024):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Triangle with Midpoints")
        self.width = width
        self.height = height

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Create triangle
        p1 = Point(0, 0)  # Top point
        p2 = Point(width // 2, height // 2)  # Bottom left
        p3 = Point(100, 200)  # Bottom right
        self.triangle = Triangle(p1, p2, p3)

    def draw_axes(self):
        """Draw coordinate axes"""
        pygame.draw.line(
            self.screen,
            self.BLACK,
            (0, self.height // 2),
            (self.width, self.height // 2),
            2,
        )  # X-axis
        pygame.draw.line(
            self.screen,
            self.BLACK,
            (self.width // 2, 0),
            (self.width // 2, self.height),
            2,
        )  # Y-axis

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.WHITE)
            self.draw_axes()
            self.triangle.draw(self.screen)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
