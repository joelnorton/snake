import pygame

from shape import Shape


class Player(Shape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y, radius)
        self.speed = 1
        self.direction = pygame.Vector2(1, 0)
        self.velocity: pygame.Vector2 = self.direction * self.speed
        self.steps = 0
        self.cardinal_direction = 0
        self.change_at = pygame.Vector2(0, 0)
        self.change_direction = pygame.Vector2(0, 0)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, 0)

    def update(self, dt: float) -> None:

        if self.steps >= 20 / self.speed:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and self.direction != pygame.Vector2(1, 0):
                self.direction = pygame.Vector2(-1, 0)
                self.cardinal_direction = 2
                self.change_at = self.position.copy()
            if keys[pygame.K_d] and self.direction != pygame.Vector2(-1, 0):
                self.direction = pygame.Vector2(1, 0)
                self.cardinal_direction = 0
                self.change_at = self.position.copy()
            if keys[pygame.K_w] and self.direction != pygame.Vector2(0, 1):
                self.direction = pygame.Vector2(0, -1)
                self.cardinal_direction = 3
                self.change_at = self.position.copy()
            if keys[pygame.K_s] and self.direction != pygame.Vector2(0, -1):
                self.direction = pygame.Vector2(0, 1)
                self.cardinal_direction = 1
                self.change_at = self.position.copy()
            self.steps = 0
            self.velocity = self.direction * self.speed
        self.steps += 1
        self.position += self.velocity

    def eat(self) -> None:
        pass
        # self.speed += 1
        # self.speed = round(self.speed / 2) * 2

    def collide_wall(self, width: float, height: float) -> bool:
        return (
            self.position.x < 0
            or self.position.x > width
            or self.position.y < 0
            or self.position.y > height
        )
