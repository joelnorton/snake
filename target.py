import pygame

from shape import Shape


class Target(Shape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        print(self.position)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float) -> None:
        pass
