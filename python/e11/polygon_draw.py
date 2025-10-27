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

        self.polygon = Polygon()
        self.font = pygame.font.Font(None, 20)

        pygame.display.set_caption(
            "Polygon Drawer — Left-click to add points, D to close & fill, R to reset"
        )

    def handle_click(self, pos: Tuple[int, int]) -> None:
        if self.polygon.closed:
            # start a new polygon if the previous is closed
            self.polygon = Polygon()
        self.polygon.add_point(Point(pos[0], pos[1]))

    def handle_key(self, key: int) -> None:
        if key == pygame.K_d:
            closed = self.polygon.close()
            if not closed:
                pygame.display.set_caption(
                    "Need at least 3 points to close the polygon — press R to reset"
                )
            else:
                pygame.display.set_caption(
                    "Polygon closed and filled — left-click to start a new polygon, R to reset"
                )
        elif key == pygame.K_r:
            self.polygon.reset()
            pygame.display.set_caption(
                "Polygon Drawer — Left-click to add points, D to close & fill, R to reset"
            )

    def draw_instructions(self) -> None:
        lines = [
            "Left-click: add point",
            "D: close & fill polygon (needs >=3 points)",
            "R: reset/current polygon",
        ]
        for i, line in enumerate(lines):
            surf = self.font.render(line, True, self.FG)
            self.screen.blit(surf, (8, 8 + i * 20))

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

            # Draw current polygon
            self.polygon.draw(self.screen)

            # Draw preview line from last point to mouse if polygon is not closed
            if not self.polygon.closed and self.polygon.points:
                mx, my = pygame.mouse.get_pos()
                last = self.polygon.points[-1].to_int_tuple()
                pygame.draw.line(self.screen, self.FG, last, (mx, my), 1)

            self.draw_instructions()

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
