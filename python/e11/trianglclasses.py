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
        font = pygame.font.Font(None, 24)  # Default font, size 24

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
    def __init__(self, width=600, height=800):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.width = width
        self.height = height

        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)

        # Initialize points collection
        self.points = []
        self.triangle = None
        self.font = pygame.font.Font(None, 24)

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

    def draw_collected_points(self):
        """Draw points that have been collected so far"""
        for i, point in enumerate(self.points, 1):
            # Draw point
            pygame.draw.circle(self.screen, self.RED, (point.x, point.y), 5)
            # Draw label
            text = f"P{i}({int(point.x)}, {int(point.y)})"
            text_surface = self.font.render(text, True, self.BLACK)
            text_rect = text_surface.get_rect(topleft=(point.x + 10, point.y + 10))
            # Draw white background for text
            background_rect = text_rect.inflate(10, 6)
            pygame.draw.rect(self.screen, self.WHITE, background_rect)
            pygame.draw.rect(self.screen, (200, 200, 200), background_rect, 1)
            # Draw text
            self.screen.blit(text_surface, text_rect)

    def handle_click(self, pos):
        """Handle mouse click event"""
        if len(self.points) < 3:
            self.points.append(Point(pos[0], pos[1]))
            if len(self.points) == 3:
                self.triangle = Triangle(*self.points)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # Reset triangle on 'R' key press
                    self.points = []
                    self.triangle = None
                    pygame.display.set_caption("Click 3 points to create a triangle")

            self.screen.fill(self.WHITE)
            self.draw_axes()

            if self.triangle:
                self.triangle.draw(self.screen)
            else:
                self.draw_collected_points()
                # self.draw_instruction()

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
