import pygame
from typing import List, Tuple


class Point:
    """Simple 2D point container."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_int_tuple(self) -> Tuple[int, int]:
        return (int(self.x), int(self.y))


class Polygon:
    """Collects points and can be closed and filled."""

    def __init__(
        self,
        color: Tuple[int, int, int] = (200, 100, 50),
        border_color=(0, 0, 0),
    ):
        self.points: List[Point] = []
        self.closed = False
        self.color = color
        self.border_color = border_color

    def add_point(self, p: Point) -> None:
        if not self.closed:
            self.points.append(p)

    def close(self) -> bool:
        """Close the polygon. Returns True if successfully closed (needs >=3 points)."""
        if len(self.points) >= 3:
            self.closed = True
            return True
        return False

    def reset(self) -> None:
        self.points = []
        self.closed = False

    def point_tuples(self) -> List[Tuple[int, int]]:
        return [p.to_int_tuple() for p in self.points]

    def draw(self, screen: pygame.Surface) -> None:
        pts = self.point_tuples()
        if not pts:
            return

        if self.closed:
            # Fill polygon and draw border
            pygame.draw.polygon(screen, self.color, pts)
            pygame.draw.polygon(screen, self.border_color, pts, 2)
        else:
            # Draw vertices and connecting lines
            if len(pts) == 1:
                pygame.draw.circle(screen, self.border_color, pts[0], 4)
            else:
                pygame.draw.lines(screen, self.border_color, False, pts, 2)
                for pt in pts:
                    pygame.draw.circle(screen, self.border_color, pt, 4)


class Game:
    """Main game loop for drawing a custom polygon."""

    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

        self.BG = (255, 255, 255)
        self.FG = (0, 0, 0)

        self.polygons = []
        self.current_polygon = Polygon()

        # Animation properties
        self.rotation_angle = 0
        self.rect_size = (100, 60)  # width and height of rectangle
        self.rect_color = (50, 120, 200)
        self.rotation_speed = 2  # degrees per frame

        pygame.display.set_caption("Polygon Drawer")

    def handle_click(self, pos: Tuple[int, int]) -> None:
        if not self.current_polygon.closed:
            self.current_polygon.add_point(Point(pos[0], pos[1]))

    def handle_key(self, key: int) -> None:
        if key == pygame.K_d and not self.current_polygon.closed:
            if self.current_polygon.close():
                self.polygons.append(self.current_polygon)
                self.current_polygon = Polygon()
        elif key == pygame.K_r:
            if not self.current_polygon.closed:
                self.current_polygon.reset()
            else:
                self.polygons = []
                self.current_polygon = Polygon()

    def draw_rotating_rectangle(self):
        # Create a surface for the rectangle
        rect_surface = pygame.Surface(self.rect_size, pygame.SRCALPHA)
        pygame.draw.rect(rect_surface, self.rect_color, (0, 0, *self.rect_size))

        # Get the rectangle's center position
        center_x = self.width // 2
        center_y = self.height // 2

        # Rotate the surface
        rotated_surface = pygame.transform.rotate(
            rect_surface, self.rotation_angle
        )

        # Get the new rect centered at the same position
        rect = rotated_surface.get_rect(center=(center_x, center_y))

        # Draw the rotated rectangle
        self.screen.blit(rotated_surface, rect)

        # Update rotation for next frame
        self.rotation_angle = (self.rotation_angle + self.rotation_speed) % 360

    def run(self) -> None:
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    self.handle_key(event.key)

            self.screen.fill(self.BG)

            # Draw all completed polygons
            for polygon in self.polygons:
                polygon.draw(self.screen)

            # Draw current polygon
            self.current_polygon.draw(self.screen)

            # Draw preview line from last point to mouse if current polygon is not closed
            if not self.current_polygon.closed and self.current_polygon.points:
                mx, my = pygame.mouse.get_pos()
                last = self.current_polygon.points[-1].to_int_tuple()
                pygame.draw.line(self.screen, self.FG, last, (mx, my), 1)

            # Draw the rotating rectangle
            self.draw_rotating_rectangle()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
